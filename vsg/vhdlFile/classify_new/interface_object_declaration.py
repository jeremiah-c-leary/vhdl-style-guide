
from vsg.vhdlFile.classify_new import interface_constant_declaration
from vsg.vhdlFile.classify_new import interface_file_declaration
from vsg.vhdlFile.classify_new import interface_signal_declaration
from vsg.vhdlFile.classify_new import interface_unknown_declaration
from vsg.vhdlFile.classify_new import interface_variable_declaration

from vsg.vhdlFile import utils

'''
    interface_object_declaration ::=
        interface_constant_declaration
      | interface_signal_declaration
      | interface_variable_declaration
      | interface_file_declaration
'''

def detect(iCurrent, lObjects):

    iReturn = interface_constant_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = interface_signal_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = interface_variable_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = interface_file_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    ### This capture constant, signal and variable declarations without optional keywords
    iReturn = interface_unknown_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    return iCurrent
