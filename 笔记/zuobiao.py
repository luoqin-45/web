import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


img = Image.open('map.jpg')  # 读取图片
plt.imshow(img)
# plt.xticks([]), plt.yticks([])  # 隐藏x轴和y轴的函数值
plt.show()