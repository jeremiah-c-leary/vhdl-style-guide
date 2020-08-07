
from vsg.vhdlFile.classify import component_declaration
from vsg.vhdlFile.classify import constant_declaration
from vsg.vhdlFile.classify import signal_declaration
from vsg.vhdlFile.classify import use_clause
from vsg.vhdlFile.classify import variable_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    package_declarative_item ::=
        subprogram_declaration
      | subprogram_instantiation_declaration
      | package_declaration
      | package_instantiation_declaration
      | type_declaration
      | subtype_declaration
      | constant_declaration
      | signal_declaration
      | variable_declaration
      | file_declaration
      | alias_declaration
      | component_declaration
      | attribute_declaration
      | attribute_specification
      | disconnection_specification
      | use_clause
      | group_template_declaration
      | group_declaration
      | PSL_Property_Declaration
      | PSL_Sequence_Declaration
    '''

    if constant_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if signal_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if variable_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if use_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if component_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False
