
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.wait_statement.label):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.wait_statement.wait_keyword):
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
