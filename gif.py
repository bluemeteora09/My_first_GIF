import imageio.v3 as iio


filenames = ['Catpic1.png', 'Catpic2.png']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('mycat.gif', images, duration = 500, loop = 0)