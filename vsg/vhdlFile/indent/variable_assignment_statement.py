
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.variable_assignment_statement.label):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.simple_variable_assignment.target):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.conditional_variable_assignment.target):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.selected_variable_assignment.with_keyword):
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
