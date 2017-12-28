from PIL import Image

img1 = Image.open("a.jpg")
img2 = Image.open("a.jpg")

print(img1.size)
print(img1.format)
#img.show()

def cropImage(img1, img2):
    area = (20, 30, 100, 100)
    r1, g1, b1 = img1.split()
    r2, g2, b2 = img2.split()
    #newImg = img1.crop(area)

    print(r2)
    newImg = Image.merge("RGB", (r2, g2, b1))

    newImg.show()

cropImage(img1, img2)