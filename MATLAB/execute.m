clear all, close all, clc

cd ..
current_path = pwd;
files = dir(strcat(current_path, '\Matrix\*.mat'));
cd MATLAB

data = ["name", "error", "memory", "time", "language", "os"];
filename = 'matlab.csv';
writematrix(data, filename);

clearvars -except files filename
for i=1:length(files)
    
    fprintf("-----------------------------------\n");

    folder_path = files(i).folder;
    matrix_name = files(i).name;
    matrix_path = strcat(folder_path, '\', matrix_name);
    
    [~, matrix_name, ~] = fileparts(matrix_name);
    fprintf("Matrix: %s\n", matrix_name);
    
    [error, mem, time] = analyze(matrix_path);
    
    fprintf("\nRelative error: %e\n", error)
    fprintf("Time elapsed: %f seconds\n", time)
    fprintf("Total memory used by MATLAB: %f MB\n", mem)

    fprintf("-----------------------------------\n\n");
    
    % "os" column will be 0 for Windows, 1 otherwise
    data = [matrix_name, string(error), string(mem), string(time), string(0), string(double(~ispc))];
    writematrix(data,filename,'WriteMode','append');
    
    % clear all variables except the ones needed for the iteration
    clearvars -except files filename i
end
