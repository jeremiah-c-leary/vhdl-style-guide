
from vsg.token import instantiation_list as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    instantiation_list ::=
        instantiation_label { , instantiation_label }
      | **others**
      | **all**
    '''

    if utils.is_next_token('others', iToken, lObjects):
        return utils.assign_next_token_required('others', token.others_keyword, iToken, lObjects)

    if utils.is_next_token('all', iToken, lObjects):
        return utils.assign_next_token_required('all', token.all_keyword, iToken, lObjects)

    iCurrent = utils.assign_next_token(token.instantiation_label, iToken, lObjects)

    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iToken, lObjects)
        iCurrent = utils.assign_next_token(token.instantiation_label, iToken, lObjects)

    return iCurrent
