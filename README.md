# PH Jobskills Index

This is a very simple web scraper that can be used to determine the in-demand 
skills for the current job market in the Philippines. This is a work in progress.

## Todos
- [ ] Create a separate output folder
- [ ] Automate data harvesting using Github actions
- [ ] (Option 1) Convert CSV to JSON file
- [ ] (Option 2) Directly create JSON file on `scraper.py`
- [ ] Create a web document that displays the output data (using Graphs/Tables/etc)
- [ ] Deploy on Github Pages

## How to Use
Check or try to run `sample_query.py`. Sample inputs for the function are included in this file.
All sample file outputs are included in this repo as CSV files.

1. Download a copy of the `scraper` folder (where `scraper.py` is located).
2. Create a directory and copy the `scraper` folder into this directory.
3. Create a Python file in this directory and write `from scraper import scrape` on the beginning of the file.
4. Include the `scrape` function with correct inputs (check for samples in `sample_query.py`).
5. Run the python file you created. This should output one or more CSV files.
6. CSV files can be opened using a spreadsheet software.

The CSV files can be easily converted to any other useful data format (like JSON).
  
## Sample Output
The demand for different back-end frameworks from companies that are
hiring web developers (real data):

<img src='https://user-images.githubusercontent.com/76241888/132360549-f6cbee91-799f-497b-94d7-cbab373b2298.png' width='700px'>

---

Another example of real data is shown for the demand of programming languages by PH companies:

<img src='https://user-images.githubusercontent.com/76241888/132358961-83ab05ec-eac9-4dd6-b1af-c6cdb5364bb4.png' width='700px'>

## Possible Sources of Error
Note that the data is obtained from search results.
The data output might not reflect the actual demand for the following reasons:
- Incomplete (or even redundant) job descriptions
- Keywords do not match the actual jobs descriptions
- Skills that are not actually required but they are somehow included in the description.

Project contributions/suggestions are highly appreciated.
