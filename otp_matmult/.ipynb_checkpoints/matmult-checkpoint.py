import numpy as np
#from numba import jit

#@jit(nopython=True, cache=True, fastmath=False)
def matmul_naive(A, B, M, N, K):
	# Add your own naive 3-loop implementation here
    C = np.zeros((M,N))
    for i in range(M):
        for j in range(N):
            cij = 0
            for k in range(K):
                cij += A[i,k]*B[k,j]
            C[i,j] = cij
    return C

M = 256
N = 256
K = 256

np.random.seed(0)

A = (np.random.random((M,K))-0.5)*0.1
B = (np.random.random((K,N))-0.5)-0.1

#C = matmul_naive(A,B,M,N,K)
#C = A @ B
C = np.matmul(A,B)

print (C[M//2,N//2])
