
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.procedure_call_statement.label):
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
