import imageio.v3 as imgio

filenames  = ['imgs/1.jpg', 'imgs/2.jpg', 'imgs/3.jpg', 'imgs/4.jpg']
imgs = []

def create_gif():
    for filename  in filenames:
        imgs.append(imgio.imread(filename))

    imgio.imwrite('3D.gif', imgs, duration = 120, loop = 0)

create_gif()
