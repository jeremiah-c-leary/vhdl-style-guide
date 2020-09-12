
from vsg.token import procedure_call_statement as token

from vsg.vhdlFile.classify_new import procedure_call

from vsg.vhdlFile import utils

lKeywords = ['null', 'return', 'exit', 'next', 'while', 'for', 'loop', 'case', 'if', 'report', 'assert', 'wait', 'end']

'''
    procedure_call_statement ::=
        [ label : ] procedure_call ;
'''

def detect(iToken, lObjects):
    iCurrent = iToken
    # Move past label if it exists
    if utils.find_in_next_n_tokens(':', 2, iCurrent, lObjects):
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        iCurrent +=1
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        iCurrent +=1
    # Check if next token is keyword
    iCurrent = utils.find_next_token(iCurrent, lObjects)
    if lObjects[iCurrent].get_value() in lKeywords:
        return iToken
    # Check if signal assignment operator exists
    if utils.find_in_range('<=', iCurrent, ';', lObjects):
        return iToken
    # Check if variable assignment operator exists
    if utils.find_in_range(':=', iCurrent, ';', lObjects):
        return iToken
    # Otherwise it must be a procedure_call_statement
    return classify(iToken, lObjects)


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)

    iCurrent = procedure_call.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
