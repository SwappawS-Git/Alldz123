import requests as r
import bs4 
import csv


def parse_page():
    response = r.get("https://quotes.toscrape.com/tag/life/", timeout=10,
                    headers={
                        'User-Agent': "programist"
                    })

    response.raise_for_status()
    bs = bs4.BeautifulSoup(response.text, "html.parser")
    quotes = bs.find_all("div", class_="quote")
    data = [[
            i.find("small", class_="author").get_text(strip=True),
            "                ",
            i.find("span", class_="text").get_text(strip=True)
            ] 
            for i in quotes]
    return data
        
        
def save(data):
    with open("life.csv", "w", newline="", encoding="utf-8") as Csv:
        CsvFile = csv.writer(Csv)
        CsvFile.writerow(["author", "                    ", "text"])
        for i in data:
            
            CsvFile.writerow(i)


data = parse_page()
save(data)   