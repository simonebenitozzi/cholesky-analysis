function [error, mem, time] = analyze(matrix_path)

% Analyzes the Cholesky decomposition on sparse Matrix, whose path is given
% in input
%
% Inputs:
%   matrix_path: full path of the file containing the matrix to be analyzed
%
% Outputs:
%   error: the relative error between the expected result and the computed
%       result
%   mem: the difference in memory (expressed in MB) used by MATLAB between 
%       right after thematrix is loaded and after the linear system 
%       solution is computed
%   time: the number of seconds required to compute the solution

    load(matrix_path, 'Problem');
    A = Problem.A;
    clear Problem matrix_path
    
    % memory usage before execution (after loading matrix)
    before_mem = memory;

    % problem parameters
    xe = ones(size(A, 1), 1);
    b = A*xe;

    % --- system solving
    try
        tic %starts timing
        
        % Cholesky decomposition
        [R] = chol(A);

        % solution computing
        x = R\(R'\b);

        time = toc; % ends timing
    catch exception
        fprintf("Error: %s\n", exception.identifier)
        error = NaN; mem = NaN; time = NaN;
        return
    end

    % --- error estimation
    error = norm(x - xe, 2) / norm(xe, 2);
    
    % --- memory usage estimation
    after_mem = memory;
    mem_difference_bytes = after_mem.MemUsedMATLAB-before_mem.MemUsedMATLAB;
    %conversion in MegaBytes
    mem = mem_difference_bytes*1e-6;
    
end