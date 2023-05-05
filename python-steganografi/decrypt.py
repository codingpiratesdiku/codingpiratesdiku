# importing PIL
from PIL import Image


def get_pixels(im, i):
    r1, g1, b1 = im.getpixel((i * 3, 0))
    r2, g2, b2 = im.getpixel((i * 3 + 1, 0))
    r3, g3, b3 = im.getpixel((i * 3 + 2, 0))

    return [r1, g1, b1, r2, g2, b2, r3, g3, b3]


# Read image
im = Image.open("img/kaptajn_encrypted.png").convert("RGB").copy()

combined = ""

end = False
i = 0

while not end:
    rgbs = get_pixels(im, i)

    bits = [rgb % 2 for rgb in rgbs]

    bits_str = "".join(str(bit) for bit in bits)

    combined += chr(int(bits_str[:-1], 2))

    if bits[-1] == 1:
        end = True

    i += 1

print(combined)
