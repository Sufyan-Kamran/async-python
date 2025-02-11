import asyncio
import requests 
from datetime import datetime
from bs4 import BeautifulSoup

response = requests.get('https://www.yellowpages.ca/search/si/1/plumber/Toronto+ON')
soup = BeautifulSoup(response.content, 'html.parser')

async def fetchingResponse(n):
    
    url = f'https://www.yellowpages.ca/{n}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    print(soup.select('h1')[0].text)
    lst = [i.text for i in soup.select('.merchant__item.merchant__address.merchant__address__mobile span')]
    print(lst)

async def generatingResponse():
    start_time = datetime.now()
    
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(fetchingResponse(i.get('href'))) for i in soup.select('.jsListingName')]
    
    end_time = datetime.now()
    time_difference = end_time - start_time
    print(f"Time difference: {time_difference}")
    return tasks


asyncio.run(generatingResponse())
