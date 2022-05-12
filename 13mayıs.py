# -*- coding: utf-8 -*-
"""
Created on Thu May 12 23:39:35 2022

@author: Zeynep
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("ben.jpg")[...,::-1]/255.0
noise =  np.random.normal(loc=0, scale=1, size=img.shape)

# noise overlaid over image
noisy = np.clip((img + noise*0.01),0,1)
noisy2 = np.clip((img + noise*0.1),0,1)
noisy3 = np.clip((img + noise*0.3),0,1)


cv2.imshow("orijinal",img)
cv2.imshow("%1",noisy)
cv2.imshow("%10",noisy2)
cv2.imshow("%30",noisy3)
cv2.waitKey()


image = cv2.imread("ben.jpg")[...,::-1]/255.0
mean_image = np.mean(image)


def snr (image1,noisy_image):
    noise = noisy_image - image
    mean_noise = np.mean(noise)
    noise_diff = noise - mean_noise
    var_noise = np.sum(np.mean(noise_diff**2)) ## variance of noise
    
    if var_noise == 0:
          snr = 100 ## clean image
          print(snr)
    else:
          snr = (np.log10(mean_image/var_noise))*20 ## SNR of the image
          print(snr)
      
snr(image, noisy)