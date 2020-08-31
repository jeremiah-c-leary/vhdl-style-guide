
from vsg.token import selected_waveforms as token
from vsg import parser

from vsg.vhdlFile import utils


def tokenize(iStart, iEnd, lAllObjects):
    '''
    selected_waveforms ::=
        { waveform when choices , }
        waveform when choices
    '''
    for iToken in range(iStart, iEnd):
        if utils.is_item(lAllObjects, iToken):
            if utils.object_value_is(lAllObjects, iToken, 'when'):
                utils.assign_token(lAllObjects, iToken, token.when_keyword)
            elif utils.object_value_is(lAllObjects, iToken, ','):
                utils.assign_token(lAllObjects, iToken, token.comma)
            else:
                utils.assign_token(lAllObjects, iToken, parser.todo)
