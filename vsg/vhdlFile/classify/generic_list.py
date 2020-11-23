
from vsg.vhdlFile.classify import interface_list


def classify(iToken, lObjects):
    '''
    generic_list ::=
        *generic*_interface_list
    '''

    return interface_list.classify(iToken, lObjects)
