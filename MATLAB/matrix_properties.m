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

    [~, matrix_name, ~] = fileparts(files(i).name);
    fprintf("Matrix: %s\n", matrix_name);
    
    if(strcmp(matrix_name, "StocF-1465") || strcmp(matrix_name, "Flan_1565"))
        continue
    end
    
    A = Problem.A;
    clear Problem

    conditioning = condest(A);
    data = [matrix_name, string(nnz(A)), string(conditioning)];
    writematrix(data,filename,'WriteMode','append');

    fprintf("-----------------------------------\n\n");
    
    % clear all variables except the ones needed for the iteration
    clearvars -except files filename i
end