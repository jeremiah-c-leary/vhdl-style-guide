
#from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import interface_list

'''
    generic_list ::=
        generic_interface_list
'''


def classify(iToken, lObjects):
    return interface_list.classify(iToken, lObjects)
