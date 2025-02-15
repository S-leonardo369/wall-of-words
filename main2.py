import wallpaper_changer
import wallpaper_creator
import requester_web


# it fetches a word from the web site


def main():
        
    word = requester_web.fetch_word_of_the_day()
    image_path = r"C:\Users\syedl\OneDrive\Desktop\python xl\wallpaper images\custom_minimalist_wallpaper1.jpg"

    #it creates a wallpaper which is black in color
    wallpaper_creator.create_minimalist_wallpaper(
        output_path=image_path,
        word=word["word"],
        definition=word["definition"],
        bg_color=(0, 0, 0),  # Dark blue background 10, 20, 50
        text_color=(255, 255, 255),  # White text
        font_path="arial.ttf",  # Path to your .ttf font file
        word_font_size=120,
        definition_font_size=40
    )

    #it change the current wallpaper to the created wallpaper
    wallpaper_changer.change_background(image_path)

if __name__=="__main__":
    main()

