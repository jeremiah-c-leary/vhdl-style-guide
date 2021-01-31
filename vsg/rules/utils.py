
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
