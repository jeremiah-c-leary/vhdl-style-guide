
from vsg.token import constant_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import expression
from vsg.vhdlFile.classify_new import identifier
from vsg.vhdlFile.classify_new import subtype_indication


'''
    constant_declaration ::=
        constant identifier_list : subtype_indication [ := expression ] ;
'''


def detect(iToken, lObjects):

    if utils.is_next_token('constant', iToken, lObjects):
        return classify(iToken, lObjects)    

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('constant', token.constant_keyword, iToken, lObjects)
    iCurrent = identifier.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)
    sEnd = utils.find_earliest_occurance([';', ':='], iCurrent, lObjects)
    iCurrent = utils.classify_subelement_until(sEnd, subtype_indication, iCurrent, lObjects) 
    if utils.is_next_token(':=', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(':=', token.assignment_operator, iCurrent, lObjects)
        iCurrent = utils.classify_subelement_until(';', expression, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent 
