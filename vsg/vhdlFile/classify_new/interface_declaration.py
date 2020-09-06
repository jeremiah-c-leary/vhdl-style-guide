
from vsg.vhdlFile.classify_new import interface_object_declaration
from vsg.vhdlFile.classify_new import interface_type_declaration
from vsg.vhdlFile.classify_new import interface_subprogram_declaration
from vsg.vhdlFile.classify_new import interface_package_declaration

from vsg.vhdlFile import utils

'''
    interface_declaration ::=
        interface_object_declaration
      | interface_type_declaration
      | interface_subprogram_declaration
      | interface_package_declaration
'''

def detect(iCurrent, lObjects):

    iReturn = interface_object_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = interface_type_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = interface_subprogram_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = interface_package_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    return iCurrent
