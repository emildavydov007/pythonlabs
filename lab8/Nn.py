if top_text:

            self.draw_centered_text(

                draw,

                top_text,

                font,

                width,
            
                20

            )

        # Нижний текст

        if bottom_text:

            self.draw_centered_text(

                draw,

                bottom_text,

                font,

                width,

                height - 80

            )

        return i

from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:

    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def draw_centered_text(
        self,
        draw,
        text,
        font,
        image_width,
        y
    ):
        """Рисует текст по центру"""

        bbox = draw.textbbox(
            (0, 0),
            text,
            font=font
        )

        text_width = bbox[2] - bbox[0]

        x = (image_width - text_width) // 2

        draw.text(
            (x, y),
            text.upper(),   # Мемный стиль — заглавные
            fill="white",
            font=font,
            stroke_width=3,
            stroke_fill="black"
        )

    def add_text(
        self,
        top_text="",
        bottom_text=""
    ):

        image = self.image.copy()

        draw = ImageDraw.Draw(image)

        width, height = image.size

        try:
            # Размер шрифта зависит от картинки
            font_size = max(width // 15, 30)

            font = ImageFont.truetype(
                "arial.ttf",
                font_size
            )

        except:
            font = ImageFont.load_default()

        # Верхний текст
        if top_text:
            self.draw_centered_text(
                draw,
                top_text,
                font,
                width,
                20
            )

        # Нижний текст
        if bottom_text:
            self.draw_centered_text(
                draw,
                bottom_text,
                font,
                width,
                height - 80
            )

        return image
