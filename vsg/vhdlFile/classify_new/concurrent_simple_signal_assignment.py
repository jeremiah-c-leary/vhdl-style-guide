
from vsg import parser

from vsg.token import concurrent_simple_signal_assignment as token

from vsg.vhdlFile.classify_new import delay_mechanism
from vsg.vhdlFile import utils


def detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''

    [ label : ] [ postponed ] concurrent_simple_signal_assignment

    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;

    The key to detecting this is looking for an assignment <= followed by a semicolon.
    This will be the default if the other types are not found.
    '''

    iToken = iObject

    while lAllObjects[iToken].get_value() != ';':
        if utils.is_item(lAllObjects, iToken):
            if utils.object_value_is(lAllObjects, iToken, 'when'):
                return False
            if lAllObjects[iToken].get_value() == '<=':
                return True
        iToken += 1
    else:
        return False



def tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''
    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;
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
    
    for iIndex in range(iToken, iEnd):
        if utils.is_item(lAllObjects, iIndex,):
            utils.assign_token(lAllObjects, iIndex, parser.todo)

    lAllObjects[iEnd] = token.semicolon()


