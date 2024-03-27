from PIL import Image

#7ell taswira
taswira = Image.open(r"C:\Users\ahmed\Desktop\example.png")

pix = taswira.load()

width, height = taswira.size
pixels = []

for y in range(height):
    for x in range(width):
        r, g, b = pix[x, y]
        brightness = int(0.299 * r + 0.587 * g + 0.114 * b)

        if brightness > 200:
            pixels.append("#")
        elif brightness > 150:
            pixels.append("1")
        elif brightness > 100:
            pixels.append("+")
        elif brightness > 50:
            pixels.append("-")
        else:
            pixels.append(" ")
    pixels.append("\n")

with open(r"C:\Users\ahmed\Desktop\ascii_image.txt", "w") as f:
    f.writelines(pixels)

