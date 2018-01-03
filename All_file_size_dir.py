##Load all Modules
import humansize as hs
import os
import glob

## List Comprehension
file_list_gre_than_6k = [(file,hs.human_size_test(os.stat(file).st_size)) for file in glob.glob("*.*") if os.stat(file).st_size > 6000]
file_list_gre_than_6k = {file:hs.human_size_test(os.stat(file).st_size) for file in glob.glob("*.*") if os.stat(file).st_size > 6000}
