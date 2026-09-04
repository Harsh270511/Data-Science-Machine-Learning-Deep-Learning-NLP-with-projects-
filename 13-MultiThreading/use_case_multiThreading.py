#Real world Example: Multithreading for I/O bound tasj

# Senario: Web Scraping

import threading
import requests
from bs4 import BeautifulSoup

urls=[
  'https://python.langchain.com/v0.2/docs/introduction/'
  'https://python.langchain.com/v0.2/docs/concepts/'
  'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
  response= requests.get(url)
  soup= BeautifulSoup(response.content, 'html.parse')

  print(f"Fetched {len(soup.text)} characters from {url}")

threads=[]

for url in urls:
  thread = threading.Thread(target=fetch_content, args=(url,))
  threads.append(thread)
# Real-world Example: Multithreading for I/O-bound tasks
# Scenario: Web Scraping

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    print(f"Fetched {len(soup.text)} characters from {url}")


threads = []

# Create threads
for url in urls:
    thread = threading.Thread(
        target=fetch_content,
        args=(url,)
    )
    
    threads.append(thread)
    thread.start()       # Start the thread


# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All web pages have been fetched!")