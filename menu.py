from PIL import Image
import numpy as np

def choose_pic():
	mypic = open ("mypic", "r")
	mynames = mypic.read()
	print (mynames)
	mypic.close()
	filename = raw_input("Choose image:")
	fullname = "./pic/" + filename + ".bmp"
	image = Image.open(fullname)
	return image, filename
