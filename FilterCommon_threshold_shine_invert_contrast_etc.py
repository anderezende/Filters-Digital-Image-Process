import cv2
import numpy as np

img = cv2.imread('flower.jpg')
px = img[100,100]
print (px)
# accessing only blue pixel
blue = img[100,100,0]
print (blue)
# accessing only red pixel bgr
red = img[100,100,2]
print (red)


# accessing only green pixel bgr
green = img[100,100,1]
print (green)

print (img.shape[0])

width = img.shape[0]
heigth = img.shape[1]
#escalada de cinza
'''for n in range(width):
	for n2 in range(heigth):
		b = int(img[n][n2][0])
		g = int(img[n][n2][1])
		r = int(img[n][n2][2])
		aux = (g+b+r)/3
		img[n][n2] = [aux,aux,aux]

cv2.imshow("Face", img)
cv2.waitKey(0)'''

#outro filtro de cinza
'''for n in range(width):
	for n2 in range(heigth):
		b = int(0.07 * img[n][n2][0])
		g = int(0.72 * img[n][n2][1])
		r = int(0.21 * img[n][n2][2])
		aux = (g+b+r)
		img[n][n2] = [aux,aux,aux]'''

#cv2.imshow("Face", img)
#cv2.waitKey(0)

# filtro threshold -> necessita escala de cinza antes
'''for n in range(width):
	for n2 in range(heigth):
		if(img[n][n2][0] < 100):
			img[n][n2] = 0
		else:
			img[n][n2] = 255
		
cv2.imshow("Face", img)
cv2.waitKey(0)'''

#filtro de bright (brilho) / contraste é multiplicado
'''for n in range(width):
	for n2 in range(heigth):
		b = img[n][n2][0]
		g = img[n][n2][1]
		r = img[n][n2][2]
		
		if(b+30>255):
			b = 255
		else:
			b=b+30
			
		if(g+30>255):
			g = 255
		else:
			g=g+30
		if(r+30>255):
			r = 255
		else:
			r=r+30
		
		
		img[n][n2][0] = b
		img[n][n2][1] = g
		img[n][n2][2] = r
cv2.imshow("Face", img)
cv2.waitKey(0)'''

#filtro de invert 255 - I(i,j)
'''for n in range(width):
	for n2 in range(heigth):
		b = img[n][n2][0]
		g = img[n][n2][1]
		r = img[n][n2][2]
				
		
		img[n][n2][0] = 255 - b
		img[n][n2][1] = 255 - g
		img[n][n2][2] = 255 - r
cv2.imshow("Face", img)
cv2.waitKey(0)'''

#filtro de contrast auto ajustado
'''for n in range(width):
	for n2 in range(heigth):
		
		blue[n][n2] = int(img[n][n2][0])
		g[n][n2] = int(img[n][n2][1])
		r[n][n2] = int(img[n][n2][2])
		
	AhiB = max(blue[n][n2])
	AhiG = max(g[n][n2])
	AhiR = max(r[n][n2])
		
	Alo = min(blue[n][n2],g[n][n2],r[n][n2])
		
	Amax = 255
	Amin = 0
for n in range(width):	
	for n2 in range(heigth):	
		blue[n][n2] = Amin+(blue[n][n2]-Alo)*((Amax-Amin)/(AhiB-Alo))
		g[n][n2] = Amin+(g[n][n2]-Alo)*((Amax-Amin)/(AhiG-Alo))
		r[n][n2] = Amin+(r[n][n2]-Alo)*((Amax-Amin)/(AhiR-Alo))
			
		img[n][n2][0] = 255 - blue[n][n2]
		img[n][n2][1] = 255 - g[n][n2]
		img[n][n2][2] = 255 - r[n][n2]
		
cv2.imshow("Face", img)
cv2.waitKey(0)'''

#tudo vermelho
#for n in range(width):
#	for n2 in range(heigth):
#		img[n][n2] = [0,0,255]
	
#cv2.imshow("Face", img)
#cv2.waitKey(0)



#escala de cinza
'''for n in range(width):
	for n2 in range(heigth):
		b = int(0.07 * img[n][n2][0])
		g = int(0.72 * img[n][n2][1])
		r = int(0.21 * img[n][n2][2])
		aux = (g+b+r)
		img[n][n2] = [aux,aux,aux]
'''
#filtros lineares Convulação *
matriz = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]

div = 0

novaimagem = np.ndarray(img.shape, dtype=np.float)
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
				b += int(img[n+x][n2+y][0]) * matriz[x][y]
				#green
				g += int(img[n+x][n2+y][1]) * matriz[x][y]
				#red
				r += int(img[n+x][n2+y][2]) * matriz[x][y]
				
		#print(r)
		somatorioB = b/div
		somatorioG = g/div
		somatorioR = r/div
		print(somatorioR)
		
		
			
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
		
		novaimagem[n][n2] = (somatorioB, somatorioG, somatorioR)


cv2.imshow("Face", novaimagem)
cv2.waitKey(0)	
		
					
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				