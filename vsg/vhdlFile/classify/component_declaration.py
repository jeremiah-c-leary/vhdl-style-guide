
from vsg.token import component_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import generic_clause
from vsg.vhdlFile.classify import port_clause



def detect(iToken, lObjects):
    '''
    component_declaration ::=
        component identifier [ is ]
            [ *local*_generic_clause ]
            [ *local*_port_clause ]
        end component [ *component*_simple_name ] ;
    '''

    if utils.is_next_token('component', iToken, lObjects):
        return classify(iToken, lObjects)
    else:
        return iToken


def classify(iToken, lObjects):

    iCurrent = classify_opening_declaration(iToken, lObjects)

    iCurrent = generic_clause.detect(iCurrent, lObjects)

    iCurrent = port_clause.detect(iCurrent, lObjects)

    iCurrent = classify_closing_declaration(iCurrent, lObjects)

    return iCurrent


def classify_opening_declaration(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('component', token.component_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('is', token.is_keyword, iCurrent, lObjects)

    return iCurrent


def classify_closing_declaration(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('component', token.end_component_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.component_simple_name, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
