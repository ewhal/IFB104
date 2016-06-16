
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9446800 
#    Student name: Eliot Whalan 
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  The Top Ten of Everything 
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design to produce a useful
#  application for accessing online data.  See the instruction
#  sheet accompanying this template for full details.
#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
#  Import the modules needed for this assignment.  You may not import
#  any other modules or rely on any other files.  All data and images
#  needed for your solution must be sourced from the Internet.
#

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import the Tkinter functions
from Tkinter import *

# Import Python's HTML parser
from HTMLParser import *

#import sqlite3
from sqlite3 import *


#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a GIF image, return a Tkinter
#  PhotoImage object suitable for use as the 'image' attribute
#  in a Tkinter Label widget or any other such widget that
#  can display images.
#
def gif_to_PhotoImage(gif_image):

    # Encode the byte stream as a base-64 character string
    # (MIME Base 64 format)
    characters = gif_image.encode('base64', 'strict')

    # Return the result as a Tkinter PhotoImage
    return PhotoImage(data = characters)



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a JPG or PNG image, return a
#  Tkinter PhotoImage object suitable for use as the 'image'
#  attribute in a Tkinter Label widget or any other such widget
#  that can display images.  If positive integers are supplied for
#  the width and height (in pixels) the image will be resized
#  accordingly.
#
def image_to_PhotoImage(image, width = None, height = None):

    # Import the Python Imaging Library, if it exists
    try:
        from PIL import Image, ImageTk
    except:
        raise Exception, 'Python Imaging Library has not been installed properly!'

    # Import StringIO for character conversions
    from StringIO import StringIO

    # Convert the raw bytes into characters
    image_chars = StringIO(image)

    # Open the character string as a PIL image
    pil_image = Image.open(image_chars)
    
    # Resize the image, if a new size has been provided
    if type(width) == int and type(height) == int and width > 0 and height > 0:
        pil_image = pil_image.resize((width, height), Image.ANTIALIAS)

    # Return the result as a Tkinter PhotoImage
    return ImageTk.PhotoImage(pil_image)



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by putting your solution below.
#


##### DEVELOP YOUR SOLUTION HERE #####

# Takes an image_url reads the url then returns
# the converted image
#
def dlImage(image_url):
    read_image = urlopen(image_url).read()
    photo_image = gif_to_PhotoImage(read_image) 
    return photo_image

# The topTen function takes the feedUrl, background and foreground colours
# it will then read the feed url, find all data between the <title></title> elements
# then will enumerate from 2:13 elminating any Page names
# Then it uses HTMLParser to unescape HTML
# Prepares the text to be displayed
# Then sets the label and packs it
#
def topTen(win, feedUrl, background, foreground):
    feed = urlopen(feedUrl).read()
    feedTitles = re.findall(r'<title>(.*?)</title>', feed)
    for index, title in enumerate(feedTitles[2:12]):
        parser = HTMLParser()
        text = parser.unescape(title)
        displayText = "{}. {}".format(index + 1, text)
        w = Label(win, text=displayText)
        w.config(bg=background, fg=foreground)
        w.pack()
    x = Label(win, text=feedUrl)
    x.config(bg=background, fg=foreground)
    x.pack()
    closure = lambda: save(feedTitles)
    Button(win, text="Save", command=closure).pack(side="right", expand=True, fill=X)


#Generates a button based upon the desired command and the name
def mkButton(win, pagelist, page):
    name, _, _, _, _, _, _  = page
    closure = lambda: setPage(win, pagelist, page)
    Button(win, text=name, command=closure).pack(side="left", expand=True, fill=X)

#Saves the given feed into a database
#Deletes and creates a new database on every execute 
def save(topTen):
    connection = connect(database = "top_ten.db")
    with connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS Top_Ten;")
        cursor.execute('''CREATE TABLE "Top_Ten"(`Rank` INTEGER, `Description` TEXT, PRIMARY KEY(Rank))''')

        for index, title in enumerate(topTen[2:12]):
            cursor.execute("INSERT INTO Top_Ten VALUES(?, ?);", (index + 1, title))

    connection.commit()
    cursor.close()
    connection.close() 
    


#Generates a label with an image
def mkImage(win, img, pos):
    Label(win, image=img).pack(side=pos)

# First off sets the title based off the set name
# Changes background colour
# Destroys the previous elements to give a clean slate
# Makes the image
# calles the defined function with any arguments in this case
# it will call topTen
# Generates button list
def setPage(win, pagelist, thispage):
    name, img, func, args, background, foreground, pos = thispage

    win.title(name)
    win.configure(bg=background)

    for child in win.winfo_children():
        child.destroy()

    mkImage(win, img, pos)

    func(win, *args)

    for page in pagelist:
        mkButton(win, pagelist, page)




def main():
    win = Tk()
    # eagerly evaluate the images to prevent program from freezing
    pagelist = [
            ["home", dlImage("http://b.1339.cf/cknwtvx.gif"), lambda win: None, [],"white", "black", "top"], # just img+nav
            ["sports", dlImage("http://b.1339.cf/aekkwmo.gif"), topTen, ["http://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU", "green", "yellow",], "green", "yellow", "left"],
            ["politics", dlImage("http://b.1339.cf/slxmxjm.gif"), topTen, ["http://www.theage.com.au/rssheadlines/political-news/article/rss.xml", "pink", "white",], "pink", "white", "right"],
            ["trends", dlImage("http://b.1339.cf/wiabylh.gif"), topTen, ["http://www.google.com/trends/hottrends/atom/feed?pn=p1", "red", "black",], "red", "black", "left"],
    ]
    setPage(win, pagelist, pagelist[0])
    win.mainloop()

if __name__ == "__main__":
    main()
