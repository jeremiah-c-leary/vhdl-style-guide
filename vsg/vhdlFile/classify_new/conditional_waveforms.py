
from vsg import parser

from vsg.token import conditional_waveforms as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import waveform
from vsg.vhdlFile.classify_new import condition

'''
    conditional_waveforms ::=
        waveform when condition
        { else waveform when condition }
        [ else waveform ]
'''


def tokenize(iStart, iEnd, lAllObjects):
    for iToken in range(iStart, iEnd):
        if utils.is_item(lAllObjects, iToken):
            if utils.object_value_is(lAllObjects, iToken, 'when'):
                utils.assign_token(lAllObjects, iToken, token.when_keyword)
            elif utils.object_value_is(lAllObjects, iToken, 'else'):
                utils.assign_token(lAllObjects, iToken, token.else_keyword)
            else:
                utils.assign_token(lAllObjects, iToken, parser.todo)


def classify(iToken, lObjects):

    iStart, iEnd = utils.get_range(lObjects, iToken, ';')
    for iCurrent in range(iStart, iEnd):
        if utils.is_item(lObjects, iCurrent):
            if utils.object_value_is(lObjects, iCurrent, 'when'):
                iCurrent = utils.assign_token(lObjects, iCurrent, token.when_keyword)
            elif utils.object_value_is(lObjects, iCurrent, 'else'):
                Current = utils.assign_token(lObjects, iCurrent, token.else_keyword)
            else:
                iCurrent = utils.assign_token(lObjects, iCurrent, parser.todo)

    return iCurrent



def classify_until(lUntils, iToken, lObjects):

    lMyElseUntils = lUntils.copy()
    lMyElseUntils.append('else')
    lMyWhenUntils = lUntils.copy()
    lMyWhenUntils.append('when')

    iCurrent = waveform.classify_until(['when'], iToken, lObjects)
    iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
    iCurrent = condition.classify_until(lMyElseUntils, iCurrent, lObjects)

    while utils.is_next_token('else', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('else', token.else_keyword, iCurrent, lObjects)
        iCurrent = waveform.classify_until(lMyWhenUntils, iCurrent, lObjects)
        if lObjects[iCurrent].get_value() in lUntils:
            break
        iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
        iCurrent = condition.classify_until(lMyElseUntils, iCurrent, lObjects)

    return iCurrent
