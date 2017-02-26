#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Olubodun
#
# Created:     14-02-2017
# Copyright:   (c) Olubodun 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def power(a, b):
    if type(a) == int or float and type(b) == int or float:
            return aux_xPower(abs(a), abs(b));
    else:
        return 'Argument must be integer or float';
    raise TypeError('Only digits are allowed as input')

def aux_xPower(a,b):
    if b == 0:
        return 1;
    elif b == 1:
        return a;
    else:
       return a * aux_xPower(a, b - 1)




			
			
			
			
			
			
			
	
	
