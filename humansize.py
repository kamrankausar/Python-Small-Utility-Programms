# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:40:20 2017

@author: genius
"""

# Define the Dictonary
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'Gib', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# Define the function

def approx_size(size, a_1024 = True):
    ''' Convert a file size to human-readable form.
    Key arguments:
    size -- file size in bytes
    a_1024 -- if True (default), use multiple of 1024
              if false, use multiple of 1000
    return : string
    '''
    if size < 0:
        raise ValueError('Number must be negative')
        
    multiple = 1024 if a_1024 else 1000
    for suffix in SUFFIXES[multiple]:
       size /= multiple
       if size < multiple:
           return '{0:.1f} {1}'.format(size,suffix)
         
    raise ValueError('Number too Large')
    
if __name__ == '__main__':
    print(approx_size(10000000000,False))
    print(approx_size(10000000000))
    
