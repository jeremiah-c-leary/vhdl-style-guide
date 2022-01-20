
from vsg.token import physical_type_definition as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import primary_unit_declaration
from vsg.vhdlFile.classify import range_constraint
from vsg.vhdlFile.classify import secondary_unit_declaration


def detect(iToken, lObjects):
    '''
    physical_type_definition ::=
        range_constraint
            **units**
                primary_unit_declaration
                { secondary_unit_declaration }
            **end** **units** [ physical_type_simple_name ]
    '''
    if units_keyword_found_before_semicolon(iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = range_constraint.detect(iToken, lObjects)

    iCurrent = utils.assign_next_token_required('units', token.units_keyword, iToken, lObjects)

    iCurrent = primary_unit_declaration.detect(iCurrent, lObjects)

    while not utils.is_next_token('end', iCurrent, lObjects):
        iCurrent = secondary_unit_declaration.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token(token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('units', token.end_units_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.simple_name, iCurrent, lObjects)

    return iCurrent


def units_keyword_found_before_semicolon(iToken, lObjects):
    if utils.find_in_range('units', iToken, ';', lObjects):
        return True
    return False
