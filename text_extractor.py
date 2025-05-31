import requests
from bs4 import BeautifulSoup

def scrape_webpage():
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.select("div.mw-parser-output > p")
        text = "\n\n".join([p.get_text() for p in paragraphs])
        with open("Selected_Document.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Document saved successfully.")
        return text
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return ""
    
if __name__ == "__main__":
    scrape_webpage()