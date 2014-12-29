import urllib.request
from bs4 import BeautifulSoup

'''
Scrapes all links and images from a user provided url 
and prints them out based on user's request.
'''

def print_list(lst):
    print('\n'.join(lst))
    print('\n====================\n')

# protect for import 
if __name__ == '__main__':
    
    url = input('Enter a URL: ')
    
    urlSoup = BeautifulSoup(urllib.request.urlopen("https://" + url).read())

    choice = input('\nWhat to scrape? \n'
        '1. Links \n'
        '2. Images \n'
        '3. Both \n'
        'Choice: ')

    if choice not in ["1","2","3"]:
        print("\nInvalid Scrape Option. \n")
    else:
        print('\n====================\n')

    if ((choice == "1") or (choice == "3")):
        links = [link.get('href') for link in urlSoup.findAll('a')]
        print("URLs:\n-----")
        print_list(links)
    if ((choice == "2") or (choice == "3")):
        images = [image['src'] for image in urlSoup.findAll("img")]
        print ("Images:\n-------")
        print_list(images)
