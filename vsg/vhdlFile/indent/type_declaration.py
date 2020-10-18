
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.incomplete_type_declaration.type_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.full_type_declaration.type_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.record_type_definition.record_keyword):
        iIndent += 1

    if isinstance(oToken, token.identifier_list.identifier):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.record_type_definition.end_keyword):
        iIndent -= 1

    return iIndent, bMyLabelFound
