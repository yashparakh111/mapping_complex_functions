import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import math

density = 1/250 # 1 unit per 800 pixels
density2 = 1/250 # 1 unit per 200 pixels
image_dir = "C:/Users/yashp/Documents/Python/mapping_complex_functions/testCases/color_wheel.png"

image = cv2.imread(image_dir)
image_x_res = image.shape[1]
image_y_res = image.shape[0]

# transformed_image = np.zeros((image_y_res, image_x_res, 3))
transformed_image = np.empty((image_y_res, image_x_res, 3))
transformed_image[:] = float('nan')
# transformed_image = np.array([255 for i in range(image_x_res * image_y_res * image.shape[2])]).reshape(image_y_res, image_x_res, image.shape[2])

# print(transformed_image[0][0])
# print(transformed_image.shape)

for x in range(int(image_x_res)):
    for y in range(int(int(image_y_res/2))):
        # # change (0, 0, 0, 0) to (1, 1, 1, 1)
        # make_change = True
        # for i in image[y][x]:
        #     if i != 0:                            no longer needed because cv2 
        #         make_change = False               ignores the 4th channel
        # if make_change:
        #     image[y][x] = [1., 1., 1., 1.]
        
        # x, y represent the pixel location
        # z represents the complex number location of x, y
        x_real = density * (x - (image_x_res / 2))
        y_imag = density * ((image_y_res / 2) - y)
        z = complex(x_real, y_imag)
        
        # transformed_z is z put through the function
        # transformed_x, transformed_y represent the pixel location of transformed_z
        transformed_z = pow(z, 2)
        transformed_x = transformed_z.real / density2 + image_x_res / 2
        if transformed_x - math.floor(transformed_x) > 0.85:
            transformed_x = int(round(transformed_x))
        else:
            transformed_x = int(math.floor(transformed_x))
            
        transformed_y = -transformed_z.imag / density2 + image_y_res / 2
        if transformed_y - math.floor(transformed_y) > 0.6:
            transformed_y = int(round(transformed_y))
        else:
            transformed_y = int(math.floor(transformed_y))
            
        
        # print(x, y, ":", transformed_x, transformed_y, ":", x_real, y_imag)
        
        if 0 <= transformed_x < image_x_res - 1 and 0 <= transformed_y < image_y_res - 1:
            # print(x, y, ":", transformed_x, transformed_y)
            transformed_image[transformed_y, transformed_x] = image[y][x]
            # if math.isnan(transformed_image[transformed_y, transformed_x, 3]):
            #     transformed_image[transformed_y, transformed_x, 3] = 1
            # transformed_image[transformed_y, transformed_x][3] = 0.5
            # if transformed_x == 347 and transformed_y == 238:
            #     print(transformed_z.real / density2 + image_x_res / 2, -transformed_z.imag / density2 + image_y_res / 2)
            #     print(transformed_x, transformed_y, ":", transformed_image[transformed_y, transformed_x])
            #     print(x, y, ":", image[y][x], "\n")
            # transformed_image[transformed_y + 1, transformed_x] = image[y][x]
            # transformed_image[transformed_y, transformed_x + 1] = image[y][x]
            # transformed_image[transformed_y + 1, transformed_x + 1] = image[y][x]

# inpaint to fill the missing gaps
transformed_image_mask = np.zeros((image_x_res, image_y_res), dtype = 'uint8')
# for r in range(transformed_image.shape[0]):
#     for c in range(transformed_image.shape[1]):
#         if np.isnan(transformed_image[r,c,0]):
#             transformed_image_mask[r, c] = 1
#         else:
#             transformed_image_mask[r, c] = 0
transformed_image_mask[np.isnan(transformed_image[:,:,0])] = 1
transformed_image_final = transformed_image.astype('uint8')
transformed_image_final = cv2.inpaint(transformed_image_final, transformed_image_mask, 3, cv2.INPAINT_NS)

# plot images
plt.figure(figsize = (13, 7))
plt.subplot(121)
plt.imshow(image)
#plt.subplot(222)
#plt.imshow(transformed_image)
#plt.subplot(223)
#plt.imshow(transformed_image_mask)
plt.subplot(122)
plt.imshow(transformed_image_final)
plt.show()
# plt.savefig('z_sqr_func' + str(i) + '.svg', dpi = 750, format = 'svg')


# for i in range(11):
    # mapImage(1+(i/10))
    # mapImage(i/10 + 1)

# 
# 
# #image array
# 
# 
# shift_x = image_x_dim/2
# shift_y = image_y_dim/2
# 
# for x in range(image_x_dim):
#     for y in range(image_y_dim):
#         z = complex(x - shift_x, y - shift_y)
#         
#         transformed_z = transform(z)
#         transformed_z = complex(transformed_z.real + shift_x,
#                             transformed_z.imag + shift_y)
#         if(0 <= transformed_z.real <= image_x_dim and 0 <= transformed_z.imag <= image_y_dim):
#             #print(transformed_z.real, transformed_z.imag)
#             transformed_image[int(transformed_z.imag)][int(transformed_z.real)] = image[x][y]
# 
# #plot image
# imgplot = plt.imshow(transformed_image)
# plt.show()