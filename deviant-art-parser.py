from urllib.request import Request, urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import urllib.request
import colorama
import ssl

# stuff for avoiding ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = Request('http://www.deviantart.com/')

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
    ext = '.' + input('format? ')  # file extension
    filename = input('filename? ')  # filename

    # save html of page
    file_out = open(filename + ext, 'w')
    file_out.write(str(page.read()))
    file_out.close()

    count = 0  # for image link count

    # create soup object, with html file for text and set parser
    with open(filename + ext) as file:
        soup = BeautifulSoup(file, 'html.parser')

    print('\nImages - ')

    for img in soup.find_all('img'):  # find all with img tag

        src = img.get('src')  # create object src that stores source/link(src) of image

        # check if image uploaded by user
        # all 'https://images' links are uploaded by user
        if 'https://images' in src:

            count += 1  # keep up count with number of links
            print(colorama.Fore.WHITE + f' image {count}  - \n {src}')
