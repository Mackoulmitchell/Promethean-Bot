import requests
from bs4 import BeautifulSoup

class searchClass:
    def __init__(self):
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://en.wikipedia.org/wiki/'
    
    
    def key_words_search_words(self, user_message):
        words = user_message.split()[1:]
        keywords = '_'.join(words)
        search_words = ' '.join(words)
        return keywords, search_words
    
    
    def search(self, keywords):
        response = requests.get(self.url+keywords, headers = self.headers)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        result_links = soup.findAll('a') #Find-All Parameters need to be adjusted
        return result_links
    
    
    def send_link(self, result_links, search_words):
        send_link = set()
        for link in result_links:
            text = link.text.lower() #Makes text lowercase to compare User Search to links.
            if search_words in text:
                send_link.add(link.get('href')) #href is for the link.
        return send_link