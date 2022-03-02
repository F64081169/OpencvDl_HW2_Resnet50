import numpy as np
from torchvision.transforms import *

from PIL import Image
import random
import math
import numpy as np
import torch

def random_erasing_img(p = 0.5, s_l = 0.02, s_h = 0.4 ,r1=0.3 ,mean=[0.4914, 0.4822, 0.4465]):
    '''
    p: probability of erasing img
    s_l: min erasing area
    s_h: max erasing area
    '''
    
    def eraser(img):
    #     r_1 = 0.3
    #     r_2 = 1/0.3
    #     v_l = 0
    #     v_h = 255
    #     pixel_level = False
    #     if input_img.ndim == 3:
    #         img_h, img_w, img_c = input_img.shape
    #     elif input_img.ndim == 2:
    #         img_h, img_w = input_img.shape
    #     p_1 = np.random.rand()
    #     if p_1 > p:
    #         return input_img
    #     while True:
    #         s = np.random.uniform(s_l, s_h) * img_h * img_w
    #         r = np.random.uniform(r_1, r_2)
    #         w = int(np.sqrt(s / r))
    #         h = int(np.sqrt(s * r))
    #         left = np.random.randint(0, img_w)
    #         top = np.random.randint(0, img_h)
    #         if left + w <= img_w and top + h <= img_h:
    #             break
    #     if pixel_level:
    #         if input_img.ndim == 3:
    #             c = np.random.uniform(v_l, v_h, (h, w, img_c))
    #         if input_img.ndim == 2:
    #             c = np.random.uniform(v_l, v_h, (h, w))
    #     else:
    #         c = np.random.uniform(v_l, v_h)
    #     input_img[top:top + h, left:left + w] = c                                
    #     return input_img
    
    # return eraser
        if random.uniform(0, 1) > p:
                return img

        for attempt in range(100):
                area = img.size()[1] * img.size()[2]
        
                target_area = random.uniform(s_l, s_h) * area
                aspect_ratio = random.uniform(r1, 1/r1)

                h = int(round(math.sqrt(target_area * aspect_ratio)))
                w = int(round(math.sqrt(target_area / aspect_ratio)))

                if w < img.size()[2] and h < img.size()[1]:
                    x1 = random.randint(0, img.size()[1] - h)
                    y1 = random.randint(0, img.size()[2] - w)
                    if img.size()[0] == 3:
                        img[0, x1:x1+h, y1:y1+w] = mean[0]
                        img[1, x1:x1+h, y1:y1+w] = mean[1]
                        img[2, x1:x1+h, y1:y1+w] = mean[2]
                    else:
                        img[0, x1:x1+h, y1:y1+w] = mean[0]
                    return img

        return img










# class RandomErasing(object):
#     '''
#     Class that performs Random Erasing in Random Erasing Data Augmentation by Zhong et al. 
#     -------------------------------------------------------------------------------------
#     probability: The probability that the operation will be performed.
#     sl: min erasing area
#     sh: max erasing area
#     r1: min aspect ratio
#     mean: erasing value
#     -------------------------------------------------------------------------------------
#     '''
#     def __init__(self, probability = 0.5, sl = 0.02, sh = 0.4, r1 = 0.3, mean=[0.4914, 0.4822, 0.4465]):
#         self.probability = probability
#         self.mean = mean
#         self.sl = sl
#         self.sh = sh
#         self.r1 = r1
       
#     def __call__(self, img):

#         if random.uniform(0, 1) > self.probability:
#             return img

#         for attempt in range(100):
#             area = img.size()[1] * img.size()[2]
       
#             target_area = random.uniform(self.sl, self.sh) * area
#             aspect_ratio = random.uniform(self.r1, 1/self.r1)

#             h = int(round(math.sqrt(target_area * aspect_ratio)))
#             w = int(round(math.sqrt(target_area / aspect_ratio)))

#             if w < img.size()[2] and h < img.size()[1]:
#                 x1 = random.randint(0, img.size()[1] - h)
#                 y1 = random.randint(0, img.size()[2] - w)
#                 if img.size()[0] == 3:
#                     img[0, x1:x1+h, y1:y1+w] = self.mean[0]
#                     img[1, x1:x1+h, y1:y1+w] = self.mean[1]
#                     img[2, x1:x1+h, y1:y1+w] = self.mean[2]
#                 else:
#                     img[0, x1:x1+h, y1:y1+w] = self.mean[0]
#                 return img

#         return img