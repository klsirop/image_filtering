from PIL import Image
import numpy as np
import time

def module_difference(arr, new_arr, mod_diff, arr_wid, arr_hei):
	j = 0
	while (j < arr_hei):
		i = 0
		while (i < arr_wid):
			tmp = int(arr[j][i]) - int(new_arr[j][i])
			if (tmp == 1):
				print ("arr[j][i]=" + str(arr[j][i]) + " new_arr[j][i]=" + str(new_arr[j][i]) + " i=" + str(i) + " j=" + str(j))
			if (tmp >= 0):
				mod_diff[j][i] = tmp
			else:
				mod_diff[j][i] = tmp * (-1)
			i += 1
		j += 1

def decorator_mod(func):
	def decorate_mod(arr, new_arr, mod_diff, arr_wid, arr_hei):
		t1 = time.time()
		module_difference(arr, new_arr, mod_diff, arr_wid, arr_hei)
		t2 = time.time()
		print ('%r %2.2f ms' % ("function: " + func.__name__ + ", image_wid=" + arr_wid.__str__() + ", image_hei=" + arr_hei.__str__(), (t2 - t1)))
	return decorate_mod

