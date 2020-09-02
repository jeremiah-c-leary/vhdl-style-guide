
from vsg import parser

from vsg.token import concurrent_conditional_signal_assignment as token
from vsg.token import conditional_waveforms

from vsg.vhdlFile.classify_new import delay_mechanism
from vsg.vhdlFile.classify_new import conditional_waveforms
from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
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

    iToken = iCurrent
    bAssignmentFound = False

    while lObjects[iToken].get_value() != ';':
        if utils.is_item(lObjects, iToken):
            if bAssignmentFound:
                if utils.object_value_is(lObjects, iToken, 'when'):
                    return True
            else:
                if utils.object_value_is(lObjects, iToken, 'when'):
                    return False
    
            if utils.object_value_is(lObjects, iToken, '<=') and not bAssignmentFound:
                bAssignmentFound = True
        iToken += 1
    else:
        return False


def classify(iObject, lObjects):
    '''
    concurrent_conditional_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] conditional_waveforms ;
    '''
    iStart, iCurrent, iEnd = utils.get_bounds(lObjects, iObject, ';')

    # Classify target and assignment operator
    for iToken, oObject in enumerate(lObjects[iStart:iEnd], start=iStart):
        if type(oObject) == parser.item:
            if oObject.get_value() == '<=':
                utils.assign_token(lObjects, iToken, token.assignment)
                break
            else:
                utils.assign_token(lObjects, iToken, token.target)

    # Classify guarded keyword
    while type(lObjects[iToken]) != parser.item:
        iToken += 1
    else:
        if lObjects[iToken].get_value().lower() == 'guarded':
            lObjects[iToken] = token.guarded_keyword(lObjects[iToken].get_value())
            iToken += 1

    iToken = delay_mechanism.detect(iToken, iEnd, lObjects)
    conditional_waveforms.tokenize(iToken, iEnd, lObjects)

    lObjects[iEnd] = token.semicolon()
    return iEnd
