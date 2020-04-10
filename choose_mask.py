from PIL import Image
import numpy as np

def fill_mask(mask, a, n, ch):
	for i in range (n):
		mask[a[i]] = ch
	return mask

def choose_fil_k(fil_n):
	print ("Choose fil_k from 1 to " + str(fil_n))
	fil_k = input()
	return fil_k

def show_masks():
	print ("1 - standart1:")
	print ("0 1 0\n1 2 1\n0 1 0\n")
	print ("2 - big1:")
	print ("0 0 1 0 0\n0 2 4 2 0\n1 4 8 4 1\n0 2 4 2 0\n0 0 1 0 0\n")
	print("3 - rare:")
	print("1 0 1\n0 1 0\n1 0 1\n")
	print("4 - standart1+1:")
	print("1 2 1\n2 4 2\n1 2 1\n")
	print("5 - usual:")
	print("1 1 1\n1 1 1\n1 1 1\n")
	print("6 - usual+:")
	print("1 1 1\n1 2 1\n1 1 1\n")

def choose_mask():
	print ("Choose mask:")
	print ("1 - standart1\n2 - big1\n3 - rare\n4 - standart1+1\n5 - usual\n6 - usual+\n7 - create mask")
	print ("you may use 'help'")

	choose = raw_input()
	if (choose != 7 and choose == "help"):
		show_masks()
		choose = input()
	else:
		choose = int(choose)

	if (choose == 7):
		mask_wid = input("put width: ")
		mask_hei = input("put height: ")
		mask = np.zeros((mask_hei, mask_wid), dtype=np.uint8)
		fil_n = 0
		for j in range(mask_hei):
			mask[j] = map(int, raw_input().split())
			for i in range(mask_wid):
				fil_n += mask[j][i]
		print (mask)
		print ("fil_n=" + str(fil_n))
		mask_name = "mymask"



	if (choose == 1):
		mask_wid, mask_hei = 3, 3
		mask = np.zeros((mask_hei, mask_wid), dtype=np.uint8)
		fill_mask(mask, [(0,1), (1,0), (1,2), (2,1)], 4, 1)
		mask[1][1] = 2
		fil_n = 4 * 1 + 2
		mask_name = "standart1"

	elif (choose == 2):
		mask_wid, mask_hei = 5, 5
		mask = np.zeros((mask_hei, mask_wid), dtype=np.uint8)
		fill_mask(mask, [(0, 2), (2,0), (2,4), (4,2)], 4, 1)
		fill_mask(mask, [(1,1), (1,3), (3,1), (3,3)], 4, 2)
		fill_mask(mask, [(1,2), (2,1), (2,3), (3,2)], 4, 4)
		mask[2][2] = 8
		fil_n = 4 * 1 + 4 * 2 + 4 * 4 + 8
		mask_name = "big1"

	elif (choose == 3):
		mask_wid, mask_hei = 3, 3
		mask = np.zeros((mask_hei, mask_wid), dtype=np.uint8)
		fill_mask(mask, [(0,0), (0,2), (1,1), (2,0), (2,2)], 5, 1)
		fil_n = 5 * 1
		mask_name = "chess"

	elif (choose == 4):
		mask_wid, mask_hei = 3, 3
		mask = np.zeros((mask_hei, mask_wid), dtype=np.uint8)
		fill_mask(mask, [(0,0), (0,2), (2,0), (2,2)], 4, 1)
		fill_mask(mask, [(0,1), (1,0), (1,2), (2,1)], 4, 2)
		mask[1][1] = 4
		fil_n = 4 * 1 + 4 * 2 + 4
		mask_name = "standart1+1"

	elif (choose == 5):
		mask_wid, mask_hei = 3, 3
		mask = np.zeros((mask_hei, mask_wid), dtype=np.uint8)
		fill_mask(mask, [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)], 9, 1)
		fil_n = 9 * 1
		mask_name = "usual"

	elif (choose == 6):
		mask_wid, mask_hei = 3, 3
		mask = np.zeros((mask_hei, mask_wid), dtype=np.uint8)
		fill_mask(mask, [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)], 8, 1)
		mask[1][1] = 2
		fil_n = 8 * 1 + 2
		mask_name = "usual+"


	fil_k = choose_fil_k(fil_n)

	print (mask)
	return mask, mask_wid, mask_hei, fil_n, fil_k, mask_name
