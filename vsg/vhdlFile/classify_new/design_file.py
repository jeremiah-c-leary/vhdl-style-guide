
from vsg.vhdlFile.classify_new import design_unit

from vsg.vhdlFile import utils


def tokenize(lObjects):
    '''
    design_file ::= 
        design_unit { design_unit }
    '''
    for iCurrent in range(0, len(lObjects)):
        if utils.is_item(lObjects, iCurrent):
            iCurrent = design_unit.detect(iCurrent, lObjects)
        else:
            iCurrent += 1
