
from vsg.token import entity_designator as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import signature


def classify(iToken, lObjects):
    '''
    entity_designator ::=
        entity_tag [ signature ]
    '''

    iCurrent = utils.assign_next_token(token.entity_tag, iToken, lObjects)

    iCurrent = signature.detect(iCurrent, lObjects)

    return iCurrent
