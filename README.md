# PH Jobskills Index

This is a very simple web scraper that can be used to determine the in-demand 
skills for the current job market in the Philippines. This is a work in progress.

## Todos
- [ ] Error handling
- [ ] Automate data harvesting using Github actions
- [ ] Create a web document that displays the output data (using Graphs/Tables/etc)
- [ ] Deploy on Github Pages
- [ ] More detailed documentation

## How to Use
1. Check and edit `scraper.py`. The sample input for the function is included in the file.
2. Run `python scraper.py`. This should output one or more CSV files.
3. CSV files can be opened using a spreadsheet software.

The CSV files can be easily converted to any other useful data format (like JSON).
  
## Sample Output
The demand for different back-end frameworks from companies that are
hiring web developers (real data):

<img src='https://user-images.githubusercontent.com/76241888/131454095-d2e3e99c-584b-4274-93d5-d3ce7fcb0586.png' style='width: 80%'>

---

Another example of real data is shown for the demand of programming languages by PH companies:

<img src='https://user-images.githubusercontent.com/76241888/131453606-4bf48d47-72de-4465-a926-54a1e394f55f.png' style='width: 80%'>

## Possible Sources of Error
Note that the data is obtained from search results.
The data output might not reflect the actual demand for the following reasons:
- Incomplete (or even redundant) job descriptions
- Keywords do not match the actual jobs descriptions
- Skills that are not actually required but they are somehow included in the description.

Project contributions/suggestions are highly appreciated.
