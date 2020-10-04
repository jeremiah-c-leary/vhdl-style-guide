
from vsg.token import generate_statement_body as token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.begin_keyword):
        oToken.set_indent(iIndent)
        iIndent += 1

    if isinstance(oToken, token.end_keyword):
        iIndent -= 1
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
