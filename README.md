# PH Jobskills Index
This is a simple web scraper that can be used to determine the in-demand 
skills for the current job market in the Philippines. This is a work in progress.

## Todos
- [ ] Automate data harvesting using Github actions
- [ ] Create a web document that displays the output data (using Graphs/Tables/etc)
- [ ] Deploy on Github Pages
- [ ] More detailed documentation

## How to Use
1. Check and edit `scraper.py`. The sample input for the function is included in the file.
2. Run `python scraper.py`. This should output one or more javascript files.
3. Each javascript file contains a list of Json data.
  You can process this file however you want.
  
## Sample Output
The demand for different back-end frameworks from companies that are
hiring web developers on a span of two days (real data):
```
const webFrameworks = [
  {
    "date": "2021-08-27", 
    "laravel": 1400, 
    "spring-boot": 278, 
    "asp.net": 73, 
    "ruby-rails": 74, 
    "python-django": 87, 
    "python-flask": 26, 
    "node.js": 1060
  },
  {
    "date": "2021-08-29", 
    "laravel": 1411, 
    "spring-boot": 278, 
    "asp.net": 73, 
    "ruby-rails": 74, 
    "python-django": 87, 
    "python-flask": 26, 
    "node.js": 1001
  },
]
```
The demand for laravel developers increased from 1400 jobs to 1411 jobs in a matter of two days.

---

Another example of real data is shown for the in-demand skills of Data analysts:
```
const dataAnalytics = [
  {
    "date": "2021-08-29", 
    "sql": 3620, 
    "tableau": 1993, 
    "power-bi": 1771, 
    "excel": 3614, 
    "python": 1728
  }
]
```
The number of available jobs for Data analysts are higher than web developers.

## Possible Sources of Error
The data output might not reflect the actual demand for the following reasons:
- Incomplete job descriptions
- Keywords do not match the actual jobs descriptions
- Skills that are not actually required (but having it is a *plus*)

Project contributions/suggestions are accepted for addressing these issues.
