import sys
import numpy as np
N = int(sys.argv[1])

while (N > 0):
	n = np.random.randn(1)[0]
	final_no = 1750 + n*50
	if(final_no >= 0):
		print(final_no)
		N = N - 1
	
