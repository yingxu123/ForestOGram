import urllib
import shutil
import re
from pathlib import Path
from bs4 import BeautifulSoup

# target page containing links to the image files
target_page = 'https://media.ebird.org/catalog?taxonCode=pinpig2&mediaType=audio&sort=rating_rank_desc'

# local path
dest_path = '.'

# NOTE: this implementation (easily modified) assumes link hrefs contain absolute
# URL's with 'http://' protocol prefix e.g. http://example.com/dir/image.jpg and that
# all links on the target_page point to desired image files.

img_urls = []

page = urllib.request.urlopen(target_page).read()
soup = BeautifulSoup(page, 'html.parser')

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    img_urls.append(link.get('href'))

counter = 1

for img_url in img_urls:

  img_filename = Path(img_url).name
  img_dest = dest_path + '/' + img_filename

  # recreate url with a url-encoded img_filename to handle whitespace in filenames
  img_url_clean = img_url.rsplit('/', 1)[0] + '/' + urllib.parse.quote(img_filename)

  print(str(counter) + ":\t " + img_dest)
  counter += 1

  with urllib.request.urlopen(img_url_clean) as response, open(img_dest, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

  #if counter > 4:
  #  break

print("DONE!")
print("Saved " + str(counter - 1) + " files.")
