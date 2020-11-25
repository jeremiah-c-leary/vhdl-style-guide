
from vsg.token import concurrent_assertion_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import assertion


def detect(iToken, lObjects):
    '''
    concurrent_assertion_statement ::=
        [ label : ] [ postponed ] assertion ;

    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]

    '''

    if utils.find_in_next_n_tokens('assert', 4, iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.label_name, token.label_colon)

    iCurrent = utils.assign_next_token_if('postponed', token.postponed_keyword, iCurrent, lObjects)

    iCurrent = assertion.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
