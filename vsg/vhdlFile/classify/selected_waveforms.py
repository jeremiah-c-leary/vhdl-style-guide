
from vsg.token import selected_waveforms as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    selected_waveforms ::=
        { waveform when choices , }
        waveform when choices
    '''

    if classify_when_keyword(oObject, iObject, lObjects, dVars):
        return True

    if classify_comma(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_when_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'when':
        lObjects[iObject] = token.when_keyword(sValue)
        dVars['selected_waveforms']['when'] = True 
        return True
    return False


def classify_comma(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == ',':
        lObjects[iObject] = token.comma()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['selected_waveforms']['when'] = False
