
from vsg.token import procedure_call as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import actual_parameter_part


lExceptions = ['<=', 'end', 'map', 'component', 'entity', 'configuration', 'if']


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
            if lObjects[iCurrent].get_value().lower() in lExceptions:
                return False
        iCurrent += 1

    return True


def classify(iToken, lObjects):
    '''
    procedure_call ::=
        *procedure*_name [ ( actual_parameter_part ) ]
    '''

    iCurrent = utils.assign_next_token(token.procedure_name, iToken, lObjects)

    if utils.is_next_token('(', iToken, lObjects):
        iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)

        iCurrent = actual_parameter_part.classify(iCurrent, lObjects)

        iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)

    return iCurrent
