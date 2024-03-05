import numpy as np
import matplotlib.pyplot as plt
from loop_seq_start import loop_naive, loop_vectorial_radius, loop_vectorial_sub_cube
from time import time
import tqdm

#v_size = 64
grd_pte_boucle = np.array([27.7, 35.5, 27.5, 27.8, 27.6])
grd_pte_boucle_rdm = np.array([21.2, 20.79, 22.1, 21.4])
pte_grd_boucle = np.array([32.3, 34.2, 40])

#v_size = 32
grd_pte_boucle_32 = np.array([4.27, 3.31, 3])

#v_size = 128
grd_pte_boucle_128 = np.array([348.7])

#rad = 5
grd_pte_boucle_5 = np.array([122.11])

#rad = 1 
grd_pte_boucle_1 = np.array([4.07, 4.33])

#numba vsize puis rad
grd_pte_boucle_numba_64_3 = np.array([2.44, 2.1, 1.97])
grd_pte_boucle_numba_32 = np.array([2.23, 2.0, 1.7])
grd_pte_boucle_numba_128 = np.array([3.76, 3.33, 3.8])
grd_pte_boucle_numba_5 = np.array([6.2, 4.35, 4.24])
grd_pte_boucle_numba_1 = np.array([3.7, 2.7, 1.88, 3.15])

#radius
radius_64_3 = np.array([1.58, 1.49, 1.2])
radius_32 = np.array([1.00, 1.37, 0.97])
radius_128 = np.array([1.80, 1.16, 1.29])
radius_5 = np.array([1.20, 1.20, 1.36])
radius_1 = np.array([1.20, 1.28, 1.2])

#scaling curve q.13
vsize_list = [256, 128, 64, 32, 16, 8, 512]
vsize_times_c = [6.64, 0.93, 0.3, 0.20, 0.23, 0.25, 74.7]
radius_list = [3, 5, 10, 20, 40, 60, 50]
radius_times_c = [0.93, 3.18, 16.09, 60.6, 84, 1.34, 28.68]
vsize_times_python = [32.58, 8.77, 3.45, 3.0, 3.29, 3.42, 386]
radius_times_python = [8.77, 21.12, 149]
plt.plot(vsize_list, vsize_times_c, label=r"compile with C and -O3, $radius=3$", color='yellowgreen')
plt.plot(vsize_list, vsize_times_python, label=r"vectorial radius compiled with Numba, $radius=3$", color='cornflowerblue')
plt.xlabel(r"$v_{size}$")
plt.ylabel('time [s]')
plt.title('Comparison of scaling curves between C and Python')
#plt.show()
plt.savefig('q13_vsize.png')

plt.plot(radius_list, radius_times_c, label=r"compile with C and -O3, $v_{size}=128$", color='yellowgreen')
plt.plot(radius_list, radius_times_c, label=r"vectorial radius compiled with Numba, $v_{size}=128$", color='cornflowerblue')
plt.xlabel(r"$radius$")
plt.ylabel('time [s]')
plt.title('Comparison of scaling curves between C and Python')
#plt.show()
plt.savefig('q13_radius.png')

#means
print(grd_pte_boucle_5.mean())
v_size = [32, 64, 128]
rad = [1, 3, 5]
naive_vsize = [grd_pte_boucle_32.mean(), grd_pte_boucle_rdm.mean(), grd_pte_boucle_128.mean()]
naive_rad = [grd_pte_boucle_1.mean(), grd_pte_boucle_rdm.mean(), grd_pte_boucle_5.mean()]
numba_vsize = [grd_pte_boucle_numba_32.mean(), grd_pte_boucle_numba_64_3.mean(), grd_pte_boucle_numba_128.mean()]
numba_rad = [grd_pte_boucle_numba_1.mean(), grd_pte_boucle_numba_64_3.mean(), grd_pte_boucle_numba_5.mean()]
radius_vsize = [radius_32.mean(), radius_64_3.mean(), radius_128.mean()]
radius_rad = [radius_1.mean(), radius_64_3.mean(), radius_5.mean()]



