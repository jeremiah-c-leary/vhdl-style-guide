
from vsg.vhdlFile.classify_new import context_item


def detect(iCurrent, lObjects):
    '''
    context_clause ::=
        { context_item }
    '''

    return context_item.detect(iCurrent, lObjects)
