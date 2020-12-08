# import torch
#
# from PIL import Image, ImageDraw, ImageFont, ImageColor
#
#
# def add_num(image, text):
#     # 设置字体（字体样式，字体大小）
#     font = ImageFont.truetype("arial.ttf", 250)
#     # 设置字体颜色
#     fontcolor = ImageColor.colormap.get('red')
#     # ImageDraw模块的函数：Draw(image):创建一个可以在给定图像上绘图的对象
#     draw = ImageDraw.Draw(image)
#     # 获取图片大小
#     width, height = image.size
#     # 将文字加到图片上
#     draw.text((width - 150, 30), text, font=font, fill=fontcolor)
#     # 特别要注意这个文件路径名\\head2.png这里有两个\
#     image.save("C:\\Users\蔡畅\Desktop\流畅的python\\head2.png")
#
#
# if __name__ == '__main__':
#     image = Image.open("C:\\Users\蔡畅\Desktop\流畅的python\\pingjia.png")
#     # 将到图片上的文本内容
#     text = "+"
#     add_num(image, text)
#
# 显示事例图像
# Plotting a sample data:
from matplotlib import pyplot as plt
import numpy as np
r, c = 6, 6
fig, axs = plt.subplots(r, c)

cnt = 0
X_train_resized =
for i in range(r):
    for j in range(c):
        axs[i,j].imshow(X_train_resized[np.random.randint(0,6000)])
        axs[i,j].axis('off')
        cnt += 1
fig.savefig("./TMI_generators_output/tmi_training_random_sample.png")
plt.suptitle('Non-nuclei Training Sample - label = 1')
plt.show()
#
# r, c =6, 6
# fig, axs = plt.subplots(r, c)
# cnt = 0
# for i in range(r):
#     for j in range(c):
#         axs[i,j].imshow(X_train_resized[np.random.randint(6000,8000)])
#         axs[i,j].axis('off')
#         cnt += 1
# fig.savefig("./TMI_generators_output/tmi_training_random_sample.png")
# plt.suptitle('Nuclei Training Sample -label = 2 ')
# plt.show()