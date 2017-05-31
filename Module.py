# -*- coding: utf-8 -*- 


def function_in_module():
    print "function_in_module was called"


def dump_attributes():
    print "Dumping underscore attrs"
    # print __dict__
    print __doc__
    print __file__
    print __name__
    print __package__
    # print __path__


def dump_caller_location():
    if __name__ == '__main__':
        print 'This program is being run by itself'
    else:
        print 'I am being imported from another module'

if __name__ == "__main__":
    dump_caller_location()