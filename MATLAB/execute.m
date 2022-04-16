clear all, close all, clc %#ok<CLALL,DUALC> 

cd ..
prev_path = pwd;
files = dir(strcat(prev_path, '\Matrix\*.mat'));
cd MATLAB

%data = ["name", "rows", "columns", "error", "memory", "time", "language", "operatingSystem"];
%writematrix(data, filename);

filename = strcat(prev_path, '\Analysis\resources\', 'data.csv');

clearvars -except files filename
for i=1:length(files)
    
    fprintf("-----------------------------------\n");

    load(strcat(files(i).folder, '\', files(i).name), 'Problem');
    A = Problem.A;
    clear Problem
    
    [~, matrix_name, ~] = fileparts(files(i).name);
    fprintf("Matrix: %s\n", matrix_name);
    
    [error, mem, time] = analyze(A);
    
    if (~isnan(error))
        fprintf("\nRelative error: %e\n", error)
    end
    if (~isnan(time))
        fprintf("Time elapsed: %f seconds\n", time)
    end
    if (~isnan(mem))
        fprintf("Total memory used by MATLAB: %f MB\n", mem)
    end
    fprintf("-----------------------------------\n\n");
    
    % "os" column will be 0 for Windows, 1 otherwise
    data = [matrix_name, string(size(A,1)), string(size(A,2)), string(error), string(mem), string(time), string(0), string(double(~ispc))];
    writematrix(data,filename,'WriteMode','append');
    
    % clear all variables except the ones needed for the iteration
    clearvars -except files filename i
end
