import re
import random
import csv
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


def scrape(keyword_list, filename, job_title):
    regex = re.compile(r'\.csv$')
    # filename can be 'file_sample.csv'
    if not regex.search(filename):
        print('Filename should be a .csv file')
        return None

    regex = re.compile(r'([a-z]+)(\s[a-z]+)*$')
    if not regex.search(job_title):
        print('job_title should contain space separated keywords')
        print('Examples:')
        print('\tDeveloper')
        print('\tData Analyst')
        print('\tSenior Software Developer')
        return None

    # Include the current date (ISO format) on the output
    csv_row = [date.today().isoformat()]
    for item in keyword_list:
        # URL for searching jobs for a particular item:
        url = 'https://ph.indeed.com/jobs?q='

        # URL character replacements:
        url_char_replace = {
            ' ': '%20',
            '+': '%2B',
            '#': '%23'
            }
        item_url = item
        for key in url_char_replace:
            item_url = item_url.replace(key, url_char_replace[key])

        job_title_url = job_title.replace(' ', '%20')
        url += item_url + '%20' + job_title_url + '&l='

        print('Searching for ' + item)
        # Pick a random user agent:
        user_agent = random.choice(user_agent_list)
        # Set the headers
        headers = {'User-Agent': user_agent}
        # Make a request and process out the response:
        request = Request(url=url, headers=headers)
        response = urlopen(request).read()
        webdata = response.decode()
        # Look for the number of jobs using regex:
        regex = re.compile(r'\d+(,\d+)* jobs')
        jobs = regex.search(webdata).group()
        # Example output: jobs = '1,213 jobs'
        # Convert the 'jobs' string into integer:
        jobs_int = int(jobs.replace(',', '').replace(' jobs', ''))
        csv_row.append(jobs_int)

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
            quoting=csv.QUOTE_NONNUMERIC
        )
    except (OSError, IOError) as e:
        # If the file is not yet created, this will be written initially:
        file = open(filename, 'w', newline='')
        file_writer = csv.writer(
            file,
            delimiter=',',
            quotechar='\'',
            quoting=csv.QUOTE_NONNUMERIC
        )
        keyword_list.insert(0, 'date')
        file_writer.writerow(keyword_list)

    file_writer.writerow(csv_row)
    file.close()
    print('The data is written to ' + filename)
    print('Double check the file for errors. '
          'Revise the keyword list if necessary')


if __name__ == '__main__':
    # Sample Query:
    # Determine the demand for back-end web frameworks for developers:
    web_frameworks = [
        'PHP Laravel',
        'Java Spring',
        'ASP .NET',
        'Ruby Rails',
        'Python Django',
        'Python Flask',
        'Node.js',
    ]
    # job_title is 'developer'
    # job_title is used to filter out the results
    scrape(web_frameworks, 'web_frameworks.csv', 'developer')
    # Output the data to 'web_frameworks.csv'
