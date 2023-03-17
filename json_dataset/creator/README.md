# Data Scraper

This is a tool for scraping the NetSuite Documentation for different instruction steps.

## How to run

1. Install [Node.js](https://nodejs.org/en/download/)
2. In this directory, run `npm install`
3. Go to `gen.js`, and at the bottom change the urls list to the urls you want to scrape
4. Run `node gen.js`
5. The output will be in `data.json`

Note: Node is not available by default on the unity server (as a module or preinstalled). I ran this on my local machine and then copied the output to the unity server. You can probably install node on the unity server, but I didn't try.