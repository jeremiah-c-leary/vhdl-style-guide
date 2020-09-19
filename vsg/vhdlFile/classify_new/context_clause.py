
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import context_item


def detect(iToken, lObjects):
    '''
    context_clause ::=
        { context_item }
    '''
    iCurrent = utils.detect_submodule(iToken, lObjects, context_item)
    return iCurrent
