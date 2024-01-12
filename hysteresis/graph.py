import numpy as np 

import matplotlib.pyplot as plt 

 

# Load data from a text file, assuming delimiter is whitespace. 

# Skip the header row if there is one. 

path = 'C:\\Users\\Lab Student D\\OneDrive \- Imperial College London\\Desktop\\Chris_aryan\\C2_micromagnetics\\hysteresis\\table.txt'
data = np.loadtxt(path, skiprows=1)

 

# Assuming m_x is in the first column and B_ext in the third column. 

m_x = data[:, 1] 

B_ext = data[:, 4] 

 

# Create a plot of m_x against B_ext. 

plt.figure(figsize=(10, 6)) 

plt.plot(B_ext, m_x, 'o-', label='m_x vs B_ext')  # 'o-' gives us points connected by lines 

plt.xlabel('B_ext (T)') 

plt.ylabel('m_x') 

plt.title('Plot of m_x vs B_ext') 

plt.legend() 

plt.grid(True) 
plt.savefig('hysteresis\\graph.png')
plt.show()