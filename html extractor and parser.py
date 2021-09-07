from urllib.request import Request, urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import urllib.request
import ssl

# stuff for avoiding ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

"""url of website below, I have used deviant art here as an example"""
url = Request('http://deviantart.com')

try:
    response = urlopen(url, context=ctx)

except URLError as e:

    # to give reason/error code, if a URL error occurs
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print("The server couldn't fulfill the request.")
        print('Error code: ', e.code)
else:
    page = urllib.request.urlopen(url, context=ctx)  # open webpage

    # save html of page
    """enter name of file to be created below"""
    file_out = open('filename_here.html', 'w')
    file_out.write(str(page.read()))
    file_out.close()

    # create soup object, with html file for text and set parser
    with open('filename_here.html') as file:
        soup = BeautifulSoup(file, 'html.parser')  # you can use 'lxml' and 3rd party parsers too

    """code to parse stuff will go here,
       check the BeautifulSoup documentation - https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 
       below is an example which will print all links from the html file"""

    for link in soup.find_all('a'):
        current_link = link.get('href')
        print(current_link)
