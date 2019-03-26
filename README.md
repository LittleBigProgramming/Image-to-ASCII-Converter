# Image-to-ASCII-Converter
This is a CLI application taking an image and outputting a text file with the image drawn in ASCII style. This is based on the density level of the greyscale of the image once converted.

This was the result of following a tutorial in Python Playground Geeky Projects for the Curious Programmer by Mahesh Venkitachalam. If you can interested in the book it can be found [here.](https://nostarch.com/pythonplayground) As this was one of my first experiences with Python I thought this was a really cool idea and I hope to build on it further in the future. 

As I had never setup a python environment before, these are the steps I carried out to do it.

Install pip/upgrade to the latest version - `python3 -m pip install --user --upgrade pip` 

Next install virtualenv - `python3 -m pip install --user virtualenv` This allows you to manage packages for different projects.

Once this is done run `python3 -m virtualenv env` for your isolated python environment and `source env/bin/activate` to activate it.

Packages can now be installed
```
pip install numpy
pip install image
```

The image package is a dependancy of PIL (Python Imaging Library) and numpy is used to compute averages.

To run the CLI help command run `python ascii.py -h` otherwise to run the program with it's required params run `python ascii.py --file image.jpg`
