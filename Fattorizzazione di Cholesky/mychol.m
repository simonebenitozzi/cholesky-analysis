function [R, p] = mychol(A)
%
% 
% R matrice triangolare superiore tale che R'*R = A
% p parametro: se p = 0 allora A è definita positiva e A = R'*R,
%              se p > 0 allora A non è definita positiva 
%                       q = p-1; R(1:q, 1:q)'*R(1:q, 1:q) = A(1:q, 1:q)
%
n = size(A ,1);
%
R = zeros(n,n);


%
for k=1:n
%  
    if (A(k,k) <= 0)
        disp('la matrice non è definita positiva')
        p = k;
        return
    else    
        R(k,k) = sqrt(A(k,k));
    %
        for i=k+1:n
            R(k,i) = A(k,i)/R(k,k);
        end
    %   
    %   in forma vettoriale più compatta
    %   R(k, k+1:n) = A(k, k+1:n)/R(k,k);
    %
        for i=k+1:n
            for j=k+1:n
                A(i,j) = A(i,j) - 1/A(k,k)*A(i,k)*A(k,j);
            end
        end
    %   
    %   in forma vettoriale più compatta
    %   A(k+1:n, k+1:n) = A(k+1:n, k+1:n) -1/A(k,k)*A(k+1:n, k)*A(k, k+1:n);
    %    
    end    
end    
p = 0;