from PIL import Image, ImageDraw, ImageFont
import textwrap


def create_minimalist_wallpaper(
    output_path, word, definition, bg_color, text_color, font_path, word_font_size, definition_font_size
):
    # Create a blank image
    img_width, img_height = 1920, 1080  # Standard full HD resolution
    img = Image.new("RGB", (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Load fonts
    word_font = ImageFont.truetype(font_path, word_font_size)
    definition_font = ImageFont.truetype(font_path, definition_font_size)

    # Draw the word (centered horizontally, upper third vertically)
    word_bbox = draw.textbbox((0, 0), word, font=word_font)
    word_width = word_bbox[2] - word_bbox[0]
    word_height = word_bbox[3] - word_bbox[1]
    word_x = (img_width - word_width) // 2
    word_y = img_height // 4
    draw.text((word_x, word_y), word, fill=text_color, font=word_font)

    # Wrap the definition text
    max_text_width = img_width - 200  # Leave padding on both sides

    def wrap_text(text, font, max_width):
        """Wrap text to fit within a specific width."""
        lines = []
        for line in text.split("\n"):
            # Wrap each paragraph independently
            current_line = []
            for word in line.split():
                test_line = " ".join(current_line + [word])
                test_width = draw.textbbox((0, 0), test_line, font=font)[2]
                if test_width <= max_width:
                    current_line.append(word)
                else:
                    lines.append(" ".join(current_line))
                    current_line = [word]
            if current_line:
                lines.append(" ".join(current_line))
        return "\n".join(lines)

    wrapped_definition = wrap_text(definition, definition_font, max_text_width)

    # Dynamically shrink the font if the text doesn't fit vertically
    def fit_font_to_height(text, font, max_width, max_height):
        while True:
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            if text_width <= max_width and text_height <= max_height:
                break
            font = ImageFont.truetype(font_path, font.size - 2)
        return font

    max_definition_height = img_height - word_y - word_height - 50  # Remaining space below the word
    definition_font = fit_font_to_height(
        wrapped_definition, definition_font, max_text_width, max_definition_height
    )

    # Calculate the position for the definition (below the word, centered horizontally)
    text_bbox = draw.textbbox((0, 0), wrapped_definition, font=definition_font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    definition_x = (img_width - text_width) // 2
    definition_y = word_y + word_height + 60

    # Draw the wrapped definition text
    draw.multiline_text(
        (definition_x, definition_y),
        wrapped_definition,
        fill=text_color,
        font=definition_font,
        align="center",
    )

    # Save the image
    img.save(output_path)


# Usage
if __name__=="__main__":
        
    image_path = r"C:\Users\syedl\OneDrive\Desktop\python xl\wallpaper images\custom_minimalist_wallpaper1.jpg"
    create_minimalist_wallpaper(
        image_path,
        word="circuitous",
        definition="If something—such as a path, route, or journey—is described as circuitous, it is not straight, short, and direct, but rather takes a circular or winding course. Circuitous can also describe speech or writing that is not said or done simply or clearly.",
        bg_color=(0, 0, 0),
        text_color=(255, 255, 255),
        font_path="arial.ttf",
        word_font_size=120,
        definition_font_size=40,
    )
