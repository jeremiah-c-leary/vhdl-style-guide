
from vsg.vhdlFile.classify import alias_declaration
from vsg.vhdlFile.classify import constant_declaration
from vsg.vhdlFile.classify import subtype_declaration
from vsg.vhdlFile.classify import type_declaration
from vsg.vhdlFile.classify import use_clause
from vsg.vhdlFile.classify import variable_declaration

def tokenize(oObject, iObject, lObjects, dVars):
    '''
    protected_type_body_declarative_item ::=
        subprogram_declaration
      | subprogram_body
      | subprogram_instantiation_declaration
      | package_declaration
      | package_body
      | package_instantiation_declaration
      | type_declaration
      | subtype_declaration
      | constant_declaration
      | variable_declaration
      | file_declaration
      | alias_declaration
      | attribute_declaration
      | attribute_specification
      | use_clause
      | group_template_declaration
      | group_declaration
    '''

    if type_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if subtype_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if constant_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if variable_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if alias_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if use_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False
