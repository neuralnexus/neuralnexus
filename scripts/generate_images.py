# scripts/generate_images.py
from PIL import Image, ImageOps

img = Image.open('profile.png').convert('RGB')
img.save('profile_light.png')

inverted = ImageOps.invert(img)
inverted.save('profile_dark.png')

