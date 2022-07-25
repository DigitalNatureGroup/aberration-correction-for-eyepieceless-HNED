import numpy as np
import cv2
N=1080
z = np.full((N,N),254)
print(cv2.imwrite('../output/white{}.png'.format(N), z))