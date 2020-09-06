
#from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import interface_declaration

'''
    interface_element ::=
        interface_declaration
'''


def classify(iToken, lObjects):
    return interface_declaration.detect(iToken, lObjects)
