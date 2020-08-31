
from vsg import parser

from vsg.token import concurrent_selected_signal_assignment as token

from vsg.vhdlFile.classify_new import delay_mechanism
from vsg.vhdlFile.classify_new import selected_waveforms
from vsg.vhdlFile import utils


def detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''
    concurrent_selected_signal_assignment ::=
        with expression select [ ? ]
            target <= [ guarded ] [ delay_mechanism ] selected_waveforms ;

    The key to detecting this is looking for the **with** keyword before the **select** keyword.
    '''

    iToken = iObject
    bWithFound = False
    while lAllObjects[iToken].get_value() != ';':
        if utils.is_item(lAllObjects, iToken):
            if bWithFound:
                if utils.object_value_is(lAllObjects, iToken, 'select'):
                    return True
            if utils.object_value_is(lAllObjects, iToken, 'with'):
                bWithFound = True
        iToken += 1
    else:
        return False



def tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''
    concurrent_selected_signal_assignment ::=
        with expression select [ ? ]
            target <= [ guarded ] [ delay_mechanism ] selected_waveforms ;
    '''
    iStart, iCurrent, iEnd = utils.get_bounds(lAllObjects, iObject, ';')

    # Classify target and assignment operator
    for iToken, oObject in enumerate(lAllObjects[iStart:iEnd], start=iStart):
        if type(oObject) == parser.item:
            if oObject.get_value() == 'select':
                utils.assign_token(lAllObjects, iToken, token.select_keyword)
                break
            elif oObject.get_value() == 'with':
                utils.assign_token(lAllObjects, iToken, token.with_keyword)
            else:
                utils.assign_token(lAllObjects, iToken, parser.todo)

    # Classify target and assignment operator
    iCurrent = iToken
    for iToken, oObject in enumerate(lAllObjects[iCurrent:iEnd], start=iCurrent):
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
    selected_waveforms.tokenize(iToken, iEnd, lAllObjects)

    lAllObjects[iEnd] = token.semicolon()


