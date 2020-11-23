
from vsg.token import subprogram_body as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import subprogram_declarative_part
from vsg.vhdlFile.classify import subprogram_kind
from vsg.vhdlFile.classify import subprogram_statement_part


def detect(iToken, lObjects):
    '''
    subprogram_body ::=
        subprogram_specification is
            subprogram_declarative_part
        begin
            subprogram_statement_part
        end [ subprogram_kind ] [ designator ] ;
    '''

    if utils.is_next_token('is', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iToken, lObjects)

    iCurrent = subprogram_declarative_part.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('begin', token.begin_keyword, iCurrent, lObjects)

    iCurrent = subprogram_statement_part.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)

    if subprogram_kind.detect(iCurrent, lObjects):
        iCurrent = subprogram_kind.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_if_not(';', token.designator, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
