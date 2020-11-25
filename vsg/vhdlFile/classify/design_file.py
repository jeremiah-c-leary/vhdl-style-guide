
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import design_unit


def tokenize(lObjects):
    '''
    design_file ::=
        design_unit { design_unit }
    '''
    iReturn = 0
    for iCurrent in range(0, len(lObjects)):
        iTemp = iCurrent
        if iTemp >= iReturn:
            if utils.is_item(lObjects, iTemp):
                iReturn = design_unit.detect(iTemp, lObjects)
