
from vsg.vhdlFile import utils

from vsg.token import component_specification as token

from vsg.vhdlFile.classify import instantiation_list


def classify(iToken, lObjects):
    '''
    component_specification ::=
        instantiation_list : component_name
    '''

    iCurrent = iToken

    iCurrent = instantiation_list.classify(iToken, lObjects)

    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.component_name, iCurrent, lObjects)

    return iCurrent
