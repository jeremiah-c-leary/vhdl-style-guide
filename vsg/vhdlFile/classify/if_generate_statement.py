
from vsg.token import if_generate_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import condition
from vsg.vhdlFile.classify import generate_statement_body


def detect(iToken, lObjects):
    '''
    if_generate_statement ::=
        *generate*_label :
            if [ *alternative*_label : ] condition generate
                generate_statement_body
            { elsif [ *alternative_label* : ] condition generate
                generate_statement_body }
            [ else [ *alternative_label* : ] generate
                generate_statement_body ]
            end generate [ *generate*_label ] ;
    '''

    if utils.are_next_consecutive_tokens([None, ':', 'if'], iToken, lObjects):
        return classify(iToken, lObjects)
    if utils.are_next_consecutive_tokens(['if'], iToken, lObjects):
        iIndex = utils.find_next_token(iToken, lObjects)
        oToken = token.if_keyword(lObjects[iToken].get_value())
        utils.print_error_message('generate_label', oToken, iIndex, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.tokenize_label(iToken, lObjects, token.generate_label, token.label_colon)

    iCurrent = utils.assign_next_token_required('if', token.if_keyword, iCurrent, lObjects)

    ### Need to handle alternaive_label ###

    iCurrent = condition.classify_until(['generate'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('generate', token.generate_keyword, iCurrent, lObjects)

    iCurrent = generate_statement_body.classify(iCurrent, lObjects)

    while utils.is_next_token('elsif', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('elsif', token.elsif_keyword, iCurrent, lObjects)

        iCurrent = condition.classify_until(['generate'], iCurrent, lObjects)

        iCurrent = utils.assign_next_token_required('generate', token.generate_keyword, iCurrent, lObjects)

        iCurrent = generate_statement_body.classify(iCurrent, lObjects)

    if utils.is_next_token('else', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('else', token.else_keyword, iCurrent, lObjects)

        iCurrent = utils.assign_next_token_required('generate', token.generate_keyword, iCurrent, lObjects)

        iCurrent = generate_statement_body.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('generate', token.end_generate_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.end_generate_label, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
