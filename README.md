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
Check `sample_query.py`. Sample inputs for the function are included in this file.

1. Download a copy of the `scraper` folder (where `scraper.py` is located).
2. Create a directory and copy the `scraper` folder into this directory.
3. Create a Python file in the directory you created and write `from scraper import scrape` on the beginning of the file.
4. Include the `scrape` function with correct inputs (check for samples in `sample_query.py`).
5. Run the python file you created. This should output one or more CSV files.
6. CSV files can be opened using a spreadsheet software.

The CSV files can be easily converted to any other useful data format (like JSON).
  
## Sample Output
The demand for different back-end frameworks from companies that are
hiring web developers (real data):

<img src='https://user-images.githubusercontent.com/76241888/131454095-d2e3e99c-584b-4274-93d5-d3ce7fcb0586.png' width='700px'>

---

Another example of real data is shown for the demand of programming languages by PH companies:

<img src='https://user-images.githubusercontent.com/76241888/131453606-4bf48d47-72de-4465-a926-54a1e394f55f.png' width='700px'>

## Possible Sources of Error
Note that the data is obtained from search results.
The data output might not reflect the actual demand for the following reasons:
- Incomplete (or even redundant) job descriptions
- Keywords do not match the actual jobs descriptions
- Skills that are not actually required but they are somehow included in the description.

Project contributions/suggestions are highly appreciated.
