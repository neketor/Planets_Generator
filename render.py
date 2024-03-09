from PIL import Image, ImageDraw, ImageFont

color = (0, 0, 0)

# Пустой фон.
im = Image.new('RGB', (900, 800), "black")
draw = ImageDraw.Draw(im)


headline = ImageFont.truetype("arial.ttf", size=30)
planet_info = ImageFont.truetype("arial.ttf", size=25)
# draw.text((40, 20), "Pon", font=headline) Example

