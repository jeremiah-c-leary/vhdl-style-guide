
from vsg.vhdlFile.indent import case_generate_statement
from vsg.vhdlFile.indent import for_generate_statement
from vsg.vhdlFile.indent import if_generate_statement
from vsg.vhdlFile.indent import generate_statement_body


def set_indent(iCurrentIndent, bLabelFound, oToken):

    iIndent = iCurrentIndent
    bMyLabelFound = bLabelFound

    iIndent, bMyLabelFound = for_generate_statement.set_indent(iIndent, bLabelFound, oToken)
    iIndent, bMyLabelFound = if_generate_statement.set_indent(iIndent, bLabelFound, oToken)
    iIndent, bMyLabelFound = case_generate_statement.set_indent(iIndent, bLabelFound, oToken)
    iIndent, bMyLabelFound = generate_statement_body.set_indent(iIndent, bLabelFound, oToken)

    return iIndent, bMyLabelFound
