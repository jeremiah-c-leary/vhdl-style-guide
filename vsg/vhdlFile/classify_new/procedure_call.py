
from vsg.token import procedure_call as token

from vsg.vhdlFile.classify_new import actual_parameter_part

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
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
    iToken = iCurrent

    while lObjects[iToken].get_value() != ';':
        if utils.is_item(lObjects, iToken):
            if lObjects[iToken].get_value() == '<=':
                return False
            if lObjects[iToken].get_value() == 'end':
                return False
        iToken += 1
    else:
        return True


def classify(iCurrent, lObjects):
    '''
    procedure_call ::=
        *procedure*_name [ ( actual_parameter_part ) ]
    '''
    iToken = iCurrent
    utils.find_next_token(iCurrent, lObjects)
    utils.assign_token(lObjects, iToken, token.procedure_name)
    iToken += 1

    iToken = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iToken, '('):
        utils.assign_token(lObjects, iToken, token.open_parenthesis)
        iToken += 1

        iToken = actual_parameter_part.classify(iToken, lObjects)

        iToken = utils.find_next_token(iToken, lObjects)
        utils.assign_token(lObjects, iToken, token.close_parenthesis)
        iToken += 1

    return iToken
