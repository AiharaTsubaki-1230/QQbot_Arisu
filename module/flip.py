from PIL import Image

def img_h(src):
    img1 = Image.open(src)
    w,h = img1.size
    img2 = Image.new("RGB", (w // 2 * 2, h // 2 * 2))

    img3 = img1.crop((0, 0, w // 2, h))
    img4 = img3.transpose(Image.FLIP_LEFT_RIGHT)

    img2.paste(img3, (0,0))
    img2.paste(img4, (w//2, 0))
    img2.save("/Users/a1231/data/images/temp.png")

def img_v(src):
    img1 = Image.open(src)
    w,h = img1.size
    img2 = Image.new("RGB", (w // 2 * 2, h // 2 * 2))

    img3 = img1.crop((0, 0, w, h // 2))
    img4 = img3.transpose(Image.FLIP_TOP_BOTTOM)

    img2.paste(img3, (0,0))
    img2.paste(img4, (0,h//2))
    img2.save("/Users/a1231/data/images/temp.png")

def img_h1(src):
    img1 = Image.open(src)
    w,h = img1.size
    img2 = Image.new("RGB", (w // 2 * 2, h // 2 * 2))

    img4 = img1.crop((w // 2, 0, w // 2 * 2, h))
    img3 = img4.transpose(Image.FLIP_LEFT_RIGHT)

    img2.paste(img3, (0,0))
    img2.paste(img4, (w//2, 0))
    img2.save("/Users/a1231/data/images/temp.png")

def img_v1(src):
    img1 = Image.open(src)
    w,h = img1.size
    img2 = Image.new("RGB", (w // 2 * 2, h // 2 * 2))

    img4 = img1.crop((0, h // 2, w, h // 2 * 2))
    img3 = img4.transpose(Image.FLIP_TOP_BOTTOM)

    img2.paste(img3, (0,0))
    img2.paste(img4, (0,h//2))
    img2.save("/Users/a1231/data/images/temp.png")
