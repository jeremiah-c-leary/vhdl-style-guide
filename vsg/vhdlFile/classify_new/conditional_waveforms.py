
from vsg.token import conditional_waveforms as token
from vsg import parser

from vsg.vhdlFile import utils


def tokenize(iStart, iEnd, lAllObjects):
    '''
    conditional_waveforms ::=
        waveform when condition
        { else waveform when condition }
        [ else waveform ]
    '''
    for iToken in range(iStart, iEnd):
        if utils.is_item(lAllObjects, iToken):
            if utils.object_value_is(lAllObjects, iToken, 'when'):
                utils.assign_token(lAllObjects, iToken, token.when_keyword)
            elif utils.object_value_is(lAllObjects, iToken, 'else'):
                utils.assign_token(lAllObjects, iToken, token.else_keyword)
            else:
                utils.assign_token(lAllObjects, iToken, parser.todo)


def classify(iToken, lObjects):
    '''
    conditional_waveforms ::=
        waveform when condition
        { else waveform when condition }
        [ else waveform ]
    '''
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
