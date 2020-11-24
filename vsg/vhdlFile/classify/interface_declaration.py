
from vsg.vhdlFile.classify import interface_object_declaration
from vsg.vhdlFile.classify import interface_package_declaration
from vsg.vhdlFile.classify import interface_subprogram_declaration
from vsg.vhdlFile.classify import interface_type_declaration


def detect(iToken, lObjects):
    '''
    interface_declaration ::=
        interface_object_declaration
      | interface_type_declaration
      | interface_subprogram_declaration
      | interface_package_declaration
    '''

    iCurrent = interface_object_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = interface_type_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = interface_subprogram_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = interface_package_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
