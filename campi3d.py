import imageio.v3 as imgio
from os import listdir, path, makedirs

imgs_dir = 'CamPi3D/Images'
gifs_dir = 'CamPi3D/GIFs'
filenames  = [f'{imgs_dir}/1.jpg', f'{imgs_dir}/2.jpg', f'{imgs_dir}/3.jpg', f'{imgs_dir}/4.jpg']
imgs = []
files_num = listdir(gifs_dir)
gif_num = []

for files in files_num:
    if files.endswith('.gif'):
        gif_num.append(files)

gif_name = len(gif_num) + 1

if not path.exists('CamPi3D'):
    makedirs('CamPi3D')
if not path.exists(imgs_dir):
    makedirs(imgs_dir)
if not path.exists(gifs_dir):
    makedirs(gifs_dir)

def create_gif():
    for filename  in filenames:
        imgs.append(imgio.imread(filename))
    loop_imgs = imgs + imgs[-2:0:-1]
    imgio.imwrite(f'{gifs_dir}/{gif_name}.gif', loop_imgs, duration = 120, loop = 0)

create_gif()
