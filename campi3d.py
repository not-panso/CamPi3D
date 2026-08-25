import imageio.v3 as iio
from os import listdir, path, makedirs, remove

# Finding if there is a usb and using the appropriate directory
mountpoint = '/run/media/panso' # Rememeber to change to /media/campi when done testing in own machine
mounts = listdir(mountpoint) 
if mounts:
    abc_mounts = sorted(mounts)
    usb_dir = f'{mountpoint}/{abc_mounts[0]}/CamPi3D'

    # Creating the folders needed
    imgs_dir = f'{usb_dir}/Images' # Directory where the original images where taken
    gifs_dir = f'{usb_dir}/GIFs' # Directory where the gif is created from the above images
    makedirs(imgs_dir, exist_ok=True)
    print('Images directory created or it already exists')
    makedirs(gifs_dir, exist_ok=True)
    print('GIFs directory created or it already exists')

    # Creating the warning files needed
    if path.isfile(f'{imgs_dir}/DO NOT ADD OR MODIFY ANY FILES HERE'):
        print('Images warning file already exists')
    else: 
        open(f'{imgs_dir}/DO NOT ADD OR MODIFY ANY FILES HERE', 'w').close() # Warning file for images directory
        print('Created Images warning file')
    if path.isfile(f'{gifs_dir}/DO NOT ADD OR MODIFY ANY FILES HERE'):
        print('GIFs warning file already exists')
    else: 
        open(f'{gifs_dir}/DO NOT ADD OR MODIFY ANY FILES HERE', 'w').close() # Warning file for gifs directory
        print('Created GIFs warning file')
    if path.isfile(f'{usb_dir}/README.txt'):
        print('README.txt already exists')
    else: 
        with open(f'{usb_dir}/README.txt', 'w') as f: # Creating the README.txt file
            f.write("This folder is used by CamPi3D, a Raspberry Pi camera project that saves photos and generates GIFs here. Please don't modify, rename, or add files in the Images or GIFs folders, since GIF numbering depends on what's already in the GIFs folder and unexpected files can cause names to overlap or GIFs to overwrite each other. You're welcome to copy or delete the files, just don't edit or add to them directly.")
            print('Created README.txt')

    # Managing the files
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
            imgs.append(iio.imread(filename))
        loop_imgs = imgs + imgs[-2:0:-1]
        print('Generating GIF...')
        iio.imwrite(f'{gifs_dir}/{gif_name}.gif', loop_imgs, duration = 120, loop = 0)
        print('GIF generated!')
        print('Deleting images...')
        for filename in filenames:
            remove(filename)
        print('Images deleted!')

    create_gif()
else:
    print('No USB found. Exiting...')
