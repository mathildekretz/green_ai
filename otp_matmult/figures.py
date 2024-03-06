import numpy as np
import matplotlib.pyplot as plt


#scaling curve q.10
matsize_list = [32, 64, 128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280, 1408, 1536, 1664, 1792, 1920, 2048]
matsize_times_o3 = [1.8e-5, 4.2e-4, 1.4e-3, 6.6e-3, 2.4e-2, 5.6e-2, 0.17, 0.26, 0.35, 0.46, 0.60, 0.84, 1.11, 1.45, 1.85, 2.31, 2.93, 3.50]
matsize_times_o2 = [9.8e-5, 7.6e-4, 1.4e-3, 1.0e-2, 3.2e-2, 7.2e-2, 0.13, 0.21, 0.32, 0.47, 0.65, 0.89, 1.17, 1.53, 1.92, 2.40, 2.95, 3.62]
plt.plot(matsize_list, matsize_times_o2, label=r"compile with C and -O2", color='orangered')
plt.plot(matsize_list, matsize_times_o3, label=r"compile with C and -O3", color='deeppink')
plt.xlabel(r"marix size")
plt.ylabel('time [s]')
plt.title('Scaling curves for vectorized matmult in C')
plt.legend()
plt.savefig('q10.png')
plt.clf()

#scaling curve q12
matsize_list = [256, 512, 768, 1024, 1408, 1664, 2048]
matsize_times_o3 = [5.7e-3, 3.3e-2, 0.10, 0.23, 0.58, 0.97, 1.87]
matsize_times_o2 = [5.7e-3, 4.2e-2, 0.13, 0.27, 0.64, 1.01, 2.0]
plt.plot(matsize_list, matsize_times_o2, label=r"compile with C and -O2", color='orangered')
plt.plot(matsize_list, matsize_times_o3, label=r"compile with C and -O3", color='deeppink')
plt.xlabel(r"marix size")
plt.ylabel('time [s]')
plt.title('Scaling curves for vectorized matmult in C')
plt.legend()
plt.savefig('q12.png')
plt.clf()