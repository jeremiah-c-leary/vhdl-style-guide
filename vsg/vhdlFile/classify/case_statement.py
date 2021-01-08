
from vsg.token import case_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import case_statement_alternative
from vsg.vhdlFile.classify import expression


def detect(iToken, lObjects):
    '''
    case_statement ::=
        [ *case*_label : ]
            case [ ? ] expression is
                case_statement_alternative
                { case_statement_alternative }
        end case [ ? ] [ case_label ] ;
    '''
    if utils.keyword_found('case', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.case_label, token.label_colon)
    iCurrent = utils.assign_next_token_required('case', token.case_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('?', token.question_mark, iCurrent, lObjects)

    iCurrent = expression.classify_until(['is'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)

    iCurrent = utils.detect_submodule(iCurrent, lObjects, case_statement_alternative)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('case', token.end_case_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('?', token.question_mark, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.end_case_label, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
