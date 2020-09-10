
from vsg.token import process_sensitivity_list as token

from vsg.vhdlFile.classify_new import sensitivity_list

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    process_sensitivity_list ::=
        all | sensitivity_list
    '''
    if utils.is_next_token('all', iToken, lObjects):
        return utils.assign_next_token_required('all', token.all_keyword, iToken, lObjects)
    else:
        return sensitivity_list.classify(iToken, lObjects)
