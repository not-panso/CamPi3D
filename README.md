# CamPi
A DIY 3D camera project for the Raspberry Pi which uses 4 camera modules to snap 4 different images (**almost**) simultaniously and stich them into a `.gif` file.

# Requirements
- Raspberry Pi 3B (Haven't been tested with other models because I don't own any other models)
- MicroSD (a 16Gb should do just fine)
- USB **of any size** (the amount of images you take is dependant on the size of the USB)
- Camera modules (most likely the IMX219 but it is still WIP)
- Camera Hat (problably [this one](https://www.arducam.com/arducam-8mp-4-quadrascopic-camera-bundle-kit-b0396.html) but WIP)
- Flash
- Button
- 3D Printed enclosure 

---

# Current roadmap for the project 
This is everything I need to get assesed before I can actually start making this project
- [ ] Hardware
  - [x] Raspberry Pi 3B
  - [x] MicroSD
  - [x] USB
  - [ ] Camera modules
  - [ ] Camera Hat
  - [ ] Flash
  - [ ] Button
- [ ] Code (WIP)
- [ ] Enclosure

## Everything that has been implemented in the code yet
- [ ] Taking pictures
- [x] Making the `.gif` from the 4 images
- [x] Creating necessary folders to save the gifs and the images alongside with the needed warnings
- [ ] Make a custom `.img` file for easy installation of the project on a MicroSD

---

# Power problem
The only problem with it is that when I make it, it will be powered by a powerbank because I don't have the budget for a Raspberry Pi battery. That is the only part I won't be documenting and you will be on your own on choosing the correct battery and adding it to the project while also adapting the 3D model enclosure files accordingly.
