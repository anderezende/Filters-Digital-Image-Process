import numpy as np
from skimage import data
from skimage import novice
from skimage.novice import Picture
from skimage import data_dir



img = novice.open('noise50.png')

px = img[10,50]
print (px)

width = img.width
heigth = img.height


#filtros lineares Convulação *
matriz = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]

div = 0
novaimagem = np.zeros(shape=(width, heigth, 3), dtype=np.uint8)

for x in range(len(matriz)):
	for y in range(len(matriz)):
		
		div += matriz[x][y]
if(div ==0):
	div = 1

for n in range(width-len(matriz)):
	for n2 in range(heigth-len(matriz)):
		somatorioB = 0
		somatorioG = 0
		somatorioR = 0
		b = 0
		g = 0
		r = 0
		for x in range(len(matriz)):
			for y in range(len(matriz)):
				#blue
				b += int(img[n+x, n2+y].blue) * matriz[x][y]
				#green
				g += int(img[n+x, n2+y].green) * matriz[x][y]
				#red
				r += int(img[n+x,n2+y].red) * matriz[x][y]
				
		#print(r)
		somatorioB = b/div
		somatorioG = g/div
		somatorioR = r/div
		#print(somatorioR)
		
		
			
		if(somatorioB > 255):
			somatorioB = 255
		
		if(somatorioB <0):
			somatorioB = 0
			
		if(somatorioG > 255):
			somatorioG = 255
		if(somatorioG <0):
			somatorioG = 0
		
		if(somatorioR > 255):
			somatorioR = 255
		if(somatorioR <0):
			somatorioR = 0
		
		novaimagem[n, n2] = (somatorioB, somatorioG, somatorioR)

novaimagem = Picture(array=novaimagem)
novaimagem.show() 

		
					