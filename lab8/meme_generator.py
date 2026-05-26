from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:

    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def add_text(self, top_text="", bottom_text=""):

        image = self.image.copy()

        draw = ImageDraw.Draw(image)

        width, height = image.size

        font_size = width // 10

        try:
            font = ImageFont.truetype(
                "impact.ttf",
                font_size
            )

        except:
            try:
                font = ImageFont.truetype(
                    "arialbd.ttf",
                    font_size
                )

            except:
                font = ImageFont.load_default()

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

                if bbox[2] < width - 80:
                    current = test

                else:
                    lines.append(current)
                    current = word

            if current:
                lines.append(current)

            return lines

        def draw_lines(lines, y):

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
                    (x, y),
                    line,
                    fill="white",
                    font=font,
                    stroke_width=8,
                    stroke_fill="black"
                )

                y += line_height

        if top_text:

            draw_lines(
                wrap(top_text),
                30
            )

        if bottom_text:

            lines = wrap(bottom_text)

            draw_lines(
                lines,
                height
                - len(lines)
                * (font_size + 10)
                - 30
            )

        return image