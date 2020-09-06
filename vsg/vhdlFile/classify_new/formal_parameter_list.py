
from vsg.vhdlFile.classify_new import interface_list

'''
    formal_parameter_list ::=
        *parameter*_interface_list
'''

def classify(iToken, lObjects):
    return interface_list.classify(iToken, lObjects)
