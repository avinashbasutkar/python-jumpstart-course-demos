import shutil
import requests
import os
import subprocess

url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'

os.chdir(r'C:\\Users\\abasutkar\\Desktop\\Python_Scripts\\Python Jumpstart\\cat pictures')

folder = 'C:\\Users\\abasutkar\\Desktop\\Python_Scripts\\Python Jumpstart\\cat pictures'

i = 0
while i < 8:
    i += 1
    res = requests.get(url, stream=True)

    file_name = 'cat{}'.format(i) + '.jpg'

    with open(file_name, 'wb') as f:
        shutil.copyfileobj(res.raw, f)

subprocess.call(['explorer', folder])