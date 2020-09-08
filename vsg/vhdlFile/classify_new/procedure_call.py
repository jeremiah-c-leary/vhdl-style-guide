
from vsg.token import procedure_call as token

from vsg.vhdlFile.classify_new import actual_parameter_part

from vsg.vhdlFile import utils

lExceptions = ['<=', 'end', 'map', 'component', 'entity', 'configuration']

def detect(iToken, lObjects):
    '''
    Calling functions:

    concurrent_procedure_call_statement ::=
        [ label : ] [ postponed ] procedure_call ;

    procedure_call_statement ::=
        [ label : ] procedure_call ;

    --------------------------

    procedure_call ::=
        *procedure*_name [ ( actual_parameter_part ) ]

    Differentiating a procedure call from anything else is essentially the absence of keywords.
    '''
    iCurrent = iToken

    while lObjects[iCurrent].get_value() != ';':
        if utils.is_item(lObjects, iCurrent):
            if lObjects[iCurrent].get_value() in lExceptions:
                return False
        iCurrent += 1
    else:
        return True


def classify(iToken, lObjects):
    '''
    procedure_call ::=
        *procedure*_name [ ( actual_parameter_part ) ]
    '''
    iCurrent = utils.assign_token(lObjects, iToken, token.procedure_name)

    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, '('):
        iCurrent = utils.assign_token(lObjects, iCurrent, token.open_parenthesis)

        iCurrent = actual_parameter_part.classify(iCurrent, lObjects)

        iCurrent = utils.find_next_token(iCurrent, lObjects)
        iCurrent = utils.assign_token(lObjects, iCurrent, token.close_parenthesis)

    return iCurrent
