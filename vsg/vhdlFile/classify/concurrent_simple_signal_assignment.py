
from vsg.token import concurrent_simple_signal_assignment as token

from vsg.vhdlFile.classify import delay_mechanism


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;
    '''

    if classify_semicolon(oObject, iObject, lObjects, dVars):
        return True

    if delay_mechanism.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == ';':
        lObjects[iObject] = token.semicolon()
        return True
    return False


def clear_flags(dVars):
    concurrent_simple_signal_assignment.clear_flags(dVars)
