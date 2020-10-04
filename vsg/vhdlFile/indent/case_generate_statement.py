
from vsg.token import case_generate_statement as token
from vsg.token import case_generate_alternative


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.generate_label):
        oToken.set_indent(iIndent)
        iIndent += 2

    if isinstance(oToken, case_generate_alternative.when_keyword):
        oToken.set_indent(iIndent -1)

    if isinstance(oToken, token.end_keyword):
        iIndent -= 2
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
