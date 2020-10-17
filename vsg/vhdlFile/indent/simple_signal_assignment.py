
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.signal_assignment_statement.label):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.simple_force_assignment.target):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.simple_waveform_assignment.target):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.simple_release_assignment.target):
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
