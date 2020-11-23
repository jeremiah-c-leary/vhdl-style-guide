
from vsg.vhdlFile.classify import interface_list


def classify(iToken, lObjects):
    '''
    formal_parameter_list ::=
        *parameter*_interface_list
    '''

    return interface_list.classify(iToken, lObjects)
