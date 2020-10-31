
from vsg.token import association_element as token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.formal_part):
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
