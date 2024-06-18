"""
Module to demonstrate the idea behind map

This module implements the map function. It also has
several support functions to show how you can leverage it
to process data."""

def map(f,data):
    """Returns a copy of data, f applied to each entry
    
    Parameter f: The function to apply
    Precond: f is a function taking exactly one argument
    
    Parameter data: The data to process
    Precond: data is an iterable, each elt satisfying precond of f"""
    
    accum = []
    for item in data:
        accum.append(f(item))
    return accum

def filter(f,data):
    """
    Generates only the elements of data for which f is True

    Parameter f: The function to apply
    Precondition: f is a boolean function taking exactly one 
    
    Parameter data: The data to process
    Precondition: data an iterable, each element satisfying p
    """
    accum = []
    for item in data:
        if f(item):
            accum.append(item)
    return accum

def plus1(x):
    """
    Returns x+1

    Parameter x: the umber to add to
    Precondition: x is an int or float
    """
    return x+1

def negate(x):
    """
    Returns -x

    Parameter x: The number to negate
    Precondition: x is an int or float
    """
    return -x


def iseven(x):
    """
    Returns True if x is even

    Parameter x: The number to add to
    Precondition: x is an int
    """

    return x % 2 == 0


def ispos(x):
    """
    Returns True if x > 0

    Parameter x: The number to add to
    Precondition: x is an int or float
    """
    return x > 0
