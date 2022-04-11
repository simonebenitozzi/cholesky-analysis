clear all, close all, clc

% --- matrix loading
folder_path = '';
matrix_name = 'ex15.mat';
matrix_path = strcat(folder_path, matrix_name);
load(matrix_path)
A = Problem.A;
% spy(A)
clear Problem matrix_path folder_path matrix_name

% memory usage before execution (after loading matrix)
before_mem = memory;

% problem parameters
xe = ones(size(A, 1), 1);
b = A*xe;

% --- system solving

tic %starts timing
% Cholesky decomposition
R = chol(A);

% solution computing
x = R\(R'\b);

time = toc; % ends timing
fprintf("Time elapsed: %f seconds\n", time)

% --- error estimation
err = norm(x - xe, 2) / norm(xe, 2);
fprintf("\nRelative error: %e\nepsilon: %e\n", err, eps(1))

% --- memory usage estimation
after_mem = memory;
mem_difference = after_mem.MemUsedMATLAB-before_mem.MemUsedMATLAB;
mem_difference_mb = mem_difference*1e-6;
fprintf("\nTotal memory used by MATLAB: %e bytes (%f MB)\n", mem_difference, mem_difference_mb)
