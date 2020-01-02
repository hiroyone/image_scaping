# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# Download the google image search api
# !conda install --yes google
# !conda install --yes google_images_download

# +
from google_images_download import google_images_download   #importing the library
from selenium import webdriver
import os

home_dir=os.getenv("HOME")
driver = webdriver.Chrome(home_dir+'/Downloads/chromedriver')
response = google_images_download.googleimagesdownload()   #class instantiation

keyword = "幕の内弁当 画像"

arguments = {"keywords":keyword,"limit":100,"print_urls":True} 
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
