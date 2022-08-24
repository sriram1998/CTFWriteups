from PIL import Image

im = Image.open('chall.png')
pix = im.load()
print(im.size)

length = im.size[0]
height = im.size[1]


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
gray = (128, 128, 128)

# init dict
# keys are tuples of tuples of the six colors, values are the decoded values
hexahue = {}
hexahue[(magenta, red, lime, yellow, blue, cyan)] = 'a'
hexahue[(red, magenta, lime, yellow, blue, cyan)] = 'b'
hexahue[(red, lime, magenta, yellow, blue, cyan)] = 'c'
hexahue[(red, lime, yellow, magenta, blue, cyan)] = 'd'
hexahue[(red, lime, yellow, blue, magenta, cyan)] = 'e'
hexahue[(red, lime, yellow, blue, cyan, magenta)] = 'f'
hexahue[(lime, red, yellow, blue, cyan, magenta)] = 'g'
hexahue[(lime, yellow, red, blue, cyan, magenta)] = 'h'
hexahue[(lime, yellow, blue, red, cyan, magenta)] = 'i'
hexahue[(lime, yellow, blue, cyan, red, magenta)] = 'j'
hexahue[(lime, yellow, blue, cyan, magenta, red)] = 'k'
hexahue[(yellow, lime, blue, cyan, magenta, red)] = 'l'
hexahue[(yellow, blue, lime, cyan, magenta, red)] = 'm'
hexahue[(yellow, blue, cyan, lime, magenta, red)] = 'n'
hexahue[(yellow, blue, cyan, magenta, lime, red)] = 'o'
hexahue[(yellow, blue, cyan, magenta, red, lime)] = 'p'
hexahue[(blue, yellow, cyan, magenta, red, lime)] = 'q'
hexahue[(blue, cyan, yellow, magenta, red, lime)] = 'r'
hexahue[(blue, cyan, magenta, yellow, red, lime)] = 's'
hexahue[(blue, cyan, magenta, red, yellow, lime)] = 't'
hexahue[(blue, cyan, magenta, red, lime, yellow)] = 'u'
hexahue[(cyan, blue, magenta, red, lime, yellow)] = 'v'
hexahue[(cyan, magenta, blue, red, lime, yellow)] = 'w'
hexahue[(cyan, magenta, red, blue, lime, yellow)] = 'x'
hexahue[(cyan, magenta, red, lime, blue, yellow)] = 'y'
hexahue[(cyan, magenta, red, lime, yellow, blue)] = 'z'
hexahue[(black, white, white, black, black, white)] = '.'
hexahue[(white, black, black, white, white, black)] = ','
hexahue[(white, white, white, white, white, white)] = ' '
hexahue[(black, black, black, black, black, black)] = ' '
hexahue[(black, gray, white, black, gray, white)] = '0'
hexahue[(gray, black, white, black, gray, white)] = '1'
hexahue[(gray, white, black, black, gray, white)] = '2'
hexahue[(gray, white, black, gray, black, white)] = '3'
hexahue[(gray, white, black, gray, white, black)] = '4'
hexahue[(white, gray, black, gray, white, black)] = '5'
hexahue[(white, black, gray, gray, white, black)] = '6'
hexahue[(white, black, gray, white, gray, black)] = '7'
hexahue[(white, black, gray, white, black, gray)] = '8'
hexahue[(black, white, gray, white, black, gray)] = '9'

color_list = [red, lime, blue, yellow, cyan, magenta]

first_row = []
second_row = []
third_row = []

prev_color = white

row_count = 0


for i in range(height):
    row_count += 1
    for j in range(length):
        if pix[j, i] not in color_list:
            prev_color = white
            if row_count == 11:
                    first_row.append(white)
            elif row_count == 21:
                    second_row.append(white)
            elif row_count == 31:
                    third_row.append(white)

        else:
            if pix[j, i] != prev_color:
                if row_count == 11:
                    first_row.append(pix[j, i])
                elif row_count == 21:
                    second_row.append(pix[j, i])
                elif row_count == 31:
                    third_row.append(pix[j, i])
                prev_color = pix[j, i]

sentence = ""
print(len(first_row), len(second_row), len(third_row))

i = 0

while i < len(first_row):
    if first_row[i] == white:
        sentence += " "
        i += 1
    else:
        sentence += hexahue[(first_row[i], first_row[i+1], second_row[i], second_row[i+1], third_row[i], third_row[i+1])]
        i += 2

print(sentence)
