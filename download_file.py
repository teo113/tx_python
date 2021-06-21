# author: github.com/teo113
# desc: This script downloads a file from a url to a specified folder

import requests

url = r'https://linktofile'
output = r'C:\pathtofolder\downloaded_file.zip'

r = requests.get(url)
with open(output, 'wb') as f:
    f.write(r.content)

