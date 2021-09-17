# You don't have to modify this file
# Check the 'queries' directory for sample queries
from scraper import scrape
import os

for filename in os.listdir('queries'):
    query_file = open('queries/' + filename, 'r')
    scrape(query_file)
