function [error, mem, time] = analyze(A)

% Analyzes the Cholesky decomposition on the sparse Matrix given
% in input
%
% Inputs:
%   A: the Matrix to be analyzed
%
% Outputs:
%   error: the relative error between the expected result and the computed
%       result
%   mem: the difference in memory (expressed in MB) used by MATLAB between 
%       right after the matrix is loaded and after the linear system 
%       solution is computed
%   time: the number of seconds required to compute the solution

    try
        % checks if the input matrix A is sparse
        if(~issparse(A))
            err = MException('analyze:NoSparse', ...
                    'Invalid Input. The matrix given in input is not Sparse');
                throw(err);
        end
    catch exception
        fprintf("Error: %s\n", exception.identifier)
        error = NaN; mem = NaN; time = NaN;
        return
    end
    
    % memory usage before execution (after loading matrix)
    try
        before_mem = memory;
    catch
        [~, pid] = system('pgrep MATLAB');
        [~, mem_usage] = system(['cat /proc/' strtrim(pid) '/status | grep VmSize']);
        before_mem = str2double(strtrim(extractAfter(extractBefore(mem_usage, ' kB'), ':'))) / 1000;
    end

    % problem parameters
    xe = ones(size(A, 1), 1);
    b = A*xe;

    % --- system solving
    try
        tic %starts timing
        
        % Cholesky decomposition (the input matrix A needs to be sparse to apply the amd Permutation)
        [R, flag, P] = chol(A);
        
        % flag checks if A is a Definite Positive Matrix
        if(flag ~= 0)
                err = MException('analyze:NoSPD', ...
                    'Invalid Input. The matrix given in input is not a Positive Definite');
                throw(err);
        end

        % --- solution computing
        
        % x = R\(R'\b); % Solution without using the permutation matrix (inefficient)
        x = P*(R\(R'\(P'*b)));
        
        time = toc; % ends timing
    catch exception
        fprintf("Error: %s\n", exception.identifier)
        error = NaN; mem = NaN; time = NaN;
        return
    end

    % --- memory usage estimation
    try
        after_mem = memory;
        % difference and MB conversion
        mem = (after_mem.MemUsedMATLAB - before_mem.MemUsedMATLAB) * 1e-6;
    catch
        [~, pid] = system('pgrep MATLAB');
        [~, mem_usage] = system(['cat /proc/' strtrim(pid) '/status | grep VmSize']);
        after_mem = str2double(strtrim(extractAfter(extractBefore(mem_usage, ' kB'), ':'))) / 1000;

        mem = after_mem - before_mem;
    end

    % --- error estimation
    error = norm(x - xe, 2) / norm(xe, 2);

end