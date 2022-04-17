clear all, close all, clc %#ok<CLALL,DUALC> 

cd ..
prev_path = pwd;
if (ispc)
    files = dir(strcat(prev_path, '\Matrix\*.mat'));
    filename = strcat(prev_path, '\Analysis\resources\', 'data.csv');
else
    files = dir(strcat(prev_path, '/Matrix/*.mat'));
    filename = strcat(prev_path, '/Analysis/resources/', 'data.csv');
end
cd MATLAB

%data = ["Name", "Dim", "Nnz", "Cond", "Error", "Memory", "Time", "Language", "OperatingSystem"];
%writematrix(data, filename);

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
    
    [error, mem, time] = analyze(A);
    
    if (~isnan(error) || ~isnan(time) || ~isnan(mem))
        fprintf("\nRelative error: %e\n", error)
        fprintf("Time elapsed: %f seconds\n", time)
        fprintf("Total memory used by MATLAB: %f MB\n", mem)

        conditioning = condest(A);

        % "os" column will be 0 for Windows, 1 otherwise
        data = [matrix_name, string(size(A,1)), string(nnz(A)), string(conditioning), string(error), string(mem), string(time), string(0), string(double(~ispc))];
        writematrix(data,filename,'WriteMode','append');
    end

    fprintf("-----------------------------------\n\n");
    
    % clear all variables except the ones needed for the iteration
    clearvars -except files filename i
end
