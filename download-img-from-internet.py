# https://image.shutterstock.com/image-photo/closeup-portrait-smiling-half-naked-260nw-1356965294.jpg

# requests
# wget
# urllib

# 1.>  requests

import requests
import shutil

image_url = "https://image.shutterstock.com/image-photo/closeup-portrait-smiling-half-naked-260nw-1356965294.jpg"

fileName = image_url.split("/")[-1].split("-")[-1]

req = requests.get(image_url , stream= True)

if req.status_code == 200:

    req.raw.decode_content = True

    with open(fileName, "wb") as f:
        shutil.copyfileobj(req.raw , f)
    print("The image is downloaded successfully",fileName)
else:
    print("The image can't be downloaded!")

# ----------------------------------------------------------------------------------------
#2.> wget

import  wget

image_url = "https://image.shutterstock.com/image-photo/closeup-portrait-smiling-half-naked-260nw-1356965294.jpg"

imageName = wget.download(image_url)
print("Successfully downloaded image",imageName)

# ----------------------------------------------------------------------------------------
#3.> urllib


import urllib.request

image_url = "https://image.shutterstock.com/image-photo/closeup-portrait-smiling-half-naked-260nw-1356965294.jpg"

imageName = "12345.jpg"

urllib.request.urlretrieve(image_url , imageName)

