
from vsg import parser

from vsg.token import waveform as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import waveform_element


def classify_until(lUntils, iToken, lObjects):
    '''
    waveform ::=
        waveform_element { , waveform_element }
      | unaffected
    '''

    if utils.is_next_token('unaffected', iToken, lObjects):
        return utils.assign_next_token_required('unaffected', token.unaffected_keyword, iToken, lObjects)

    iCurrent = iToken
    lMyUntils = lUntils
    lMyUntils.append(',')

    iCurrent = waveform_element.classify_until(lMyUntils, iCurrent, lObjects)

    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)
        iCurrent = waveform_element.classify_until(lMyUntils, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_if(')', parser.todo, iCurrent, lObjects)

    return iCurrent
