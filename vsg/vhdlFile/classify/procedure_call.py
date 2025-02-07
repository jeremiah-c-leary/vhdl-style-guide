# -*- coding: utf-8 -*-

from vsg.token import procedure_call as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import actual_parameter_part

lExceptions = ["<=", "end", "map", "component", "entity", "configuration", "if"]


def detect(oDataStructure):
    """
    Calling functions:

    concurrent_procedure_call_statement ::=
        [ label : ] [ postponed ] procedure_call ;

    procedure_call_statement ::=
        [ label : ] procedure_call ;

    --------------------------

    procedure_call ::=
        *procedure*_name [ ( actual_parameter_part ) ]

    Differentiating a procedure call from anything else is essentially the absence of keywords.
    """

    oDataStructure.align_seek_index()
    while not oDataStructure.seek_token_lower_value_is(";"):
        if oDataStructure.get_seek_token_lower_value() in lExceptions:
            return False
        oDataStructure.increment_seek_index()
        oDataStructure.advance_to_next_seek_token()
    return True


def classify(iToken, lObjects):
    """
    procedure_call ::=
        *procedure*_name [ ( actual_parameter_part ) ]
    """

    iCurrent = utils.assign_next_token(token.procedure_name, iToken, lObjects)

    if utils.is_next_token("(", iToken, lObjects):
        iCurrent = utils.assign_next_token_required("(", token.open_parenthesis, iCurrent, lObjects)

        iCurrent = actual_parameter_part.classify(iCurrent, lObjects)

        iCurrent = utils.assign_next_token_required(")", token.close_parenthesis, iCurrent, lObjects)

    return iCurrent
