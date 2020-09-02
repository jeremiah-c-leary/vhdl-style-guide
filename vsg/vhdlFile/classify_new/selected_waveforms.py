
from vsg.token import selected_waveforms as token
from vsg import parser

from vsg.vhdlFile import utils


def tokenize(iStart, iEnd, lObjects):
    '''
    selected_waveforms ::=
        { waveform when choices , }
        waveform when choices
    '''
    for iToken in range(iStart, iEnd):
        if utils.is_item(lObjects, iToken):
            if utils.object_value_is(lObjects, iToken, 'when'):
                utils.assign_token(lObjects, iToken, token.when_keyword)
            elif utils.object_value_is(lObjects, iToken, ','):
                utils.assign_token(lObjects, iToken, token.comma)
            else:
                utils.assign_token(lObjects, iToken, parser.todo)
