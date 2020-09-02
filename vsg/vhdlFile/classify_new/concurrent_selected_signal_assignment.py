
from vsg import parser

from vsg.token import concurrent_selected_signal_assignment as token

from vsg.vhdlFile.classify_new import delay_mechanism
from vsg.vhdlFile.classify_new import selected_waveforms
from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    concurrent_selected_signal_assignment ::=
        with expression select [ ? ]
            target <= [ guarded ] [ delay_mechanism ] selected_waveforms ;

    The key to detecting this is looking for the **with** keyword before the **select** keyword.
    '''

    iToken = iCurrent
    bWithFound = False
    while lObjects[iToken].get_value() != ';':
        if utils.is_item(lObjects, iToken):
            if bWithFound:
                if utils.object_value_is(lObjects, iToken, 'select'):
                    return True
            if utils.object_value_is(lObjects, iToken, 'with'):
                bWithFound = True
        iToken += 1
    else:
        return False


def classify(iCurrent, lObjects):
    '''
    concurrent_selected_signal_assignment ::=
        with expression select [ ? ]
            target <= [ guarded ] [ delay_mechanism ] selected_waveforms ;
    '''
    iStart, iEnd = utils.get_range(lObjects, iCurrent, ';')

    # Classify target and assignment operator
    for iToken, oObject in enumerate(lObjects[iStart:iEnd], start=iStart):
        if type(oObject) == parser.item:
            if oObject.get_value() == 'select':
                utils.assign_token(lObjects, iToken, token.select_keyword)
                break
            elif oObject.get_value() == 'with':
                utils.assign_token(lObjects, iToken, token.with_keyword)
            else:
                utils.assign_token(lObjects, iToken, parser.todo)

    # Classify target and assignment operator
    iCurrent = iToken
    for iToken, oObject in enumerate(lObjects[iCurrent:iEnd], start=iCurrent):
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
    selected_waveforms.tokenize(iToken, iEnd, lObjects)

    lObjects[iEnd] = token.semicolon()

    return iEnd
