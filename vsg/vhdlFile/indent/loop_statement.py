
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.loop_statement.loop_label):
        oToken.set_indent(iIndent)
        bMyLabelFound = True
        iIndent += 1

    if isinstance(oToken, token.iteration_scheme.for_keyword):
        if not bMyLabelFound:
          oToken.set_indent(iIndent)
          iIndent += 1
        else:
          oToken.set_indent(iIndent - 1)
        bMyLabelFound = False
            
    if isinstance(oToken, token.iteration_scheme.while_keyword):
        if not bMyLabelFound:
          oToken.set_indent(iIndent)
          iIndent += 1
        else:
          oToken.set_indent(iIndent - 1)
        bMyLabelFound = False
            
    if isinstance(oToken, token.loop_statement.loop_keyword):
        oToken.set_indent(iIndent - 1)

    if isinstance(oToken, token.loop_statement.end_keyword):
        oToken.set_indent(iIndent - 1)
        iIndent -= 1

    return iIndent, bMyLabelFound
