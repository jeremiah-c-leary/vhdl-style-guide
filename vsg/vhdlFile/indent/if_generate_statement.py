
from vsg.token import if_generate_statement as token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.generate_label):
        oToken.set_indent(iIndent)
        iIndent += 1

    if isinstance(oToken, token.if_keyword):
        oToken.set_indent(iIndent - 1)

    if isinstance(oToken, token.elsif_keyword):
        oToken.set_indent(iIndent - 1)

    if isinstance(oToken, token.else_keyword):
        oToken.set_indent(iIndent - 1)

    if isinstance(oToken, token.end_keyword):
        iIndent -= 1
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
