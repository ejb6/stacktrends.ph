import re
import json
from urllib.request import urlopen, Request
from datetime import date

# Request Header (to avoid being blocked by Jobstreet)
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924\
    .87 Safari/537.36'
    }

# Check for a sample query on the bottom of this file.
#
# The output data is stored in a JS file so that...
# it can be readily displayed in a web document.


def scrape(keyword_list, filename, job_title):
    # filename can be 'camelCase.js'
    regex = re.compile(r'\.js$')
    if not regex.search(filename):
        print('Filename should be a .js file')
        return None

    regex = re.compile(r'\s')
    if regex.search(filename):
        print('Filename should not contain any whitespace')
        return None

    regex = re.compile(r'([a-z]+)(\-[a-z]+)*$')
    if not regex.search(job_title):
        print('job_title should contain dash separated lowercase keywords')
        print('Examples:')
        print('\tdeveloper')
        print('\tdata-analyst')
        print('\tsenior-software-developer')
        return None

    # Include the current date (ISO format) on the output
    json_data = {'date': date.today().isoformat()}
    for item in keyword_list:
        # URL for searching jobs for a particular item:
        url = 'https://www.jobstreet.com.ph/en/'
        url += 'job-search/' + item + '-' + job_title + '-jobs'

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
        json_data[item] = jobs_int

    # The following block is used to append the json_data
    with open(filename, 'w+') as convert_file:
        contents_current = convert_file.read()
        # The current content of the file is similar to the following:
        #   const data = [...list of json data...]
        if contents_current:
            contents_current.replace(']', ',')
        else:
            # If the file is not yet created, this will be written initially:
            regex = re.compile(r'\.js$')
            contents_current = 'const ' + regex.sub('', filename)
            contents_current += ' = ['
        convert_file.write(contents_current + json.dumps(json_data) + ']')


if __name__ == '__main__':
    # Sample Query:
    # Determine the demand for back-end web frameworks for developers:
    web_frameworks = [
        'laravel',
        'spring-boot',
        'asp.net',
        'ruby-rails',
        'python-django',
        'python-flask',
        'node.js'
        ]
    scrape(web_frameworks, 'webFrameworks.js', 'developer')
    # Output the data to 'webFrameworks.js'
