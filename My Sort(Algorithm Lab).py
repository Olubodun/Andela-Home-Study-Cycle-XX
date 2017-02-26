#---------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Olubodun
#
# Created:     14-02-2017
# Copyright:   (c) Olubodun 2017
# Licence:     <your licence>
#----------------------------------------------------------------------------
def my_sort(x):
    return sorted([i for i in x if i%2==1]) + sorted([i for i in x if i%2 == 0])



