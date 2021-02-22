from PIL import Image
import numpy as np
#characters to convert brightness values to
asciiString = "` ^ \" , : ; I l ! i ~ + _ - ? ] [ } { 1 ) ( | \\ / t f j r x n u v c z X Y U J C L Q 0 O Z m w q p d b k h a o * # M W & 8 % B @ $"
ascii = asciiString.split()

#storing as np array
#importing image and converting to greyscale
im = np.array(Image.open("DuckTales_28Main_title29.png").convert('L'))
#adjusting brightness to character amount
im = im/3.93
im = np.round(im, decimals =  0)
imx = im.astype(int)
#creating empty string to push ascii art into
art = ""
#iterating array and adding the related brightness character to the art string
for x in imx[::2]:
  art += "\n"
  for y in x:
    art += ascii[y -1]

#print(art)
#saving the art as a text file
f = open("output.txt", "a")
print(art, file=f)
f.close()