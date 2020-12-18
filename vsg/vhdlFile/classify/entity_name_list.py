
from vsg.token import entity_name_list as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import entity_designator


def classify(iToken, lObjects):
    '''
    entity_name_list ::=
        entity_designator { , entity_designator }
      | others
      | all
    '''

    if utils.is_next_token('others', iToken, lObjects):

        return utils.assign_next_token_required('others', token.others_keyword, iToken, lObjects)

    elif utils.is_next_token('all', iToken, lObjects):

        return utils.assign_next_token_required('all', token.all_keyword, iToken, lObjects)

    else:

        iCurrent = entity_designator.classify(iToken, lObjects)

        while utils.is_next_token(',', iCurrent, lObjects):

            iCurrent = utils.assign_next_token_required(',', token.comma, iToken, lObjects)

            entity_designator.classify(iToken, lObjects)

    return iCurrent
