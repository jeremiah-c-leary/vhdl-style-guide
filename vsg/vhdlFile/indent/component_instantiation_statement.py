
from vsg.token import component_instantiation_statement as token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.instantiation_label):
        oToken.set_indent(iIndent)
        iIndent += 1

    if isinstance(oToken, token.semicolon):
        oToken.set_indent(iIndent)
        iIndent -= 1

    return iIndent, bMyLabelFound
