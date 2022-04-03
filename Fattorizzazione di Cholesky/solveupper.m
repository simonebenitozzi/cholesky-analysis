function x = solveupper(U, b)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% solveupper risolve il sistema Ux = b con U matrice triangolare superiore
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%
% ricavo la dimensione di x
%
n = length(b);

x = zeros(n ,1);
%
x(n) = b(n)/U(n, n) ;
%
for i =n-1:-1:1
    %
    % i e' la riga che sto considerando
    %
    % devo sostituire le incognite gia ' trovate
    % che sono x(i+1) ,... ,x(n)
    %
    s = 0;
    %
    for j = i +1: n
       s = s + U (i,j)*x(j);
    end
    %
    x(i) = (b(i) - s)/U(i,i);
    %
end

