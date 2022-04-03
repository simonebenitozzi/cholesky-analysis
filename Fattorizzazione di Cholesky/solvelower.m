function x = solvelower(L , b )
%
% ricavo la dimensione di x
%
n = length( b ) ;
x = zeros(n ,1) ;
%
x(1) = b(1)/L(1, 1) ;
%
for i =2:n
    %
    % i e' la riga che sto considerando
    %
    % devo sostituire le incognite gia ' trovate
    % che sono x(1) ,... ,x(i-1)
    %
    s = 0;
    %
    for j = 1:i-1
       s = s + L(i, j)*x(j) ;
    end
    %
    x(i) = ( b(i) -s )/L(i ,i) ;
    %
end

