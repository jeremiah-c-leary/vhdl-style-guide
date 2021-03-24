
from vsg import parser


def add_optional_item(lTokens, oViolation, oInsertToken):
    lTokens.append(parser.whitespace(' '))
    lTokens.append(oInsertToken)
    oViolation.set_tokens(lTokens)


def remove_optional_item(lTokens, oViolation, oInsertToken):
    if isinstance(lTokens[0], parser.whitespace):
        oViolation.set_tokens([])
    else:
        oViolation.set_tokens([lTokens[0]])


def is_single_line(oToi):
    lTokens = oToi.get_tokens()
    for oToken in lTokens:
        if isinstance(oToken, parser.carriage_return):
            return False
    return True


def number_of_carriage_returns(lTokens):
    iReturn = 0
    for oToken in lTokens:
        if isinstance(oToken, parser.carriage_return):
            iReturn += 1
    return iReturn


def print_debug(lTokens):
    sPrint = ''
    for oToken in lTokens:
        sPrint += oToken.get_value()
    print(sPrint)


def does_line_start_with_comment(lTokens):
    if isinstance(lTokens[0], parser.comment):
        return True
    if isinstance(lTokens[0], parser.whitespace) and isinstance(lTokens[1], parser.comment):
        return True
    return False


def get_toi_parameters(oToi):
    return oToi.get_line_number(), oToi.get_tokens()
