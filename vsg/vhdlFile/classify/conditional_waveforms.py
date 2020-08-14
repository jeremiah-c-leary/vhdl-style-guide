
from vsg.token import conditional_waveforms as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    conditional_waveforms ::=
        waveform when condition
        { else waveform when condition }
        [ else waveform ]
    '''

    if classify_when_keyword(oObject, iObject, lObjects, dVars):
        return True

    if classify_else_keyword(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_when_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'when':
        lObjects[iObject] = token.when_keyword(sValue)
        dVars['conditional_waveforms']['when'] = True 
        return True
    return False


def classify_else_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'else':
        lObjects[iObject] = token.else_keyword(sValue)
        return True
    return False


def clear_flags(dVars):
    dVars['conditional_waveforms']['when'] = False
