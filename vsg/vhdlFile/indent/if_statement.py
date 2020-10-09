
from vsg.token import if_statement as token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.if_label):
        oToken.set_indent(iIndent)
        bMyLabelFound = True
        iIndent += 1

    if isinstance(oToken, token.if_keyword):
        if bMyLabelFound:
            oToken.set_indent(iIndent - 1)
            bMyLabelFound = False
        else:
            oToken.set_indent(iIndent)
            iIndent += 1

    if isinstance(oToken, token.elsif_keyword):
        oToken.set_indent(iIndent - 1)

    if isinstance(oToken, token.else_keyword):
        oToken.set_indent(iIndent - 1)

    if isinstance(oToken, token.end_keyword):
        iIndent -= 1
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
