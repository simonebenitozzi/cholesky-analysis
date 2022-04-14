clear all, close all, clc

cd ..
current_path = pwd;
files = dir(strcat(current_path, '\Matrix\*.mat'));
N = length(files);

% data preallocation
data = strings(N+1, 4);
data(1,:) = ["name", "error", "memory", "time"];

for i=1:N
    fprintf("-----------------------------------\n");
    
    % --- matrix loading
    folder_path = files(i).folder;
    matrix_name = files(i).name;
    matrix_path = strcat(folder_path, '\', matrix_name);
    load(matrix_path)
    A = Problem.A;
    % spy(A)
    
    [~, matrix_name, ~] = fileparts(matrix_name);
    fprintf("Matrix: %s\n", matrix_name);
    clear Problem matrix_path folder_path

    % memory usage before execution (after loading matrix)
    before_mem = memory;

    % problem parameters
    xe = ones(size(A, 1), 1);
    b = A*xe;

    % --- system solving

    try
        tic %starts timing
        % Cholesky decomposition

        R = chol(A);

        % solution computing
        x = R\(R'\b);

        time = toc; % ends timing
        fprintf("Time elapsed: %f seconds\n", time)

    catch exception
        fprintf("Error: %s\n", exception.identifier)
        
        data(i+1,:) = [matrix_name, "", "", ""];
        continue
    end
    
    % --- error estimation
    err = norm(x - xe, 2) / norm(xe, 2);
    fprintf("\nRelative error: %e\nepsilon: %e\n", err, eps(1))

    % --- memory usage estimation
    after_mem = memory;
    mem_difference = after_mem.MemUsedMATLAB-before_mem.MemUsedMATLAB;
    mem_difference_mb = mem_difference*1e-6;
    fprintf("\nTotal memory used by MATLAB: %e bytes (%f MB)\n", mem_difference, mem_difference_mb)
    fprintf("-----------------------------------\n\n\n");
    
    data(i+1, :) = [matrix_name, string(err), string(mem_difference_mb), string(time)];
end

writematrix(data, 'matlab.csv')