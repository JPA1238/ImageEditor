from PIL import Image, ImageDraw, ImageFont

print('imager loaded')


def getBlankWhiteImage():
    img = Image.new('RGB', (600, 600), (255, 255, 255))
    return img


getBlankWhiteImage().save('images/blankWhite.png', 'png')


def getBlankBlackImage():
    img = Image.new('RGB', (600, 600), (50, 50, 50))
    return img


getBlankBlackImage().save('images/blankBlack.png', 'png')


def loadImage(link, name):
    img = Image.open(link)
    img.convert('RGB')
    img.thumbnail((600, 600), Image.LANCZOS)
    img.save('images/' + name + '.png', 'png')
    del img


def getTextImage(width: int, height: int, text: str, fontSize: int):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    textImg = ImageDraw.Draw(img)
    if fontSize == 0:
        fontSize = int(height/2)
    font = ImageFont.truetype(
        '/usr/share/fonts/hack-nerd/Hack Regular Nerd Font Complete Mono.ttf', fontSize)
    _, _, w, h = textImg.textbbox((0,0), text, font=font)
    h += int(h*0.21)
    textImg.text(((width-w)/2, (height-h)/2), text=text,
                 fill=(0, 0, 0), font=font)
    img.save('images/textImage.png', 'png')
    del img

def cropImage (l, r, t, b):
    img = Image.open('images/resized.png')
    img = img.crop((l, t, r, b))
    img.save('images/cropped.png', 'png')
    del img

def mergeImage() :
    img = Image.open('images/cropped.png')
    text = Image.open('images/textImage.png')
    combined = Image.new('RGB', (img.size[0], img.size[1] + text.size[1]))
    combined.paste(img, (0, 0))
    combined.paste(text, (0, img.size[1]))
    combined.save('images/edited.png', 'png')
    del img, text, combined

def resizeImage(link):
    img = Image.open(link)
    img = img.resize((1920, int( (1920 / img.size[0]) * img.size[1] )))
    img.save('images/resized.png', 'png')

def edit(link, text, l, r, t, b, fontSize):
    resizeImage(link)
    img = Image.open('images/resized.png')
    w, h = img.size
    cropImage(l, w-r, t, h-b)
    img = Image.open('images/cropped.png')
    w, h = img.size
    getTextImage(w, int(h/10), text, fontSize)
    mergeImage()
    del img

def saveImage(folder, name):
    img = Image.open('images/edited.png')
    img.save(folder + '/' + name + '.png', 'png')
