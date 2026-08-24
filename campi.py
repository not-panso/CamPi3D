import imageio.v3 as imgio
from os import listdir

filenames  = ['imgs/1.jpg', 'imgs/2.jpg', 'imgs/3.jpg', 'imgs/4.jpg']
imgs = []
files_num = listdir('GIFs')
gif_num = []

for files in files_num:
    if files.endswith('.gif'):
        gif_num.append(files)

gif_name = len(gif_num) + 1


def create_gif():
    for filename  in filenames:
        imgs.append(imgio.imread(filename))
    loop_imgs = imgs + imgs[-2:0:-1]
    imgio.imwrite(f'GIFs/{gif_name}.gif', loop_imgs, duration = 120, loop = 0)

create_gif()
