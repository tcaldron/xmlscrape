# xmlscrape

This Python 3 script extracts URLs from all XML sitemaps contained in the current directory and exports in a variety of formats.

This is typically useful for SEO analysts that need to work with very large sitemaps, which can range into the millions of URLs. Because XML sitemaps should be limited to 50,000 URLs each, very large websites might have a ton of XML sitemap files, and concatenating the URLs from them is a chore. Exporting to a single list allows easier crawling or analysis with SEO-specific tools like Screaming Frog or data science applications.

It can output URLs to a file which you specify, with support for Excel (.xlsx), comma-separated values (.csv), and plain text (.txt). It includes options for deduplication, ignoring of index files, and sorting alphanumerically.

Many thanks to the team at [Climb](https://www.climbmarketing.com) for the support in developing this and our other tools.  

## Installation

Installation (and the instructions for it) have been kept as simple and plain English as possible in order to support SEOs that are newer to Python and GitHub.

Start out by making sure you have Python 3 installed. If you want to check, open up a terminal window on your computer and type "python3 --version." If it says Python 3.6 or higher, you're good to go. If not, go here: <https://www.python.org/downloads/>

Click the green button on this page (on the upper right) and download the zip file. Then open a terminal in the same directory as the zip file's contents (on a Mac, you can right click the folder and look through the options for "New Terminal at Folder") and run:

```bash
pip install -r requirements.txt
```

## Usage

You can run the script with a simple "python3 xmlscrape.py" in the terminal. All arguments are optional, but provide useful functionality: 

```bash
python3 xmlscrape.py # simplest usage, outputs to "output.txt" by default
python3 xmlscrape.py --o scraped_urls.xlsx # outputs the extracted URLs to an Excel file
python3 xmlscrape.py --deduplicate --sort # it can also dedupe and sort before output
python3 xmlscrape.py --ignore_index # you can add this argument in order to ignore sitemap index files
```

Some notes:

* The application assumes that you've placed the XML sitemaps in the same folder as xmlscrape.py. Support for specifying other directories might be added in the future.
* By default, the application will export to "output.txt" unless a filename is specified after --o.
* Unless you apply the --sort argument, deduplicated output will be in somewhat random order. This is because I chose a method of deduplication that's quite fast when working with large amounts of data, but has the disadvantage of not supporting any sort of ordering. If you need it sorted, make sure to apply --sort.
* The --ignore_index function will ignore sitemaps that contain XML markup identifying them as sitemap index files. If there are XML files present that link to other sitemaps but are not flagged as being sitemap index files, this won't apply.  

## To Do

* [ ] Do unit testing (yikes).
* [ ] Add the ability (or create a separate tool) to scrape URLs, deduplicate and sort them, and then re-export back to XML format.
* [ ] Add the ability to specify another directory that contains the sitemaps.
* [ ] Consider using a deduplication method that maintains the original list order.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
