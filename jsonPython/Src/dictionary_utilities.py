'''
Created on Feb 15, 2020

@author: nicomp
'''
def iterate_dictionary(myDictionary):
    for k, v in myDictionary.items():
        print ("k is " + str(type(k)) + ", v is " + str(type(v)))
        if isinstance(v, dict):
            iterate_dictionary(v)
        else:
            print("{0} : {1}".format(k, v))
            if (isinstance(v, list)):
                for vv in v:
                    if (isinstance(vv, dict)):
                        iterate_dictionary(vv)
