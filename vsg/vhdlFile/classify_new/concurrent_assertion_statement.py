
from vsg.token import concurrent_assertion_statement as token

from vsg import parser

from vsg.vhdlFile.classify_new import assertion

from vsg.vhdlFile import utils

'''
    concurrent_assertion_statement ::=
        [ label : ] [ postponed ] assertion ;

    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]

'''


def detect(iToken, lObjects):
    '''
    concurrent_assertion_statement ::=
        [ label : ] [ postponed ] assertion ;
    '''
    if utils.find_in_next_n_tokens('assert', 4, iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iReturn = iToken
    iReturn = utils.tokenize_label(iReturn, lObjects, token.label_name, token.label_colon)
    iReturn = utils.assign_next_token_if('postponed', token.postponed_keyword, iReturn, lObjects)
    iReturn = assertion.classify(iReturn, lObjects)
    iReturn = utils.assign_next_token_required(';', token.semicolon, iReturn, lObjects)
    return iReturn
