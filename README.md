# python-tutorial
Python tutorial for SWE x ACE event!

## Welcome!
This tutorial is intended for people of any skill level. Today we're going to be learning about how we can use python to make something cool, and by extension, learning a little bit about the potential for cool fun stuff that can be made with code.

## What is Python?

According to the website:
"Python is powerful... and fast;
plays well with others;
runs everywhere;
is friendly & easy to learn;
is Open."

Python is an interpreted high level language for general purpose programming. There are literally so many applications of Python and today we're only going to be going over the very basics of what you can do with Python and with programming as a whole.

## How to download all the stuff you'll need
I don't recommend following along this tutorial. This is meant to be a gentle introduction and I found myself running into a lot of issues downloading the same things on Windows and MacOS. If you're curious to try this exercise out on your own and other exercises, as well, I will post a link to the book I adapted this tutorial from as well as other helpful videos and links.
If you run into any issues with the instructions below don't hesitate in either messaging me on Facebook or emailing me at dtravie@gmail.com. It can be very easy to mess things up!

## What are we making??
We're going to be creating what's known as a webscraper. We're going to run a script in a language called Python which can allow us to open webpages, send information to websites, and retrieve information from websites.

To do this some other people wrote what's known as a package which is like DLC but for existing languages and codebases.

## Program 1: Insta-py!
We're going to create a Python program which will take us to our desired instagram site based on the command line arguments we provide it.
Let's create a file in our text editor of choice and name it `instapy.py`
Just to make sure everything is working I'm going to do what's known as a 'Hello World'. This is usually the first program you write in a new language and Python's has to be the most elegant of them all:

```python
print('hello world!')
```
Sidenote: this is a terminal emulator which allows us text based access to our operating system. In order for this tutorial to last just under an hour I'm not going to go too much into it. However, if you have any questions about what I'm doing you're more than welcome to ask and I'd be super down to guide you or get started with working from a command line.

There's all sorts of programming concepts available for exploration within Python. Today we're just going to use simple if statements, and a for loop.
We're going to use a module called 'webbrowser' to allow us to open websites. We need this package so we can open whatever website we want from Instagram.

```python
import webbrowser
webbrowser.open('https://instagram.com')
```
This is pretty cool but we want to be able to open whatever instagram we feel like opening in a given time. In order to do this it would be really cool if we could use what's known as a command line argument. This means we're passing in stuff through the terminal. To achieve this, we need to import the sys module. This allows python access to the system specific parameters and functions.

```python
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.instagram.com/' + address)
# Note:
# If you do not include join the following error will occur
# TypeError: cannot concatenate 'str' and 'list' objects

```

There's a couple things going on here

If statements will execute the code that is encapsulated by it when the condition evaluates to true
Else statements will execute when the condition evaluates to false
We are asking the system if the length of the arguments being passed into the terminal is greater than one. Why?
sys.argv is actually an array of the words after python
`['instapy.py', 'beyonce']`

If the length is indeed greater than 1, then we want to equate `address` to those arguments, not including the name of the file. The notation `[1:]` denotes the array starting at 1 until the end of the array, whatever length that might be.

If the length is 1 or less, the address will then be equated to whatever what was on our clipboard

### Let's play around with it!


## Program 2: Py-de and Prejudice!

Now we're going to use a package called `requests` to request information from a webpage. We're going to download the entirety of Pride and Prejudice to a file on our computer.

Make a new file and write the following

```python
import requests

myFile = requests.get('http://www.gutenberg.org/files/1342/1342-0.txt')

playFile = open('PrideAndPrejudice.txt', 'wb')
#len(myFile.text)
#print(myFile.text[:250])
```

Importing the requests package allows us to run these specially written functions for `Request` objects like `get`. `get` is what takes the url of whatever it is you want to download.

playFile is going to be a text file we create to store the information we've retrieved from the website. `wb` stands for write binary which lets the open function know that we have to open the file in write binary mode. We want to use binary data rather than text data which has to do with what's known as Unicode encodings.

```python
for i in myFile.iter_content(100000):
    playFile.write(i)
playFile.close()
```

This is what's known as a for loop. A for loop will move through a list using an iterator, in this case we're using `i`. For each element denoted by i, we're going to take what's in myFile (the data we got from the website) and write to the playFile (the file we created on our hard drive). The 100000 just denotes that we'll be writing at 100,000 bytes at a time.

# Thanks for watching!

If you have any questions feel free to Facebook message me or email me at dtravie@gmail.com. This tutorial was adapted from the following book which also has a ton of neat exercises and other topics as well. https://automatetheboringstuff.com/chapter11/

Join the ACE slack at https://uf-ace.slack.com

There are tons of free resources if you're interested in learning Python but if you need any guidance on what to learn or do feel free to shoot me a message I'd be glad to help out!
