
from vsg.token import waveform_element as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import expression


def classify_until(lUntils, iToken, lObjects):
    '''
    waveform_element ::=
        *value*_expression [ after *time*_expression ]
      | null [ after *time*_expression ]
    '''

    if utils.is_next_token('null', iToken, lObjects):
        iCurrent = utils.assign_next_token_required('null', token.null_keyword, iToken, lObjects)
    else:
        lMyUntils = lUntils
        lMyUntils.append('after')
        iCurrent = expression.classify_until(lMyUntils, iToken, lObjects)

    if utils.is_next_token('after', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('after', token.after_keyword, iCurrent, lObjects)
        iCurrent = expression.classify_until(lUntils, iCurrent, lObjects)

    return iCurrent
