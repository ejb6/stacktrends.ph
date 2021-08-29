# PH Jobskills Index
This is a simple web scraper that can be used to determine the in-demand 
skills for the current job market in the Philippines. This is a work in progress.

## How to Use
1. Edit `scraper.py`. The input format for the function is included in the file.
2. Run `python scraper.py`. This should output one or more javascript files.
3. Each javascript file contains a list of Json data.
  You can process this file however you want.
  
## Sample Output
The current demand for different Web frameworks for companies that are
hiring web developers:

<code>
const webFrameworks = [{
    "date": "2021-08-29", 
    "laravel": 1411, 
    "spring-boot": 278, 
    "asp.net": 73, 
    "ruby-rails": 74, 
    "python-django": 87, 
    "python-flask": 26, 
    "node.js": 1001
}]
</code>
