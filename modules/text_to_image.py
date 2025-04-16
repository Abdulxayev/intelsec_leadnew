from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, filename="report.png"):
    width = 800
    height = 1200
    background = (255, 255, 255)
    font_color = (0, 0, 0)

    img = Image.new("RGB", (width, height), color=background)
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    lines = text.split('\n')
    y = 10
    for line in lines:
        d.text((10, y), line, font=font, fill=font_color)
        y += 20

    img.save(filename)
    return filename
