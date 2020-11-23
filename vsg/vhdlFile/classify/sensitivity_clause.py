
from vsg.token import sensitivity_clause as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import sensitivity_list


def detect(iToken, lObjects):
    '''
    sensitivity_clause ::=
        on sensitivity_list
    '''

    if utils.is_next_token('on', iToken, lObjects):
        return True
    return False


def classify_until(lUntils, iToken, lObjects):

    iCurrent = utils.assign_next_token_required('on', token.on_keyword, iToken, lObjects)

    iCurrent = sensitivity_list.classify_until(lUntils, iCurrent, lObjects)

    return iCurrent
