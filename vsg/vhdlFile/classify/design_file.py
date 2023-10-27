
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import design_unit


def tokenize(lObjects):
    '''
    design_file ::=
        design_unit { design_unit }
    '''
#    print('--> design_file')
#    iReturn = 0
#    for iCurrent in range(0, len(lObjects)):
#        print(f'iCurrent = {iCurrent}::{iReturn}::{lObjects[iCurrent]}')
#        if iCurrent >= iReturn:
#            if utils.is_item(lObjects, iCurrent):
#                iReturn = design_unit.detect(iCurrent, lObjects)
#                print(f'iReturn = {iReturn}::{len(lObjects)}')
    iCurrent = 0;
    while iCurrent < len(lObjects):
        iReturn = design_unit.detect(iCurrent, lObjects)
        if iReturn == iCurrent:
            iCurrent += 1
        else:
            iCurrent = iReturn

#    print(lObjects[iCurrent::])
#    print('<-- design_file')
