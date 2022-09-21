# Web Scraper

Using Python and its packages to extract certain information from a website, e.g. product names.

## How to use
Using one's preferred code editor (e.g. VSCode), user enters keyword 'python' and filepath followed by url as string and xpath as string. Xpath can easily be copied in browser.

e.g. `python projects/WebScraper/extract_data.py "https://leroymerlin.co.za/building-materials/construction-equipment/ladders" "//*[@id='maincontent']/div[4]/div[1]/div[9]/ol/li/div[2]/strong/a"`

## How to test
Using one's preferred code editor (e.g. VSCode), user enters keyword 'pytest' and filepath followed by url.

e.g. `pytest projects/WebScraper/test_extract_data.py'

## Code and Resources Used
**Python Version:** `3.10.6`

**Packages:** `click, requests` 

**url:** `"https://leroymerlin.co.za/building-materials/construction-equipment/ladders"`

**xpath:** `"//*[@id='maincontent']/div[4]/div[1]/div[9]/ol/li/div[2]/strong/a"`





