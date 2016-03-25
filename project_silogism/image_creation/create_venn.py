from PIL import ImageColor,Image,ImageDraw,ImageFilter
im=Image.new('RGBA',(2000,2000),'white')

smallCircle=[0,400,400]
largeCircle=[1,800,800]
smallEllipse=[0,600,300]
largeEllipse=[1,800,400]


def intersecting_circles(circle1,circle2):
	x, y =  im.size
	eX1, eY1 = circle1[1],circle1[2]
	r1=circle1[0]
	eX2, eY2 = circle2[1],circle2[2]
	r2=circle2[0]
	bbox1 =  (x/2 - eX1/2-50, y/2 - eY1/2, x/2 + eX1/2-50, y/2 + eY1/2)
	bbox2 =  (x/2 - eX2/2+50, y/2 - eY2/2, x/2 + eX2/2+50, y/2 + eY2/2)
	draw = ImageDraw.Draw(im)
	draw.ellipse(bbox1,outline='black',width=3 )
	draw.ellipse(bbox2,outline='black' ,width=3)
	#im1=im.filter(ImageFilter.SHARPEN)	
	im.save("output.png")

circle1=smallEllipse
circle2=largeEllipse

intersecting_circles(circle1,circle2)




