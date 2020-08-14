
from vsg.token import concurrent_conditional_signal_assignment as token

from vsg.vhdlFile.classify import delay_mechanism
from vsg.vhdlFile.classify import conditional_waveforms


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    concurrent_conditional_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] conditional_waveforms ;
    '''

    if dVars['conditional_waveforms']['when']:
        if classify_semicolon(oObject, iObject, lObjects, dVars):
            clear_flags(dVars)
            return True

    if delay_mechanism.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if conditional_waveforms.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == ';':
        lObjects[iObject] = token.semicolon()
        return True
    return False


def clear_flags(dVars):
    delay_mechanism.clear_flags(dVars)
    conditional_waveforms.clear_flags(dVars)
