def process_image(image):
    new_data = []
    data = image.getdata()
    background_color = data[0]

    for pixel in data:
        if pixel == background_color:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append((*pixel[:3], 255))
    image.putdata(new_data)



def _set_alpha_for_image_background(pixmap):
    image = pixmap.toImage()

    background_color = QColor(image.pixel(0, 0))
    # print(image)
    # print(color)
    # color.setAlpha(1.0)
    # print(color)

    for x in range(image.width()):
        for y in range(image.height()):
            pixel_color = QColor(image.pixel(x ,y))
            r, g, b, a = QColor(image.pixel(x ,y)).getRgb()
            if pixel_color == background_color:
                # alpha.setPixel(x, y, 0.0)
                # pixel_color.setAlpha(0.0)
                print(pixel_color)
                # # print(type(QColor(*pixel_color)))
                # # image.setPixel(x, y, QColor((pixel_color[0], pixel_color[1], pixel_color[2], 1.0)).rgb())
                # image.setPixel(x, y, QColor(r, g, b, 0.0).rgb())
                # image.pixel(x, y).setAlpha(1.0)

                pixel_color.setAlpha(0.0)

                image.setPixel(x, y, pixel_color.rgba())

    print(image)

    return QPixmap(image)



    # image = Image.open('img/b111.png')

    # new_data = []
    # data = image.getdata()

    # print(data[0])
    # for pixel in data:
    #     if pixel[3] < 200:
    #         new_data.append((255, 255, 255))
    #     else:
    #         new_data.append((0, 0, 0))
    # image.putdata(new_data)
    # image.convert('RGB')
    # image.save('img/bb11.png')

    # background_color = data[0]

    # for pixel in data:
    #     if pixel == background_color:
    #         new_data.append((0, 0, 0, 1))
    #     else:
    #         new_data.append((*pixel, 1))
    # image.putdata(new_data)
    # img.save('img/p1.png')

    # filename = 'img/b6a.png'
    # image = Image.open(filename)
    # process_image(image)
    # image.save(filename)
