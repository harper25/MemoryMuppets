from PIL import Image


def add_transparent_background(image):
    new_data = []
    data = image.getdata()
    background_color = data[0]

    for pixel in data:
        if pixel == background_color:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append((*pixel[:3], 255))
    image.putdata(new_data)


filename = '.'
image = Image.open(filename)
add_transparent_background(image)
image.save(filename)
