# PH Developer Skills Index

This is a simple web scraper that can be used to determine the in-demand 
skills for the current job market in the Philippines. This does not require any back-end framework to run.

## Sample Output

The demand for different programming languages from PH employers:

<img src='https://user-images.githubusercontent.com/76241888/132360549-f6cbee91-799f-497b-94d7-cbab373b2298.png' width='700px'>

---

Another example of real data is shown for the demand for database frameworks.

<img src='https://user-images.githubusercontent.com/76241888/132358961-83ab05ec-eac9-4dd6-b1af-c6cdb5364bb4.png' width='700px'>

## TODO
- [x] Create a separate output folder
- [x] Automate data harvesting using GitHub actions
- [ ] Parse the CSV data using JavaScript
- [ ] Create a web document that displays the output data (using Graphs, tables)
- [ ] Deploy on GitHub Pages

## How to obtain data on your own
### Quick Method
1. Download/clone this repo on your PC. Make sure that Python is installed. This was developed using Python 3.9.6.
2. Open up your terminal (Bash/PowerShell/CMD) and go into the repo's directory.
3. Enter `python run.py` and check the CSV outputs in the `output` directory.

The CSV files can be easily converted to any other useful data format (like JSON).
These files can also be opened with a spreadsheet software like MS Excel.

### Manual Queries

![image](https://user-images.githubusercontent.com/76241888/133780613-0eb91835-66d6-4323-9afd-bc393a244235.png)

Please check  the `queries/` directory if you haven't done so. If you want to create your own CSV query files, take note of the following sample format for the *search term*:

```
(symfony or symphony) (developer or programmer)
```

Enclosing multiple words with a parenthesis (separated with '`or`') will include at least one of the words on the result. This will match all the following terms:

- Symfony developer
- Symfony programmer
- Symphony developer
- Symphony programmer

The search term is not case sensitive. Another example is shown:

```
codeigniter (developer or programmer or "software engineer")
```

This will match all of the following:

- Codeigniter developer
- Codeigniter programmer
- Codeigniter software engineer

To include a phrase as a search term, include quotation marks (e.g., "software engineer").

## Possible Sources of Error
Note that the data is obtained from search results.
The data output might not reflect the actual demand for the following reasons:
- Incomplete (or even redundant) job descriptions
- Keywords do not match the actual job descriptions

Project contributions/suggestions are highly appreciated.
