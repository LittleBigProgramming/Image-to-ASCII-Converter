import sys, random, argparse
import numpy
import math

from PIL import Image

# gray scale level values from: 
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10 levels of gray
gscale2 = '@%#*+=-:. '

def getAverageL(image):
    # Given PIL Image, return average value of grayscale value
    im = numpy.array(image)
    w, h = im.shape

    return numpy.average(im.reshape(w * h))

def covertImageToAscii(fileName, cols, scale, moreLevels):
    # Given Image and dims (rows, cols) returns an m*n list of Images 
    global gscale1, gscale2

    # open image and convert to grayscale
    image = Image.open(fileName).convert('L')

    W, H = image.size[0], image.size[1]
    print("Input image dimenstions: %d x %d" % (W, H))
    w = W / cols
    # compute tile height based on aspect ratio and scale
    h = w / scale
    # compute number of rows
    rows = int(H / h)
    
    print("Columns: %d, Rows: %d" % (cols, rows))
    print("Tile dimensions: %d x %d" % (w, h))

    # Check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified number of columns!")
        exit(0)

    # Ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        # correct last tile
        if j == rows - 1:
            y2 = H
        # append an empty string
        aimg.append("")
        for i in range(cols):
            # crop image to tile
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            # Correct last tile
            if i == cols - 1:
                x2 = W
            # Crop image to extract tile
            img = image.crop((x1, y1, x2, y2))
            # get average luminance
            avg = int(getAverageL(img))
            # Look up ascii char
            if moreLevels:
                gsval = gscale1[int((avg * 69) / 255)]
            else:
                gsval = gscale2[int((avg * 9) /255)]
            # Append ascii char to string
            aimg[j] += gsval
    
    return aimg

def main():

    descStr = "This CLI application converts an image into ASCII art."
    parser = argparse.ArgumentParser(description = descStr)

    parser.add_argument('--file', dest = 'imgFile', required = True)
    parser.add_argument('--scale', dest = 'scale', required = False)
    parser.add_argument('--out', dest = 'outFile', required = False)
    parser.add_argument('--cols', dest = 'cols', required = False)
    parser.add_argument('--morelevels', dest = 'moreLevels', action = 'store_true')

    args = parser.parse_args()
  
    imgFile = args.imgFile
    outFile = 'ascii-image.txt'
    if args.outFile:
        outFile = args.outFile
    # set scale default as 0.43 which suits a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    cols = 80
    if args.cols:
        cols = int(args.cols)

    print('generating your ASCII art... Please wait :)')
    aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels)

    f = open(outFile, 'w')
    for row in aimg:
        f.write(row + '\n')
    f.close()
    print("The ASCII image has been created in %s" % outFile + ", enjoy :)")

if __name__ == '__main__':
    main()
