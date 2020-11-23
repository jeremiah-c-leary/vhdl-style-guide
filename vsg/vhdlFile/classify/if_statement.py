
from vsg.token import if_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import condition
from vsg.vhdlFile.classify import sequence_of_statements


def detect(iToken, lObjects):
    '''
    if_statement ::=
        [ if_label : ]
            if condition then
                sequence_of_statements
            { elsif condition then
                sequence_of_statements }
            [ else
                sequence_of_statements ]
            end if [ if_label ] ;
    '''

    if utils.keyword_found('if', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.if_label, token.label_colon)
    iCurrent = utils.assign_next_token_required('if', token.if_keyword, iCurrent, lObjects)
    iCurrent = condition.classify_until(['then'], iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('then', token.then_keyword, iCurrent, lObjects)

    iCurrent = sequence_of_statements.detect(iCurrent, lObjects)

    while utils.is_next_token_one_of(['else', 'elsif'], iCurrent, lObjects):
        if utils.is_next_token('elsif', iCurrent, lObjects):
            iCurrent = utils.assign_next_token_required('elsif', token.elsif_keyword, iCurrent, lObjects)
            iCurrent = condition.classify_until(['then'], iCurrent, lObjects)
            iCurrent = utils.assign_next_token_required('then', token.then_keyword, iCurrent, lObjects)
            iCurrent = sequence_of_statements.detect(iCurrent, lObjects)
        else:
            iCurrent = utils.assign_next_token_required('else', token.else_keyword, iCurrent, lObjects)
            iCurrent = sequence_of_statements.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('if', token.end_if_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.end_if_label, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent
