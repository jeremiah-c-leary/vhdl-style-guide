
from vsg.token import concurrent_assertion_statement as token

from vsg import parser

from vsg.vhdlFile.classify_new import assertion

from vsg.vhdlFile import utils

'''
    concurrent_assertion_statement ::=
        [ label : ] [ postponed ] assertion ;
'''


def detect(iCurrent, lObjects):
    '''
    concurrent_assertion_statement ::=
        [ label : ] [ postponed ] assertion ;
    '''

    if assertion.detect(iCurrent, lObjects):
        return classify(iCurrent, lObjects)
    return iCurrent


def classify(iCurrent, lObjects):
    iReturn = iCurrent
    iReturn = utils.tokenize_label(iReturn, lObjects, token.label_name, token.label_colon)
    iReturn = utils.tokenize_postponed(iReturn, lObjects, token.postponed_keyword)
    iReturn = assertion.tokenize(iReturn, lObjects)
    iReturn = utils.tokenize_semicolon(iReturn, lObjects, token.semicolon)
    return iReturn
