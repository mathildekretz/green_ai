import numpy as np
from numba import jit
from time import time
from tqdm import tqdm
import matplotlib.pyplot as plt

@jit(nopython=True, cache=True, fastmath=False)
def loop_naive(v_size, rad, A, B):
	# Add your hown naive 6-loop implementation
	for k in range(rad, v_size-rad):
		for j in range(rad, v_size-rad):
			for i in range(rad, v_size-rad):
				for z in range(-rad, rad):
					for y in range(-rad, rad):
						for x in range(-rad, rad):
							B[i, j, k] += A[i+x, j+y, k+z]


def loop_vectorial_sub_cube(v_size, rad, A, B):
	for i in range(rad, v_size - rad):
		for j in range(rad, v_size - rad):
			for k in range(rad, v_size - rad):
				B[i, j, k] = np.sum(A[i-rad:i+rad+1, j-rad:j+rad+1, k-rad:k+rad+1])


@jit(nopython=True, cache=True, fastmath=False)
def loop_vectorial_radius(v_size, rad, A, B):
	for dx in range(-rad, rad+1):
		for dy in range(-rad, rad+1):
			for dz in range(-rad, rad+1):
				B[rad:-rad, rad:-rad, rad:-rad] += A[rad+dx:v_size-rad+dx, rad+dy:v_size-rad+dy, rad+dz:v_size-rad+dz]



v_size = 128
rad = 20

# Initialize A with values using broadcasting
x, y, z = np.ogrid[:v_size, :v_size, :v_size]
A = (x + y + z).astype("float32")

# Initialize B as an empty array with the same shape as A
B = np.zeros_like(A).astype("float32")		
# loop_naive(v_size,rad,A,B)
# loop_vectorial_sub_cube(v_size,rad,A,B)
loop_vectorial_radius(v_size,rad,A,B)

print(B[v_size//2, v_size//2, v_size//2])
