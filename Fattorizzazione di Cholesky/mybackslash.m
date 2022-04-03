function x = mybackslash(A, b)

%
% soluzione sistema lineare con il medesimo flow-chart del \ di MATLAB
%

[R, p] = mychol(A);

if p == 0
   disp('utilizzo la fattorizzazione di Cholesky') 
   y = solvelower(R', b);
   x = solveupper(R, y);     
else    
   disp('utilizzo la fattorizzazione LU') 
   x = mybackslash_pivot_totale(A, b);
end   
    