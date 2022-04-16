clear all, close all, clc %#ok<CLALL,DUALC> 

cd ..
prev_path = pwd;
if (ispc)
    files = dir(strcat(prev_path, '\Matrix\*.mat'));
    filename = strcat(prev_path, '\Analysis\resources\', 'data2.csv');
else
    files = dir(strcat(prev_path, '/Matrix/*.mat'));
    filename = strcat(prev_path, '/Analysis/resources/', 'data2.csv');
end
cd MATLAB

data = ["Name", "Nnz", "Cond"];
writematrix(data, filename);

clearvars -except files filename
for i=1:length(files)
    
    fprintf("-----------------------------------\n");

    if(ispc)
        load(strcat(files(i).folder, '\', files(i).name), 'Problem');
    else
        load(strcat(files(i).folder, '/', files(i).name), 'Problem');
    end
    
    A = Problem.A;
    clear Problem
    
    [~, matrix_name, ~] = fileparts(files(i).name);
    fprintf("Matrix: %s\n", matrix_name);

    conditioning = condest(A);
    data = [matrix_name, string(nnz(A)), string(conditioning)];
    writematrix(data,filename,'WriteMode','append');

    fprintf("-----------------------------------\n\n");
    
    % clear all variables except the ones needed for the iteration
    clearvars -except files filename i
end