
from vsg.token import concurrent_procedure_call_statement as token

from vsg import parser

from vsg.vhdlFile.classify_new import procedure_call

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    concurrent_procedure_call_statement ::=
        [ label : ] [ postponed ] procedure_call ;
    '''
    iReturn = iCurrent
    if procedure_call.detect(iCurrent, lObjects):
        iReturn = utils.tokenize_label(iReturn, lObjects, token.label_name, token.label_colon)
        iReturn = utils.tokenize_postponed(iReturn, lObjects, token.postponed_keyword)
        iReturn = procedure_call.classify(iReturn, lObjects)
        iReturn = utils.assign_next_token_required(';', token.semicolon, iReturn, lObjects)

    return iReturn
