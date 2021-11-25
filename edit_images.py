from PIL import Image
import json

calibrationNumber = 50
titleHeight = 65  # npr Zadaci visestrukog izbora
colors = {
    'Brojevi i algebra': (229, 177, 32)
    # ostale boje
}


def isColorSame(rgbColor1, rgbColor2):
    isSame = rgbColor1[0] > rgbColor2[0]-calibrationNumber and rgbColor1[0] < rgbColor2[0]+calibrationNumber and rgbColor1[1] > rgbColor2[1] - \
        calibrationNumber and rgbColor1[1] < rgbColor2[1]+calibrationNumber and rgbColor1[2] > rgbColor2[2] - \
        calibrationNumber and rgbColor1[2] < rgbColor2[2]+calibrationNumber
    return isSame


def isTitle(yCoordinate, borderColor):
    pixelColor = image.getpixel((width*0.33, yCoordinate+5))

    # if title (Zadatci visestrukog izbora)
    if isColorSame(borderColor, pixelColor):
        return True
    else:
        return False


def findYBorders(image, borderColor, height, width):
    borders = []
    y = 1
    returnedBorders = []
    while y != height-1:
        pixelColor = image.getpixel((width*0.33, y))

        if isColorSame(borderColor, pixelColor):

            # if title (Zadatci visestrukog izbora)
            if isTitle(y, borderColor):

                # check if title is the first border
                if len(borders) != 0:
                    borders.append(y)

                borders.append(y + titleHeight)
                y += titleHeight
            else:
                borders.append(y+3)
                y += 3
        y += 1

    if len(borders) % 2 != 0:
        print('ERROR - neparni broj bordera')
        return

    for i in range(0, len(borders), 2):
        # if gap greater than 100px (if not title)
        if borders[i+1] - borders[i] > 100:
            returnedBorders.append((borders[i], borders[i+1]))

    return returnedBorders


def cutPage(image, frame):
    left, right = frame

    for i in range(len(borders)):
        top, bottom = borders[i]
        cutPage = image.crop((left, top, right, bottom-6))
    return cutPage


def isTextOnBorder(image, y, width):
    for x in range(width-1):
        pixelColor = image.getpixel((x, y))

        if isColorSame((255, 255, 255), pixelColor) == False:
            return True
    return False


def cutZadatci(cutPage, height, width, borderColor):
    zadatciY = []
    returiningZadatciY = []
    zadatci = []
    y = 0

    # get Y of zadatci
    while y < height:
        x = 0
        while x < int(width/15):
            pixelColor = cutPage.getpixel((x, y))
            if isColorSame(borderColor, pixelColor):
                zadatciY.append(y - 20)
                y += 20
                x = 0
            else:
                x += 1
        y += 1

    # structure Y of zadatci
    for i in range(len(zadatciY)):
        zadatakY = zadatciY[i]
        if i == len(zadatciY) - 1:
            nextzadatakY = height-1
        else:
            nextzadatakY = zadatciY[i+1]

        returiningZadatciY.append((zadatakY, nextzadatakY))

    # cut zadatci
    for i in range(len(returiningZadatciY)):
        top, bottom = returiningZadatciY[i]

        # if zadatak is past border
        while True:
            if isTextOnBorder(cutPage, top, width):
                top -= 10
            elif isTextOnBorder(cutPage, bottom, width):
                bottom -= 10
            else:
                break

        cutZadatak = cutPage.crop((0, top, width, bottom))
        zadatci.append(cutZadatak)
    return zadatci


with open('book.json') as f:
    book = json.load(f)


for i in range(1):  # len(book)
    obj = book[i]
    print(obj['zadatci'])

    for page in range(obj['zadatci'][0], obj['zadatci'][1]):

        image = Image.open('knjiga/{}.jpg'.format(page))
        width, height = image.size
        borderColor = colors[obj['cjelina']]

        if (page % 2 == 0):
            frame = [208, 1068]
        else:
            frame = [134, 993]

        borders = findYBorders(image, borderColor, height, width)

        framedPage = cutPage(image, frame)

        zadatci = cutZadatci(
            framedPage, framedPage.size[1], framedPage.size[0], borderColor)
        print(zadatci)
