from PIL import Image, ImageDraw, ImageFont

height = 2160*4 # This must remain constant at 2160x4 as that's the lowest resolution that results in even height lines
width = 2160*3  # Change from *3 to *6 for a landscape version

out = Image.new("L",(width, height))
dout = ImageDraw.Draw(out)

fnt = ImageFont.truetype('arial.ttf', int(width/25))

offset = 0
resolutions = [240, 360, 480, 576, 720, 1080, 1440, 2160]

for res in resolutions:
    for i in range(height):
        if int(i/(2160*4/res)) & 1:
            dout.line((offset*width/8, i, (offset+1)*width/8, i), fill=255)
    dout.text((offset*width/8 + width/75, height/2 - width/45), str(res)+'p', font=fnt, fill=255)
    offset += 1

# draw "crosshairs"
dout.line((width/2, height/2 - width/50, width/2, height/2 + width/50), fill=0, width=50)
dout.line((width/2 - width/50, height/2, width/2 + width/50, height/2), fill=0, width=50)
    
#dout.rectangle((0, height+1, width, height+240), fill=1)    

out.show()
out.save("VidCamVertResTest.png", "PNG")







height = 3840*2*3
width = 3840*3*3

out = Image.new("L",(width, height))
dout = ImageDraw.Draw(out)

fnt = ImageFont.truetype('arial.ttf', int(height/20))

offset = 0
resolutions = [426, 640, 720, 1024, 1280, 1920, 2560, 3840]

for res in resolutions:
    for i in range(width):
        if int(i/(3840*4*3/res)) & 1:
            dout.line((i, offset*height/8, i, (offset+1)*height/8), fill=255)
    dout.text((width/2 - width/25, offset*height/8 + height/30), str(res), font=fnt, fill=255)
    offset += 1

# draw "crosshairs"
dout.line((width/2, height/2 - width/50, width/2, height/2 + width/50), fill=0, width=50)
dout.line((width/2 - width/50, height/2, width/2 + width/50, height/2), fill=0, width=50)
    
#dout.rectangle((0, height+1, width, height+240), fill=1)    

out.show()
out.save("VidCamHorizResTest.png", "PNG")
