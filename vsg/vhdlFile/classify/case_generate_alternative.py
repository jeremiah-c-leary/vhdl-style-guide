
from vsg.token import case_generate_alternative as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import choices
from vsg.vhdlFile.classify import generate_statement_body


def detect(iToken, lObjects):
    '''
    case_generate_alternative ::=
        when [ alternative_label : ] choices =>
            generate_statement_body
    '''

    if utils.is_next_token('when', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('when', token.when_keyword, iToken, lObjects)

    iCurrent = choices.classify_until(['=>'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('=>', token.assignment, iToken, lObjects)

    iCurrent = generate_statement_body.classify(iCurrent, lObjects)

    return iCurrent
