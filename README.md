# lastouski

This repository contains two CSV files with headwords and definitions from Vatslaw Lastouski's dictionary.

A small script `generate_site.py` is provided to convert the CSV files into a static web site with one page per starting letter and a search field that searches across all entries.

## Generating the site

Run the script with Python 3:

```bash
python3 generate_site.py
```

This creates a new `site/` directory containing HTML files for each letter, a `data.json` file with all entries and a simple `search.js` used by the pages. Open `site/index.html` in a browser to browse or search the dictionary.
