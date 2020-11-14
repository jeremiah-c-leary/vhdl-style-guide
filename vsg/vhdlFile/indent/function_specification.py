
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.function_specification.pure_keyword):
        oToken.set_indent(iIndent)
        bMyLabelFound = True
        iIndent += 1

    if isinstance(oToken, token.function_specification.impure_keyword):
        oToken.set_indent(iIndent)
        bMyLabelFound = True
        iIndent += 1

    if isinstance(oToken, token.function_specification.function_keyword):
        if not bMyLabelFound:
          oToken.set_indent(iIndent)
          iIndent += 1
        else:
          oToken.set_indent(iIndent - 1)
        bMyLabelFound = False
            
    if isinstance(oToken, token.subprogram_body.begin_keyword):
        oToken.set_indent(iIndent - 1)

    if isinstance(oToken, token.return_statement.return_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.subprogram_body.end_keyword):
        oToken.set_indent(iIndent - 1)

    if isinstance(oToken, token.subprogram_body.semicolon):
        iIndent -= 1

    if isinstance(oToken, token.subprogram_declaration.semicolon):
        iIndent -= 1

    return iIndent, bMyLabelFound
