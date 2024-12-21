from PIL import Image


def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))


im = new_photo('Godfather.jpg')
im_2 = new_photo('Design.jpeg')

im.paste(im_2, (150, 300))
im.show('MyPhoto')
