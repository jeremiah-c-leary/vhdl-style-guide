
from vsg.token import record_type_definition as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import element_declaration


def detect(iToken, lObjects):
    '''
    record_type_definition ::=
        record
            element_declaration
            { element_declaration }
        end record [ *record_type*_simple_name ]
    '''

    if utils.is_next_token('record', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('record', token.record_keyword, iToken, lObjects)

    iCurrent = utils.classify_subelement_until('end', element_declaration, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('record', token.end_record_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.record_type_simple_name, iCurrent, lObjects)

    return iCurrent
