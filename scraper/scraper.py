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

# Check for a sample query on the bottom of this file.
# The output data is stored in a CSV file


def scrape(keywords, filename, job_title):
    regex = re.compile(r'\.csv$')
    # filename can be 'file_sample.csv'
    if not regex.search(filename):
        print('Filename should be a .csv file')
        return None

    # Change output directory to './output/'
    if not os.path.exists('output'):
        os.makedirs('output')
    os.chdir('output')

    # Include the current date (ISO format) on the output
    csv_row = [date.today().isoformat()]
    for skill in keywords:
        # URL for searching jobs for a particular item:
        url = 'https://ph.indeed.com/jobs?q='
        url += job_title
        if len(keywords[skill]) == 0:
            url += ' "' + skill + '"'
        else:
            # Add quotes to keywords to account for spaces:
            for i in range(len(keywords[skill])):
                keywords[skill][i] = '"' + keywords[skill][i] + '"'
            url += ' (' + ' or '.join(keywords[skill]) + ')'
        # URL character replacements:
        url_char_replace = {
            '+': '%2B',
            ' ': '+',
            '#': '%23',
            '"': '%22',
            '(': '%28',
            ')': '%29'
        }
        for key in url_char_replace:
            url = url.replace(key, url_char_replace[key])

        print('Searching for ' + skill)
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
            csv_row.append(0)
        else:
            # Look for the number of jobs using regex:
            regex = re.compile(r'\d+(,\d+)* jobs')
            jobs = regex.search(webdata).group()
            # Example output: jobs = '1,213 jobs'
            # Convert the 'jobs' string into integer:
            jobs_int = int(jobs.replace(',', '').replace(' jobs', ''))
            csv_row.append(jobs_int)

        time_wait = random.randint(0, 4)
        print(f'Waiting for {time_wait} seconds to avoid detection.\n')
        time.sleep(time_wait)

    # The following block is used to append the data
    try:
        # Try to check if the file already exist:
        file = open(filename, 'r+', newline='')
        # Position stream at the end of the file (for appending)
        file.read()
        file_writer = csv.writer(
            file,
            delimiter=',',
            quotechar='\'',
            quoting=csv.QUOTE_MINIMAL
        )
    except (OSError, IOError) as e:
        # If the file is not yet created, this will be written initially:
        file = open(filename, 'w', newline='')
        file_writer = csv.writer(
            file,
            delimiter=',',
            quotechar='\'',
            quoting=csv.QUOTE_MINIMAL
        )
        first_row = list(keywords.keys())
        first_row.insert(0, 'date')
        file_writer.writerow(first_row)

    file_writer.writerow(csv_row)
    file.close()
    os.chdir(r'../')
    print('The data is written to ./output/' + filename)
    print('Double check the file for errors. '
          'Revise the keyword list if necessary\n')


if __name__ == '__main__':
    # Sample Query:
    # Determine the demand for back-end web frameworks for developers:
    web_frameworks = {
        'Laravel': [],  # Leaving the keywords blank is allowed
        'Spring': ['spring', 'springboot'],
        'ASP.NET': ['asp.net', '.net core'],
        'Ruby on Rails': ['Ruby Rails', 'Ruby on Rails'],
        'Django': [],
        'Flask': [],
        'Express': ['node', 'node.js', 'MERN'],
    }
    # job_title is 'developer'
    # job_title is used to filter out the results
    scrape(web_frameworks, 'web_frameworks.csv', 'developer')
    # Output the data to 'web_frameworks.csv'
