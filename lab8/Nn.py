if top_text:from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:

    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def add_text(self, top_text="", bottom_text=""):

        image = self.image.copy()

        draw = ImageDraw.Draw(image)

        width, height = image.size

        try:
            # Нормальный размер шрифта
            font_size = width // 10

            font = ImageFont.truetype(
                "arial.ttf",
                font_size
            )

        except:
            font = ImageFont.load_default()

        # Функция переноса строк
        def wrap(text):

            words = text.upper().split()

            lines = []

            current = ""

            for word in words:

                test = (
                    current + " " + word
                    if current
                    else word
                )

                bbox = draw.textbbox(
                    (0, 0),
                    test,
                    font=font
                )

                text_width = bbox[2]

                # Ограничение по ширине
                if text_width < width - 80:
                    current = test

                else:
                    lines.append(current)
                    current = word

            if current:
                lines.append(current)

            return lines

        # Рисование текста
        def draw_lines(lines, start_y):

            line_height = font_size + 10

            for line in lines:

                bbox = draw.textbbox(
                    (0, 0),
                    line,
                    font=font
                )

                text_width = bbox[2]

                x = (
                    width - text_width
                ) // 2

                draw.text(
                    (x, start_y),
                    line,
                    font=font,
                    fill="white",
                    stroke_width=5,
                    stroke_fill="black"
                )

                start_y += line_height

        # Верхний текст
        if top_text:

            lines = wrap(top_text)

            draw_lines(
                lines,
                30
            )

        # Нижний текст
        if bottom_text:

            lines = wrap(bottom_text)

            start_y = (
                height
                - len(lines)
                * (font_size + 10)
                - 30
            )

            draw_lines(
                lines,
                start_y
            )

        return image

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

def add_text(self, top_text="", bottom_text=""):

    image = self.image.copy()

    draw = ImageDraw.Draw(image)

    width, height = image.size

    try:
        # Увеличенный размер шрифта
        font_size = width // 8

        font = ImageFont.truetype(
            "arial.ttf",
            font_size
        )

    except:
        font = ImageFont.load_default()

    # Верхний текст
    if top_text:

        bbox = draw.textbbox(
            (0, 0),
            top_text,
            font=font
        )

        text_width = bbox[2] - bbox[0]

        x = (width - text_width) // 2

        draw.text(
            (x, 30),
            top_text.upper(),
            fill="white",
            font=font,
            stroke_width=5,
            stroke_fill="black"
        )

    # Нижний текст
    if bottom_text:

        bbox = draw.textbbox(
            (0, 0),
            bottom_text,
            font=font
        )

        text_width = bbox[2] - bbox[0]

        x = (width - text_width) // 2

        draw.text(
            (x, height - font_size - 40),
            bottom_text.upper(),
            fill="white",
            font=font,
            stroke_width=5,
            stroke_fill="black"
        )

    return    if top:
            draw.text(((w - len(top)*20)//2, 20), top, fill="white", font=font)
        if bottom:
            draw.text(((w - len(bottom)*20)//2, h-60), bottom, fill="white", font=font)
        
        s

