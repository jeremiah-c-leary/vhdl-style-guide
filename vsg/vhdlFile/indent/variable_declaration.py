
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.variable_declaration.shared_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.variable_declaration.variable_keyword):
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
