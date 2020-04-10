from PIL import *
import numpy as np
import time

def print_arr(arr, arr_wid, arr_hei):
	print ("PRINTING ARR:")
	j = 0
	while (j < 10):
		i = 0
		while (i < arr_wid):
			print (arr[j][i]),
			i += 1
		print ("")
		j += 1

def ft_calc_for_apert(arr, center_i, center_j, mask, mask_wid, mask_hei, ite, new_arr, fil_k):
	fil_k1 = 0
	j = center_j - mask_hei / 2
	mask_j = 0
	while (j <= center_j + mask_hei / 2):
		i = center_i - mask_wid / 2
		mask_i = 0
		while (i <= center_i + mask_wid / 2):
			if (arr[j][i] == 255):
				mn = 0
			else:
				mn = 1
			fil_k1 += mn * mask[mask_j][mask_i]
			if (fil_k1 >= fil_k):
				new_arr[center_j][center_i] = 0
				break ;
			i += 1
			mask_i += 1
		j += 1
		mask_j += 1

	if (fil_k1 < fil_k):
		new_arr[center_j][center_i] = 255


def rang_filter(arr, arr_wid, arr_hei, mask, mask_wid, mask_hei, fil_n, fil_k, new_arr):
	ite = 3
	center_j = 0 + (mask_hei / 2)
	while (center_j < arr_hei - mask_hei / 2):
		center_i = 0 + (mask_wid / 2)
		while (center_i < arr_wid - mask_wid / 2):
			ft_calc_for_apert(arr, center_i, center_j, mask, mask_wid, mask_hei, ite, new_arr, fil_k)
			ite += 1
			center_i += 1
		center_j += 1
	return new_arr

def decorator(func):
	def decorate(arr, arr_wid, arr_hei, mask, mask_wid, mask_hei, fil_n, fil_k, new_arr):
		t1 = time.time()
		rang_filter(arr, arr_wid, arr_hei, mask, mask_wid, mask_hei, fil_n, fil_k, new_arr)
		t2 = time.time()
		print ('%r %2.2f ms' % ("function: " + func.__name__ + ", image_wid=" + arr_wid.__str__() + ", image_hei=" + arr_hei.__str__(), (t2 - t1)))
	return decorate

