
from vsg.token import case_statement_alternative as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import choices
from vsg.vhdlFile.classify import sequence_of_statements


def detect(iToken, lObjects):
    '''
    case_statement_alternative ::=
        when choices =>
            sequence_of_statements
    '''
    if utils.is_next_token('when', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('when', token.when_keyword, iToken, lObjects)

    iCurrent = choices.classify_until(['=>'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('=>', token.assignment, iCurrent, lObjects)

    iCurrent = sequence_of_statements.detect(iCurrent, lObjects)

    return iCurrent
