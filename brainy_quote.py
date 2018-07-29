################# QUOTE OF THE DAY #############

import bs4, requests 

url = 'https://www.brainyquote.com/quote_of_the_day'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")

quote_categories = []
for category in soup.select('.qotd-h2'):
	quote_categories.append(category.string)

daily_quotes = []
for quotes in soup.select('.oncl_q'):
	daily_quotes.append(quotes.string)

quote_authors = []
for authors in soup.select('.oncl_a'):
	quote_authors.append(authors.string)

def quotes(quote_categories,daily_quotes,quote_authors):
	"""  takes category name, quote and author and prints the sentence."""
	if len(daily_quotes) != len(quote_authors):
		del daily_quotes[0]
		
	print('############',soup.title.string,'#################### \n')
	for category, quote, author in zip(quote_categories,daily_quotes,quote_authors):
		print(category,': \n',quote,'-',author)


quotes(quote_categories,daily_quotes,quote_authors)

#### SINGLE QUOTE 
def single_quote(self,quote_categories,daily_quotes,quote_authors):
    quote_of_day = quote_categories[0]+daily_quotes[0]+quote_authors[0]
    print(quote_of_day)