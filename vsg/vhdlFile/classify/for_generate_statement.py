
from vsg.vhdlFile import utils

from vsg.token import for_generate_statement as token

from vsg.vhdlFile.classify import parameter_specification
from vsg.vhdlFile.classify import generate_statement_body


def detect(iToken, lObjects):
    '''
    for_generate_statement ::=
        *generate*_label :
            for *generate*_parameter_specification generate
                generate_statement_body
            end generate [ *generate*_label ] ;
    '''

    if utils.are_next_consecutive_tokens([None, ':', 'for'], iToken, lObjects):
        return classify(iToken, lObjects)
    if utils.are_next_consecutive_tokens(['for'], iToken, lObjects):
        iIndex = utils.find_next_token(iToken, lObjects)
        oToken = token.for_keyword(lObjects[iToken].get_value())
        utils.print_error_message('generate_label', oToken, iIndex, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.generate_label, token.label_colon)

    iCurrent = utils.assign_next_token_required('for', token.for_keyword, iCurrent, lObjects)

    iCurrent = parameter_specification.classify_until(['generate'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('generate', token.generate_keyword, iCurrent, lObjects)

    iCurrent = generate_statement_body.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('generate', token.end_generate_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.end_generate_label, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
