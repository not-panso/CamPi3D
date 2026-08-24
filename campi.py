import imageio.v3 as imgio

filenames  = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg']
imgs = []

def create_gif():
    for filename  in filenames:
        imgs.append(imgio.imread(filename))

    imgio.imwrite('3D.gif', imgs, duration = 120, loop = 0)

create_gif()