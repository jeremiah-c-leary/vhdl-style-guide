
from vsg.token import generic_map_aspect as token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.generic_keyword):
        oToken.set_indent(iIndent)
        iIndent += 1

    if isinstance(oToken, token.close_parenthesis):
        iIndent -= 1
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
