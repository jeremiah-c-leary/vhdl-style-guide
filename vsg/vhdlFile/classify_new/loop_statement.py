
from vsg.token import loop_statement as token

from vsg.vhdlFile.classify_new import iteration_scheme
from vsg.vhdlFile.classify_new import sequence_of_statements

from vsg.vhdlFile import utils

'''
    loop_statement ::=
        [ loop_label : ]
            [ iteration_scheme ] loop
                sequence_of_statements
            end loop [ loop_label ] ;
'''


def detect(iToken, lObjects):
    if utils.find_in_next_n_tokens(':', 2, iToken, lObjects):
        iCurrent = utils.find_next_token(iToken, lObjects)
        iCurrent += 1
        iCurrent = utils.find_next_token(iToken, lObjects)
        iCurrent += 1
        if iteration_scheme.detect(iToken, lObjects):
            return classify(iToken, lObjects)
        if utils.is_next_token('loop', iToken, lObjects):
            return classify(iToken, lObjects)
        return iToken
    else:
        if iteration_scheme.detect(iToken, lObjects):
            return classify(iToken, lObjects)
        if utils.is_next_token('loop', iToken, lObjects):
            return classify(iToken, lObjects)
        return iToken
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.loop_label, token.label_colon)

    iCurrent = iteration_scheme.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('loop', token.loop_keyword, iToken, lObjects)

    iCurrent = sequence_of_statements.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('loop', token.end_loop_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.end_loop_label, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
