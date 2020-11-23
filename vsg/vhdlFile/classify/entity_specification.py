
from vsg.token import entity_specification as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import entity_name_list


def classify(iToken, lObjects):
    '''
    entity_specification ::=
        entity_name_list : entity_class
    '''

    iCurrent = entity_name_list.classify(iToken, lObjects)

    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)

    iCurrent = utils.assign_next_token(token.entity_class, iCurrent, lObjects)

    return iCurrent
