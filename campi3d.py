import imageio.v3 as imgio
from os import listdir, path, makedirs

# Making the required directories
usb_dir = 'CamPi3D'
imgs_dir = f'{usb_dir}/Images' # Directory where the original images where taken
gifs_dir = f'{usb_dir}/GIFs' # Directory where the gif is created from the above images
makedirs(imgs_dir, exist_ok=True)
makedirs(gifs_dir, exist_ok=True)

# Making warnings for each CamPi3D directory
open(f'{imgs_dir}/DO NOT ADD OR MODIFY ANY FILES HERE', 'w').close() # Warning file for images directory
open(f'{gifs_dir}/DO NOT ADD OR MODIFY ANY FILES HERE', 'w').close() # Warning file for gifs directory

with open(f'{usb_dir}/README.txt', 'w') as f:
    f.write("You do not edit the files present in the Images and GIFs folders. You can copy them elsewhere, delete them but don't modify them and preferably don't add anything there although the project does include protection to that and shouldn't affect anything.")

filenames  = [f'{imgs_dir}/1.jpg', f'{imgs_dir}/2.jpg', f'{imgs_dir}/3.jpg', f'{imgs_dir}/4.jpg'] # List of filenames of the pictures taken
imgs = []
files_num = listdir(gifs_dir) # List of every file in the GIFs directory
gif_num = []

for files in files_num: # Indexing the gif files in case there is a non gif file inside of there to avoid accidentally replacing a gif 
    if files.endswith('.gif'):
        gif_num.append(files)

gif_name = len(gif_num) + 1 # Getting the correct name for the next gif by counting the number of entries in gif_num and increasing by 1


def create_gif(): # Creating the gif 
    for filename  in filenames:
        imgs.append(imgio.imread(filename))
    loop_imgs = imgs + imgs[-2:0:-1]
    imgio.imwrite(f'{gifs_dir}/{gif_name}.gif', loop_imgs, duration = 120, loop = 0)

create_gif()
