## XMLScrape v0.0.1
## Written by Taylor Caldron at Climb Marketing (www.climbmarketing.com)
## Questions or suggestions: taylor@climbmarketing.com

import glob
from progress.bar import ShadyBar
import xmls_functions 

# First we parse the arguments and verify existence of sitemaps.
namespace = xmls_functions.parse_arguments()
numberOfSitemaps = xmls_functions.detect_sitemaps()

# Next we initialize the progress bar.
bar = ShadyBar("Processing:", max=numberOfSitemaps, 
suffix="%(index)d XML Sitemaps Processed") 

# We set up an empty list to fill via our processSitemap function.
cleanedURLs = [] 

# This is the meat of the application. We open up each sitemap
# in the local directory, scrape out the URLs, and append
# them to our list. 
for filename in glob.glob('*.xml'): 
    cleanedURLs = cleanedURLs \
    + xmls_functions.process_sitemap(filename, namespace)
    bar.next() # Incrementing the progress bar

# Shut down the progress bar once that's over. 
bar.finish() 

# Deduplicating list by converting to a set, if required. It's fast,
# but doesn't maintain the order of the original list, which is 
# part of why a sorting option was also necessary. 
if namespace.deduplicate:
    cleanedURLs = xmls_functions.deduplicate_URLs(cleanedURLs)

# Sorting, if required.
if namespace.sort:
    print("Sorting URLs in alphanumeric order.")
    cleanedURLs = sorted(cleanedURLs)

# Writing final URL list to file.
xmls_functions.output_URLs(cleanedURLs, namespace.o)

# Providing user feedback that process is complete.
print(f"Final URL list contains {len(cleanedURLs)} entries, output to" +  
    f" {namespace.o}.")
