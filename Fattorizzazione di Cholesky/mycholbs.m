function x = mycholbs(A, b)

%
% soluzione sistema lineare con fattorizzazione di Cholesky
%
[R, p] = mychol(A);

if p > 0
   disp('non posso applicare Cholesky')
   return
else
   y = solvelower(R', b);
%
   x = solveupper(R, y);    
end    