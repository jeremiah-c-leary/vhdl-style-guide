
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.procedure_call.procedure_name):
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
