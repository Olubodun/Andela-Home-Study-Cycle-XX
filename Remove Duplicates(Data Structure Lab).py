#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      Olubodun
#
# Created:     15-02-2017
# Copyright:   (c) Olubodun 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def remove_duplicates(string):
    duplicates=[]
    alpha= 'abcdefghijklmnopqrstuvwxyz'
    for i in alpha:
     if len(string) >=1:
        duplicates.append((len (string)))
     unique = "".join(sorted(set(string)))
     dup_removed = len(string)- len(unique)
     return (unique,dup_removed)

