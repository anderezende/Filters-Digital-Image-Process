import numpy as np
import random
from skimage import data
from skimage import novice
from skimage.novice import Picture
from skimage import data_dir




img = novice.open('noise50.png')

px = img[10,50]
print (px)


def CalcLines(radius):
	return radius*2+1	

	
width = img.width
heigth = img.height

for n in range(width):
	for n2 in range(heigth):
		b = 0.07 * img[n,n2].blue
		g = 0.72 * img[n,n2].green
		r = 0.21 * img[n,n2].red
		aux = (g+b+r)
		img[n,n2] = (aux,aux,aux)

Xline = 0
Yline = 0
radius = 3
lines = CalcLines(radius)
maxArray = lines*lines
avgL = []


def mediaNoise():
	novaimagem = np.zeros(shape=(width, heigth, 3), dtype=np.uint8)
	for n in range(width):
		for n2 in range(heigth):
			c = 0
			#avgL = maxArray
			avgL.clear()
			#print('Lines:', lines)
			for x in range(lines):
				Xline = n+(x-radius)
				for y in range(lines):
					Yline = n2+(y-radius)
					if(Xline >= 0 and Xline < width and Yline >= 0 and Yline < heigth):
						
						
						avgL.append(img[Xline, Yline].blue)
						
						c += 1
						
			
			avgL.sort()
			median = int(c/2)
			#print(median)
			
			#print(' --------------- ',avgL,' ------------------- ')

			novaimagem[n, n2] = (avgL[median], avgL[median], avgL[median])

	novaimagem = Picture(array=novaimagem)
	novaimagem.show() 
	

mediaNoise()



