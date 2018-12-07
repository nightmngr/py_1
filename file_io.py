
# primeri so file input/output

"""
The 'with' and 'as' Keywords
Programming is all about getting the computer to do the work.
Is there a way to get Python to automatically close our files for us?

Of course there is. This is Python.

You may not know this, but file objects contain a special pair of 
built-in methods: __enter__() and __exit__(). The details aren't important, 
but what is important is that when a file object's __exit__() method is invoked, 
it automatically closes the file. How do we invoke this method? With with and as.

The syntax looks like this:

with open("file", "mode") as variable:
  # Read or write to the file

eve primer:

with open("text.txt", "w") as textfile:
  textfile.write("Success!")




Python file objects have a closed attribute which is True when the file is closed and False otherwise.

By checking file_object.closed, we'll know whether our file is closed and can call close() on it 
if it's still open.

"""

# Pr 1

print "Primer 1"
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")
# w  - write
# r  - read
# r+ - read + write

for item in my_list:
  f.write(str(item) + "\n")
  # print f.read() e za citanje od file i go vrakja cel file
  # .readline() cita linija po linija
  # prviot povik na .readline() ja vrakja prvata linija
  # i sekoj nareden povik ja vrakja slednata linija

f.close()

print
print