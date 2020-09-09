
from vsg.token import entity_designator as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import signature

'''
    entity_designator ::=
        entity_tag [ signature ]
'''


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token(token.entity_tag, iToken, lObjects)
    iCurrent = signature.detect(iCurrent, lObjects)
    return iCurrent 
