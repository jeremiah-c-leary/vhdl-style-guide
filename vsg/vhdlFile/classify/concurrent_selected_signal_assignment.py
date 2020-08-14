
from vsg import parser

from vsg.token import concurrent_selected_signal_assignment as token

from vsg.vhdlFile.classify import delay_mechanism
from vsg.vhdlFile.classify import selected_waveforms


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    concurrent_selected_signal_assignment ::=
        with expression select [ ? ]
            target <= [ guarded ] [ delay_mechanism ] selected_waveforms ;
    '''

    if not dVars['concurrent_selected_signal_assignment']['with']:

        if classify_with_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['concurrent_selected_signal_assignment']['select']:

            if classify_select_keyword(oObject, iObject, lObjects, dVars):
                return True

        else:

            if not dVars['concurrent_selected_signal_assignment']['assignment']:

                if classify_assignment(oObject, iObject, lObjects, dVars):
                    return True

                if classify_target(oObject, iObject, lObjects, dVars):
                    return True

            else:

                if classify_semicolon(oObject, iObject, lObjects, dVars):
                    return True
    
                if classify_guarded_keyword(oObject, iObject, lObjects, dVars):
                    return True
    
                if delay_mechanism.tokenize(oObject, iObject, lObjects, dVars):
                    return True
            
                if selected_waveforms.tokenize(oObject, iObject, lObjects, dVars):
                    return True

    return False


def classify_with_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'with':
        lObjects[iObject] = token.with_keyword(sValue)
        dVars['concurrent_selected_signal_assignment']['with'] = True
        return True
    return False


def classify_select_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'select':
        lObjects[iObject] = token.select_keyword(sValue)
        dVars['concurrent_selected_signal_assignment']['select'] = True
        return True
    return False


def classify_assignment(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == '<=':
        lObjects[iObject] = token.assignment(sValue)
        dVars['concurrent_selected_signal_assignment']['assignment'] = True
        return True
    return False


def classify_target(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item:
        lObjects[iObject] = token.target(sValue)
        return True
    return False


def classify_guarded_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'guarded':
        lObjects[iObject] = token.guarded_keyword(sValue)
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['concurrent_selected_signal_assignment']['with'] = False
    dVars['concurrent_selected_signal_assignment']['select'] = False
    dVars['concurrent_selected_signal_assignment']['assignment'] = False
    delay_mechanism.clear_flags(dVars)
    selected_waveforms.clear_flags(dVars)
