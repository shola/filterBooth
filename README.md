career-fair-winnower
====================

Ruthlessly decide which employers to ignore at crowded high-tech career fairs based only on their GlassDoor rating.

To run, enter this into the terminal: <code>python3.4 career_fair_researcher.py</code>

The <code>glassdoor</code> module was not reliably producing company ratings, with many searched companies turning up <code>None</code>. Instead of using the GlassDoor API, this script leverages the Python <code>google</code> and <code>bs4</code>(BeautifulSoup) modules to select the ratings directly from a company's GlassDoor overview page.
<hr>

<strong>System Requirements</strong>: Python 3.4, *nix<br>
<strong>Required Modules</strong>: google, bs4 (BeautifulSoup)<br>
<strong>Input</strong>: reads in the company names from <code>companyList.txt</code>. Simply replace the file contents with a list of company names, one per line.<br>
<strong>Output</strong>: CSV file named 'glassdoorRatings.txt' of company names and ratings.<br>
