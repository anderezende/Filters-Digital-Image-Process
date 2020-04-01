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
for n in range(width):
	for n2 in range(heigth):
		b = 0.07 * int(img[n, n2].blue)
		g = 0.72 * int(img[n, n2].green)
		r = 0.21 * int(img[n, n2].red)
		aux = (g+b+r)
		img[n, n2] = (aux,aux,aux)

#filtros lineares Convulação *
matrizX = [[1,0,-1],[2,0,-2],[1,0,1]]
matrizY = [[1,2,1],[0,0,0],[-1,-2,-1]]

div = 0
novaimagem = np.zeros(shape=(width, heigth, 3), dtype=np.uint8)
pad = (len(matrizX)-1)/2

for n in range(width-len(matrizX)):
	for n2 in range(heigth-len(matrizX)):
		somatorioBX = 0
		somatorioGX = 0
		somatorioRX = 0
		somatorioBY = 0
		somatorioGY = 0
		somatorioRY = 0
		bX = 0
		gX = 0
		rX = 0
		bY = 0
		gY = 0
		rY = 0
		divY = 0
		divX = 0
		
		for x in range(len(matrizX)):
			for y in range(len(matrizX)):
				#blue
				Xpos = n+x-pad
				Ypos = n2+y-pad
				if(Xpos >= 0 and Xpos < heigth and Ypos >= 0 and Ypos < width):
					bX += int(img[n+x, n2+y].blue) * matrizX[x][y]
					gX += int(img[n+x, n2+y].green) * matrizX[x][y]
					rX += int(img[n+x,n2+y].red) * matrizX[x][y]
					
					bY += int(img[n+x, n2+y].blue) * matrizY[x][y]
					gY += int(img[n+x, n2+y].green) * matrizY[x][y]
					rY += int(img[n+x,n2+y].red) * matrizY[x][y]
			
					divX += matrizX[x][y]
					divY += matrizY[x][y]

		if(divX ==0): divX = 1
		if(divY ==0): divY = 1
		somatorioBX = bX/divX
		somatorioGX = gX/divX
		somatorioRX = rX/divX
		
		somatorioBY = bX/divY
		somatorioGY = gX/divY
		somatorioRY = rX/divY
		
		GRX = (somatorioBX**2 + somatorioBY**2)
		GGX = (somatorioGX**2 + somatorioGY**2)
		GBX = (somatorioRX**2 + somatorioRY**2)
		
		GRX = GRX **(1/2)
		GGX = GGX **(1/2)
		GBX = GBX **(1/2)
		
		if(GRX > 255):
			GRX = 255
		
		if(GRX <0):
			GRX = 0
			
		if(GGX > 255):
			GGX = 255
		if(GGX <0):
			GGX = 0
		
		if(GBX > 255):
			GBX = 255
		if(GBX <0):
			GBX = 0
		
		novaimagem[n, n2] = (GRX, GGX, GBX)

novaimagem = Picture(array=novaimagem)
novaimagem.show() 
