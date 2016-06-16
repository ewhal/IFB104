#-----------------------------------------------------------
#
# Web Page Downloader
#
# For a particular URL, this simple program downloads a web
# page and prints it to the Python shell window.
# You can then examine the HTML/XML source of the document
# and copy parts of it into the "regex tester" to help you
# develop your expressions for extracting particular document
# elements.  This simple script has no user interface or error
# handling, but feel free to add them if you want!
#
# Q: Why not just look at the web page's source in your
# favourite web browser (Firefox, Google Chrome, etc)?
#
# A: Because when a Python script uses the hyper-text transfer
# protocol to download a web document, it may not receive
# the same file you see in your browser!  Some web servers
# produce different HTML or XML code for different browsers.
# Therefore, to guarantee that the code you inspect is the
# same code that your own Python program sees, it's safer
# to download the web page using this script.
#

from urllib import urlopen

url = 'http://www.theage.com.au/rssheadlines/political-news/article/rss.xml' # Put your web page address here

# Read the contents of the web page as a string
web_page_contents = urlopen(url).read()

# Show the string to the user
print web_page_contents

# At this point you have the Web document as a string,
# so you can put whatever Python code you like here
# to manipulate it, or cut-and-paste the displayed contents
# from IDLE's shell window into some other tool such as
# the "regex tester" or a text editor


