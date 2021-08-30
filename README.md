# PH Jobskills Index
This is a simple web scraper that can be used to determine the in-demand 
skills for the current job market in the Philippines. This is a work in progress.

## Todos
- [ ] Error handling
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
hiring web developers (real data):
```
const webFrameworks = [
  {
    "date": "2021-08-30", 
    "PHP Laravel": 363, 
    "Java Spring": 529, 
    "ASP .NET": 543, 
    "Ruby Rails": 100, 
    "Python Django": 115, 
    "Python Flask": 56, 
    "Node.js": 446
  }
]
```

---

Another example of real data is shown for the in-demand skills of Data analysts:
```
const dataAnalytics = [
  {
    "date": "2021-08-30", 
    "sql": 930, 
    "tableau": 377, 
    "power-bi": 358, 
    "excel": 1657, 
    "python": 376
  }
]

```

## Possible Sources of Error
The data output might not reflect the actual demand for the following reasons:
- Incomplete job descriptions
- Keywords do not match the actual jobs descriptions
- Skills that are not actually required but they are somehow included in the description.

Project contributions/suggestions are highly appreciated.
