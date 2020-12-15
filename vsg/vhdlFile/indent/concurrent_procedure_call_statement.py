
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.concurrent_procedure_call_statement.label_name):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.concurrent_procedure_call_statement.postponed_keyword):
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
