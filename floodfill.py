import numpy as np
from skimage import data
from skimage import novice
from skimage.novice import Picture
from skimage import data_dir

matrizinteiro = np.zeros(shape=(width, heigth, 3), dtype=np.uint8)


img = novice.open('flower.jpg')

px = img[10,50]
print (px)

width = img.width
heigth = img.height
for n in range(width):
	for n2 in range(heigth):
		matrizinteiro[n, n2] = (0,0,0)
		
def compara(x, y)
	if(x==y){
		return true
	}else{
		return false
	}

for n in range(width):
	for n2 in range(heigth):
		atual[n, n2] = img[n,n2]
		testa = compara(atual[n,n2] == img[n,n2+1])
		if(testa ==false){
			matrizinteiro[n, n2] = atual[n,n2]
		}
		
		testa = compara(atual[n,n2] == img[n,n2-1])
		if(testa ==false){
			matrizinteiro[n, n2] = atual[n,n2]
		}
		
		testa = compara(atual[n,n2] == img[n+1,n2])
		if(testa ==false){
			matrizinteiro[n, n2] = atual[n,n2]
		}
		testa = compara(atual[n,n2] == img[n-1,n2])
		if(testa ==false){
			matrizinteiro[n, n2] = atual[n,n2]
		}
		
		

matrizinteiro = Picture(array=novaimagem)
matrizinteiro.show() 
