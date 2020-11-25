
from vsg import parser
from vsg import token

from vsg import tokens

from vsg.vhdlFile.indent import loop_statement
from vsg.vhdlFile.indent import function_specification
from vsg.vhdlFile.indent import procedure_specification
from vsg.vhdlFile.indent import interface_element
from vsg.vhdlFile.indent import generate_statement
from vsg.vhdlFile.indent import generic_clause
from vsg.vhdlFile.indent import port_clause
from vsg.vhdlFile.indent import if_statement
from vsg.vhdlFile.indent import package_body
from vsg.vhdlFile.indent import package_declaration
from vsg.vhdlFile.indent import simple_signal_assignment
from vsg.vhdlFile.indent import signal_declaration
from vsg.vhdlFile.indent import subtype_declaration
from vsg.vhdlFile.indent import type_declaration
from vsg.vhdlFile.indent import variable_declaration
from vsg.vhdlFile.indent import variable_assignment_statement
from vsg.vhdlFile.indent import wait_statement
from vsg.vhdlFile.indent import component_instantiation_statement
from vsg.vhdlFile.indent import generic_map_aspect
from vsg.vhdlFile.indent import port_map_aspect
from vsg.vhdlFile.indent import association_element


def set_token_indent(lTokens):
    '''
    Set the indent level of tokens.
    '''
    iIndent = 0
    bLabelFound = False
    bLibraryFound = False
    bArchitectureFound = False
    for oToken in lTokens:

        if isinstance(oToken, parser.whitespace):
            continue

        if isinstance(oToken, parser.blank_line):
            bLibraryFound = False
            continue

        if isinstance(oToken, parser.carriage_return):
            continue

        if isinstance(oToken, token.context_declaration.context_keyword):
            oToken.set_indent(0)
            iIndent += 1
            continue

        if isinstance(oToken, token.context_declaration.end_keyword):
            oToken.set_indent(0)
            iIndent -= 1
            continue

        if isinstance(oToken, token.library_clause.keyword):
            oToken.set_indent(iIndent)
            bLibraryFound = True
            continue

        if isinstance(oToken, token.use_clause.keyword):
            if not bArchitectureFound:
                oToken.set_indent(iIndent + 1)
            else:
                oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.context_reference.keyword):
            if bLibraryFound:
                oToken.set_indent(iIndent + 1)
            else:
                oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.entity_declaration.entity_keyword):
            oToken.set_indent(iIndent)
            iIndent += 1
            continue

        if isinstance(oToken, token.entity_declaration.end_keyword):
            iIndent -= 1
            oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.architecture_body.architecture_keyword):
            oToken.set_indent(0)
            iIndent = 1
            bArchitectureFound = True
            continue

        if isinstance(oToken, token.architecture_body.begin_keyword):
            oToken.set_indent(0)
            iIndent = 1
            continue

        if isinstance(oToken, token.architecture_body.end_keyword):
            oToken.set_indent(0)
            iIndent = 0
            continue

        if isinstance(oToken, token.architecture_body.semicolon):
            bArchitectureFound = False
            continue

        ###  Assertion statements

        if isinstance(oToken, token.concurrent_assertion_statement.label_name):
            oToken.set_indent(iIndent)
            bLabelFound = True
            iIndent += 1
            continue

        if isinstance(oToken, token.assertion_statement.label):
            oToken.set_indent(iIndent)
            bLabelFound = True
            iIndent += 1
            continue

        if isinstance(oToken, token.assertion.keyword):
            if not bLabelFound:
              oToken.set_indent(iIndent)
              iIndent += 1
            bLabelFound = False
            continue

        if isinstance(oToken, token.assertion.report_keyword):
            oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.assertion.severity_keyword):
            oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.assertion_statement.semicolon):
            iIndent -= 1
            continue

        if isinstance(oToken, token.concurrent_assertion_statement.semicolon):
            iIndent -= 1
            continue

        ### Attribute statements
        if isinstance(oToken, token.attribute_declaration.attribute_keyword):
            oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.attribute_specification.attribute_keyword):
            oToken.set_indent(iIndent)
            continue

        ### case statements
        if isinstance(oToken, token.case_statement.case_label):
            oToken.set_indent(iIndent)
            bLabelFound = True
            iIndent += 1
            continue

        if isinstance(oToken, token.case_statement.case_keyword):
            if not bLabelFound:
              oToken.set_indent(iIndent)
              iIndent += 2
            bLabelFound = False
            continue

        if isinstance(oToken, token.case_statement_alternative.when_keyword):
            oToken.set_indent(iIndent - 1)
            continue

        if isinstance(oToken, token.case_statement.end_keyword):
            oToken.set_indent(iIndent - 2)
            iIndent -= 2
            continue

        ### process statements
        if isinstance(oToken, token.process_statement.process_label):
            oToken.set_indent(iIndent)
            bLabelFound = True
            iIndent += 1
            continue

        if isinstance(oToken, token.process_statement.postponed_keyword):
            if not bLabelFound:
              oToken.set_indent(iIndent)
              iIndent += 1
              bLabelFound = True
            else:
              oToken.set_indent(iIndent - 1)
            continue

        if isinstance(oToken, token.process_statement.process_keyword):
            if not bLabelFound:
              oToken.set_indent(iIndent)
              iIndent += 1
            else:
              oToken.set_indent(iIndent - 1)
            bLabelFound = False
            continue

        if isinstance(oToken, token.process_statement.begin_keyword):
            oToken.set_indent(iIndent - 1)
            continue

        if isinstance(oToken, token.process_statement.end_keyword):
            oToken.set_indent(iIndent - 1)
            iIndent -= 1
            continue

        ### Null statements
        if isinstance(oToken, token.null_statement.label):
            oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.null_statement.null_keyword):
            oToken.set_indent(iIndent)
            continue

        ### Comments
        if isinstance(oToken, parser.comment):
            oToken.set_indent(iIndent)
            continue

        ### Components
        if isinstance(oToken, token.component_declaration.component_keyword):
            oToken.set_indent(iIndent)
            iIndent += 1
            continue

        if isinstance(oToken, token.component_declaration.end_keyword):
            iIndent -= 1
            oToken.set_indent(iIndent)
            continue

        ### Concurrent signal assignment
        if isinstance(oToken, token.concurrent_signal_assignment_statement.label_name):
            oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.concurrent_signal_assignment_statement.postponed_keyword):
            oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.concurrent_simple_signal_assignment.target):
            oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.concurrent_conditional_signal_assignment.target):
            oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.concurrent_selected_signal_assignment.with_keyword):
            oToken.set_indent(iIndent)
            continue

        ### Constant declaration
        if isinstance(oToken, token.constant_declaration.constant_keyword):
            oToken.set_indent(iIndent)
            continue

        ### Variable declaration
        if isinstance(oToken, token.variable_declaration.variable_keyword):
            oToken.set_indent(iIndent)
            continue

        ### File declaration
        if isinstance(oToken, token.file_declaration.file_keyword):
            oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.file_open_information.open_keyword):
            oToken.set_indent(iIndent + 1)
            continue

        if isinstance(oToken, token.file_open_information.is_keyword):
            oToken.set_indent(iIndent + 1)
            continue

        iIndent, bLabelFound = loop_statement.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = procedure_specification.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = function_specification.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = interface_element.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = generate_statement.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = generic_clause.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = port_clause.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = if_statement.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = package_body.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = package_declaration.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = simple_signal_assignment.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = signal_declaration.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = subtype_declaration.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = type_declaration.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = variable_declaration.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = variable_assignment_statement.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = wait_statement.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = component_instantiation_statement.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = generic_map_aspect.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = port_map_aspect.set_indent(iIndent, bLabelFound, oToken)
        iIndent, bLabelFound = association_element.set_indent(iIndent, bLabelFound, oToken)
