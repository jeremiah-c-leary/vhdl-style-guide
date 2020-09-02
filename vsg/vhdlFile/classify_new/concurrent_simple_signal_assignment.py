
from vsg import parser

from vsg.token import concurrent_simple_signal_assignment as token

from vsg.vhdlFile.classify_new import delay_mechanism
from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''

    [ label : ] [ postponed ] concurrent_simple_signal_assignment

    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;

    The key to detecting this is looking for an assignment <= followed by a semicolon.
    This will be the default if the other types are not found.
    '''

    iToken = iCurrent

    while lObjects[iToken].get_value() != ';':
        if utils.is_item(lObjects, iToken):
            if utils.object_value_is(lObjects, iToken, 'when'):
                return False
            if lObjects[iToken].get_value() == '<=':
                return True
        iToken += 1
    else:
        return False


def classify(iCurrent, lObjects):
    '''
    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;
    '''
    iStart, iEnd = utils.get_range(lObjects, iCurrent, ';')

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
    
    for iIndex in range(iToken, iEnd):
        if utils.is_item(lObjects, iIndex,):
            utils.assign_token(lObjects, iIndex, parser.todo)

    lObjects[iEnd] = token.semicolon()
    return iEnd

