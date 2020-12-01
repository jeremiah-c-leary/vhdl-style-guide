
from vsg import parser


def is_token_at_start_of_line(iIndex, oTokenMap):
    if oTokenMap.is_token_at_index(parser.carriage_return, iIndex - 1):
        return True
    if oTokenMap.is_token_at_index(parser.carriage_return, iIndex - 2) and oTokenMap.is_token_at_index(parser.whitespace, iIndex - 1):
        return True
    return False
