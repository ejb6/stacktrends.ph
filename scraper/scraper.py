import re
import random
import csv
import os
import time
from urllib.request import urlopen, Request
from datetime import date

# Request Header (to avoid being blocked by Indeed)
user_agent_list = [
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) '
     'Gecko/20100101 Firefox/91.0'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/13.1.1 Safari/605.1.15'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) '
     'Gecko/20100101 Firefox/77.0'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/83.0.4103.97 Safari/537.36'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) '
     'Gecko/20100101 Firefox/77.0'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/83.0.4103.97 Safari/537.36'),
]


def scrape(csv_file):
    # Output directory is './output/'
    if not os.path.exists('output'):
        os.makedirs('output')
    csv_reader = csv.DictReader(csv_file)
    # Include the current date (ISO format) on the output
    output_row = [date.today().isoformat()]
    # List of skills for the CSV output first row:
    first_row = []
    for row in csv_reader:
        first_row.append(row['name'])
        search_term = row['search term']

        # URL character replacements:
        url_char_replace = {
            '+': '%2B',
            '/': '%2F',
            ' ': '+',
            '#': '%23',
            '"': '%22',
            '(': '%28',
            ')': '%29'
        }
        for key in url_char_replace:
            search_term = search_term.replace(key, url_char_replace[key])

        # URL for searching jobs for a particular item:
        url = 'https://ph.indeed.com/jobs?q=' + search_term

        print('Searching for ' + row['name'])
        # Pick a random user agent:
        user_agent = random.choice(user_agent_list)
        # Set the headers
        headers = {'User-Agent': user_agent}
        # Make a request and process out the response:
        request = Request(url=url, headers=headers)
        response = urlopen(request).read()
        webdata = response.decode()
        # Check if there are no jobs available:
        regex = re.compile('did not match any jobs')
        if regex.search(webdata):
            # Append 0 jobs
            output_row.append(0)
        else:
            # Look for the number of jobs using regex:
            regex = re.compile(r'\d+(,\d+)* jobs')
            jobs = regex.search(webdata).group()
            # Example output: jobs = '1,213 jobs'
            # Convert the 'jobs' string into integer:
            jobs_int = int(jobs.replace(',', '').replace(' jobs', ''))
            output_row.append(jobs_int)

        time_wait = random.randint(0, 2)
        if time_wait:
            print(f'Waiting for {time_wait}s to avoid detection.')
        time.sleep(time_wait)

    filename = 'output/' + os.path.basename(csv_file.name)
    # The following block is used to append the data
    try:
        # Try to check if the file already exist:
        output_file = open(filename, 'r+', newline='')
        # Position stream at the end of the file (for appending)
        output_file.read()
        file_writer = csv.writer(
            output_file,
            delimiter=',',
            quotechar='\'',
            quoting=csv.QUOTE_MINIMAL
        )
    except (OSError, IOError) as e:
        # If the file is not yet created, this will be written initially:
        output_file = open(filename, 'w', newline='')
        file_writer = csv.writer(
            output_file,
            delimiter=',',
            quotechar='\'',
            quoting=csv.QUOTE_MINIMAL
        )
        first_row.insert(0, 'date')
        file_writer.writerow(first_row)

    file_writer.writerow(output_row)
    output_file.close()
    print('The data is written to ' + filename)
    print('Double check the file for errors. '
          'Revise the keyword list if necessary\n')
