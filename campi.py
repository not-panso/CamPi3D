import imageio.v3 as imgio

filenames  = ['imgs/1.jpg', 'imgs/2.jpg', 'imgs/3.jpg', 'imgs/4.jpg']
imgs = []

def create_gif():
    for filename  in filenames:
        imgs.append(imgio.imread(filename))
    loop_imgs = imgs + imgs[-2:0:-1]
    imgio.imwrite('3D.gif', loop_imgs, duration = 120, loop = 0)

create_gif()
