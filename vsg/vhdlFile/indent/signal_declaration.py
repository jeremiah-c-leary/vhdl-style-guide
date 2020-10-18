
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.signal_declaration.signal_keyword):
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
