
from vsg.token import process_sensitivity_list as token

from vsg.vhdlFile.classify_new import sensitivity_list

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    process_sensitivity_list ::=
        all | sensitivity_list
    '''
    iToken = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iToken, 'all'):
        utils.assign_token(lObjects, iToken, token.all_keyword)
        iToken += 1
    else:
        sensitivity_list.classify(iToken, lObjects)
