""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    ex = exists(file_name) #check if exists
    fr = open(file_name, 'rb+') #open reading file
    if not ex or reset: #check if file not exist or reset
        c = 0 # start counter
    else:
        c = load(fr) #read counter
    fr.close() # close read file
    fw = open(file_name, 'wb') #open file for writing
    c += 1 #update counter
    dump(c, fw) #dump updated counter
    fw.close() #close file
    return c #return updated counter

if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
