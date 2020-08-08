
from vsg.vhdlFile.classify import alias_declaration
from vsg.vhdlFile.classify import attribute_declaration
from vsg.vhdlFile.classify import component_declaration
from vsg.vhdlFile.classify import constant_declaration
from vsg.vhdlFile.classify import file_declaration
from vsg.vhdlFile.classify import shared_variable_declaration
from vsg.vhdlFile.classify import signal_declaration
from vsg.vhdlFile.classify import subtype_declaration
from vsg.vhdlFile.classify import use_clause


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    block_declarative_item ::=
         subprogram_declaration
       | subprogram_body
       | subprogram_instantiation_declaration
       | package_declaration
       | package_body
       | package_instantiation_declaration
       | type_declaration
       | subtype_declaration
       | constant_declaration
       | signal_declaration
       | shared_variable_declaration
       | file_declaration
       | alias_declaration
       | component_declaration
       | attribute_declaration
       | attribute_specification
       | configuration_specification
       | disconnection_specification
       | use_clause
       | group_template_declaration
       | group_declaration
       | PSL_Property_Declaration
       | PSL_Sequence_Declaration
       | PSL_Clock_Declaration
    '''
    if subtype_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if constant_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if signal_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if shared_variable_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if file_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if alias_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if attribute_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if use_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if component_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False
