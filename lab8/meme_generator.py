from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:
    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def add_text(self, top_text="", bottom_text=""):
        image = self.image.copy()

        draw = ImageDraw.Draw(image)

        width, height = image.size

        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()

        # Верхний текст
        if top_text:
            bbox = draw.textbbox((0, 0), top_text, font=font)
            text_width = bbox[2] - bbox[0]

            x = (width - text_width) / 2
            y = 20

            draw.text(
                (x, y),
                top_text,
                font=font,
                fill="white",
                stroke_width=2,
                stroke_fill="black"
            )

        # Нижний текст
        if bottom_text:
            bbox = draw.textbbox((0, 0), bottom_text, font=font)
            text_width = bbox[2] - bbox[0]

            x = (width - text_width) / 2
            y = height - 70

            draw.text(
                (x, y),
                bottom_text,
                font=font,
                fill="white",
                stroke_width=2,
                stroke_fill="black"
            )

        return image