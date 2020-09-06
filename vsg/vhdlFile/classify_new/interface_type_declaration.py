

from vsg.vhdlFile.classify_new import interface_incomplete_type_declaration

'''
    interface_type_declaration ::=
        interface_incomplete_type_declaration
'''


def detect(iToken, lObjects):
    return interface_incomplete_type_declaration.detect(iToken, lObjects)
