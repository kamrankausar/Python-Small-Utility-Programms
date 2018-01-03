# -*- coding: utf-8 -*-
"""


@author: genius
"""
#// format of the String
user_Id = "Kamran"
password = "password"

print("{0}'s password is {1}".format(user_Id, password))

print("{0:.1f} {1}".format(345.567,'GB'))

#  Common String methods

s = "'Sir/Ma'am, My my parents moved to the city(Delhi) from village (Damodarpur,Bihar) "
s.lower()
s.lower().count('my')


#//// Convert result from Query 

query = "user=kamran&server=master&password=abc"
a_list = query.split("&")
a_list
a_list_lists = [v.split("=", 1) for v in a_list]
a_dict = dict(a_list_lists)
a_dict