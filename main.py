from PIL import Image
import numpy as np
from menu import *
from choose_mask import *
from rang_filter import *
from module_difference import *

def create_arr_from_image(image):
	load_image = image.load()
	arr_wid, arr_hei = image.size
	arr = np.zeros((arr_hei, arr_wid), dtype=np.uint8)
	j = 0
	while (j < arr_hei):
		i = 0
		while (i < arr_wid):
			arr[j][i] = load_image[i, j]
			i += 1
		j += 1
	return arr, arr_wid, arr_hei

def main():
	image, filename = choose_pic()
	image.show()

	mask, mask_wid, mask_hei, fil_n, fil_k, mask_name = choose_mask()
	arr, arr_wid, arr_hei  = create_arr_from_image(image)
	range_filter_dec = decorator(rang_filter)

	new_arr = np.zeros((arr_hei, arr_wid), dtype=np.uint8)
	range_filter_dec(arr, arr_wid, arr_hei, mask, mask_wid, mask_hei, fil_n, fil_k, new_arr)
	new_image = Image.fromarray(new_arr)
	new_image.show()

	fullname = "./save/" + filename + "_" + mask_name + "_" + str(fil_k) + "%" + str(fil_n) + ".bmp"
	new_image.save(fullname, 'BMP')

	mod_diff = np.zeros((arr_hei, arr_wid), dtype=np.uint8)
	module_difference_dec = decorator_mod(module_difference)
	module_difference_dec(arr, new_arr, mod_diff, arr_wid, arr_hei)
	diff_image = Image.fromarray(mod_diff)
	diff_image.show()
	fullname = "./save/diff/" + filename + "_" + mask_name + "_" + str(fil_k) + "_" + str(fil_n) + "_diff.bmp"
	new_image.save(fullname, 'BMP')

main()
