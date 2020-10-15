
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.procedure_specification.procedure_keyword):
       oToken.set_indent(iIndent)
       iIndent += 1

    if isinstance(oToken, token.procedure_specification.close_parenthesis):
       oToken.set_indent(iIndent - 1)

    return iIndent, bMyLabelFound
