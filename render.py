from PIL import Image, ImageDraw, ImageFont

color = (0, 0, 0)

# Пустой фон.
im = Image.new('RGB', (1440, 900), "black")
draw = ImageDraw.Draw(im)


headline = ImageFont.truetype("arial.ttf", size=30)
draw.text((40, 20), "Pon", font=headline)

