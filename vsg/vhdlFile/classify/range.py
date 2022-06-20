
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    range ::=
        range_attribute_name
      | simple_expression direction simple_expression
    '''
    if check_for_range_attribute_name(iToken, lObjects):
        return True
    return detect_direction(iToken, lObjects)


def check_for_range_attribute_name(iToken, lObjects):
    iParens = 0
    iTodoTokens = 0
    for iIndex in range(iToken, len(lObjects)):
        iParens = utils.update_paren_counter(iIndex, lObjects, iParens)

        if iParens == -1:
            if iTodoTokens == 1:
                return True
            return False

        if not utils.token_is_whitespace_or_comment(lObjects[iIndex]):
            iTodoTokens += 1
        if iParens == 0:
            if utils.object_value_is(lObjects, iIndex, "'"):
                return True
    return False


def detect_direction(iToken, lObjects):
    iParens = 0
    for iIndex in range(iToken, len(lObjects)):
        iParens = utils.update_paren_counter(iIndex, lObjects, iParens)
        if iParens == -1:
            return False
        if check_for_direction(iParens, iIndex, lObjects):
            return True
    return False


def check_for_direction(iParens, iIndex, lObjects):
    if iParens == 0:
        if utils.is_next_token_one_of(['downto', 'to'], iIndex, lObjects):
            return True
    return False
