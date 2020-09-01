
from vsg.vhdlFile.classify_new import use_clause


def detect(iCurrent, lObjects):
    '''
    context_item ::=
        library_clause
      | use_clause
      | context_reference
    '''
    iReturn = use_clause.detect(iCurrent, lObjects)

    return iReturn
