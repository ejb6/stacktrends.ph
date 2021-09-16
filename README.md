# PH Developer Skills Index

This is a very simple web scraper that can be used to determine the in-demand 
skills for the current job market in the Philippines. This is a work in progress.

## Todos
- [x] Create a separate output folder
- [ ] Automate data harvesting using Github actions
- [ ] Parse the CSV data using JavaScript
- [ ] Create a web document that displays the output data (using Graphs/Tables/etc)
- [ ] Deploy on Github Pages

## How to Use
### Quick Method
1. Download/clone this repo on your PC. Make sure that Python is installed (preferrably v3.9.6).
2. Open up your terminal (Bash/Powershell/CMD) and go into the repo's directory.
3. Run `python sample_query.py` and check the CSV outputs in the `output` directory. 
   You can edit `sample_query.py` to custumize the output.

### Manual
1. Download a copy of the `scraper` folder (where `scraper.py` is located).
2. Create a directory and copy the `scraper` folder into this directory.
3. Create a Python file in this directory and write `from scraper import scrape` on the beginning of the file.
4. Include the `scrape` function with correct inputs (check for samples in `sample_query.py`).
5. Run the python file you created. This should output one or more CSV files to an output folder.

The CSV files can be easily converted to any other useful data format (like JSON).
These files can also be opened with a spreadsheet software like MS Excel.
  
## Sample Output
The demand for different programming languages from PH employers (real data):

<img src='https://user-images.githubusercontent.com/76241888/132360549-f6cbee91-799f-497b-94d7-cbab373b2298.png' width='700px'>

---

Another example of real data is shown for the demand for database frameworks.

<img src='https://user-images.githubusercontent.com/76241888/132358961-83ab05ec-eac9-4dd6-b1af-c6cdb5364bb4.png' width='700px'>

## Possible Sources of Error
Note that the data is obtained from search results.
The data output might not reflect the actual demand for the following reasons:
- Incomplete (or even redundant) job descriptions
- Keywords do not match the actual job descriptions

Project contributions/suggestions are highly appreciated.
