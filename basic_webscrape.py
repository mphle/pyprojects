import requests
import bs4

res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text,"lxml")


#Unique authors of the first page
authors_html = soup.select(".author")

authors = []
for author_html in authors_html:
    authors.append(author_html.text)
    
authors = list(set(authors)) #removes duplicates

#All quotes on the first page
quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
    
#Top ten tags
tags_list = []

for item in soup.select(".tag-item"):
    tags_list.append(item.select("a")[0].text)
    
tags_list


#Unique authors of the entire set of pages

base_url = "http://quotes.toscrape.com/page/{}/"

keep_scraping = True
current_page_num = 1
authors = []

while keep_scraping:
    current_url = base_url.format(current_page_num)
    current_page_num += 1

    res = requests.get(current_url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    
    if soup.select(".text"):
        print(f"Currently scraping {current_url}")
        
        authors_on_page = soup.select(".author")
        
        for author in authors_on_page:
            authors.append(author.text)
    else:
        keep_scraping = False
        print("Done scraping! No more pages to look at.")
        
unique_authors = list(set(authors))
print("\n")
print(unique_authors)

print("\n")
print(f"There are {len(unique_authors)} unique authors in total on the website.")
