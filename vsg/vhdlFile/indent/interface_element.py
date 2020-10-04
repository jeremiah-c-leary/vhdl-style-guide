
from vsg import token


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    if isinstance(oToken, token.interface_constant_declaration.constant_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.interface_signal_declaration.signal_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.interface_variable_declaration.variable_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.interface_file_declaration.file_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.interface_unknown_declaration.identifier):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.interface_incomplete_type_declaration.type_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.interface_procedure_specification.procedure_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.interface_function_specification.function_keyword):
        oToken.set_indent(iIndent)

    if isinstance(oToken, token.interface_package_declaration.package_keyword):
        oToken.set_indent(iIndent)

    return iIndent, bMyLabelFound
