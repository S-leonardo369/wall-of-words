import requests
from bs4 import BeautifulSoup

def fetch_word_of_the_day():
    """
    Fetches the Word of the Day and its definition from Merriam-Webster's website.
    Returns a dictionary with the word and definition or an error message if unsuccessful.
    """
    url = "https://www.merriam-webster.com/word-of-the-day"
    
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "lxml")
        
        # Extract the word and definition
        word = soup.find("h2", class_="word-header-txt").get_text(strip=True)


        definition_container = soup.find("div", class_="wod-definition-container")
        if not definition_container:
            raise ValueError("Failed to find the definition container.")
        
        # Look for the specific definition text
        definition_paragraph = definition_container.find("p")
        
        return {"word": word, "definition": definition_paragraph.text}
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch the Word of the Day: {e}"}
    except AttributeError:
        return {"error": "Failed to parse the Word of the Day from the page."}


fetch_word_of_the_day()