#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Olubodun
#
# Created:     10-02-2017
# Copyright:   (c) Olubodun 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def is_isogram(string):
    if isinstance(string, str) and len(string) != 0:
        string = string.lower()
        return string, len(string) == len(set(string))
    if not string:
        return string, False;
    raise TypeError('Argument should be a string')
