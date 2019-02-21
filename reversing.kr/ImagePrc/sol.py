from PIL import Image
import numpy as np


with open("fuck.bin") as x:
	x1=x.read()
	res=Image.frombuffer('RGB',(200,150)
					,x1,'raw','RGB')
	res=res.transpose(Image.TRANSPOSE)
	res=res.transpose(Image.ROTATE_90)
	res.save('flag.png')
	res.show()