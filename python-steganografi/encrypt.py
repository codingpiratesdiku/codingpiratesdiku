from PIL import Image


def modify_pixel(im, index, value):
    im.putpixel(index, value)


def get_pixels(im, i):
    r1, g1, b1 = im.getpixel((i * 3, 0))
    r2, g2, b2 = im.getpixel((i * 3 + 1, 0))
    r3, g3, b3 = im.getpixel((i * 3 + 2, 0))

    return [r1, g1, b1, r2, g2, b2, r3, g3, b3]


def put_pixels(im, i, values):
    im.putpixel((i * 3, 0), tuple(values[0:3]))
    im.putpixel((i * 3 + 1, 0), tuple(values[3:6]))
    im.putpixel((i * 3 + 2, 0), tuple(values[6:9]))


def value_to_even(value):
    if value % 2 == 1:
        return value - 1
    return value


def value_to_odd(value):
    if value % 2 == 0:
        return value + 1
    return value


im_orig = Image.open("img/kaptajn.png", "r").convert("RGB")
im = im_orig.copy()

word_to_encrypt = "Hemmelig besked her!"

for i, char in enumerate(word_to_encrypt):
    char_ascii = ord(char)
    char_bits = format(char_ascii, "08b")

    rgbs = get_pixels(im, i)

    for j, bit in enumerate(char_bits):
        if bit == "0":
            rgbs[j] = value_to_even(rgbs[j])
        elif bit == "1":
            rgbs[j] = value_to_odd(rgbs[j])

    if i == len(word_to_encrypt) - 1:
        rgbs[-1] = value_to_odd(rgbs[-1])
    else:
        rgbs[-1] = value_to_even(rgbs[-1])

    put_pixels(im, i, rgbs)

im.save("img/kaptajn_encrypted.png")