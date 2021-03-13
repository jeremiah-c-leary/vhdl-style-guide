
from vsg.vhdlFile import utils

from vsg.token import case_generate_statement as token

from vsg.vhdlFile.classify import expression
from vsg.vhdlFile.classify import case_generate_alternative



def detect(iToken, lObjects):
    '''
        case_generate_statement ::=
            *generate*_label :
                case expression generate
                    case_generate_alternative
                    { case_generate_alternative }
                end generate [ *generate*_label ] ;
    '''

    if utils.are_next_consecutive_tokens([None, ':', 'case'], iToken, lObjects):
        return classify(iToken, lObjects)
    if utils.are_next_consecutive_tokens(['case'], iToken, lObjects):
        iIndex = utils.find_next_token(iToken, lObjects)
        oToken = token.case_keyword(lObjects[iToken].get_value())
        utils.print_error_message('generate_label', oToken, iIndex, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.generate_label, token.label_colon)

    iCurrent = utils.assign_next_token_required('case', token.case_keyword, iCurrent, lObjects)

    iCurrent = expression.classify_until(['generate'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('generate', token.generate_keyword, iCurrent, lObjects)

    iToken = utils.detect_submodule(iToken, lObjects, case_generate_alternative)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('generate', token.end_generate_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.end_generate_label, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
