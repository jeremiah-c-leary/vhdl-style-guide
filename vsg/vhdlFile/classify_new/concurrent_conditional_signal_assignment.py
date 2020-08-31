
from vsg import parser

from vsg.token import concurrent_conditional_signal_assignment as token
from vsg.token import conditional_waveforms

from vsg.vhdlFile.classify_new import delay_mechanism
from vsg.vhdlFile.classify_new import conditional_waveforms
from vsg.vhdlFile import utils


def detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''

    [ label : ] [ postponed ] concurrent_conditional_signal_assignment

    concurrent_conditional_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] conditional_waveforms ;

    conditional_waveforms ::=
        waveform when condition
        { else waveform when condition }
        [ else waveform ]

    The key to detecting this is looking for an assignment <= followed by the keyword **when** before a semicolon.
    '''

    iToken = iObject
    bAssignmentFound = False

    while lAllObjects[iToken].get_value() != ';':
        if utils.is_item(lAllObjects, iToken):
            if bAssignmentFound:
                if lAllObjects[iToken].get_value().lower() == 'when':
                    return True
            else:
                if lAllObjects[iToken].get_value().lower() == 'when':
                    return False
    
            if lAllObjects[iToken].get_value() == '<=' and not bAssignmentFound:
                bAssignmentFound = True
        iToken += 1
    else:
        return False



def tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''
    concurrent_conditional_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] conditional_waveforms ;
    '''
    iStart, iCurrent, iEnd = utils.get_bounds(lAllObjects, iObject, ';')

    # Classify target and assignment operator
    for iToken, oObject in enumerate(lAllObjects[iStart:iEnd], start=iStart):
        if type(oObject) == parser.item:
            if oObject.get_value() == '<=':
                utils.assign_token(lAllObjects, iToken, token.assignment)
                break
            else:
                utils.assign_token(lAllObjects, iToken, token.target)

    # Classify guarded keyword
    while type(lAllObjects[iToken]) != parser.item:
        iToken += 1
    else:
        if lAllObjects[iToken].get_value().lower() == 'guarded':
            lAllObjects[iToken] = token.guarded_keyword(lAllObjects[iToken].get_value())
            iToken += 1

    delay_mechanism.tokenize(iToken, iEnd, lAllObjects)
    conditional_waveforms.tokenize(iToken, iEnd, lAllObjects)

    lAllObjects[iEnd] = token.semicolon()


