
from vsg.vhdlFile.classify import use_clause
from vsg.vhdlFile.classify import entity_declaration
from vsg.vhdlFile.classify import architecture_body


def tokenize(oObject, iObject, lObjects, dVars):

    '''
    design_file ::= design_unit { design_unit }
    '''
    if design_unit(oObject, iObject, lObjects, dVars):
        return True 


def design_unit(oObject, iObject, lObjects, dVars):
    '''
    design_unit ::= context_clause library_unit
    '''

    if context_clause(oObject, iObject, lObjects, dVars):
        return True

    if library_unit(oObject, iObject, lObjects, dVars):
        return True


def context_clause(oObject, iObject, lObjects, dVars):
    '''
    ??
    '''

    if use_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True


def library_unit(oObject, iObject, lObjects, dVars):
    '''
    library_unit ::=
        primary_unit
      | secondary_unit
    '''

    if primary_unit(oObject, iObject, lObjects, dVars):
        return True

    if secondary_unit(oObject, iObject, lObjects, dVars):
        return True


def primary_unit(oObject, iObject, lObjects, dVars):
    '''
    primary_unit ::=
        entity_declaration
      | configuration_declaration
      | package_declaration
      | package_instantiation_declaration
      | context_declaration
      | PSL_Verification_Unit
    ''' 

    if entity_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True


def secondary_unit(oObject, iObject, lObjects, dVars):
    '''
    secondary_unit ::=
        architecture_body
      | package_body
    '''    
    if architecture_body.tokenize(oObject, iObject, lObjects, dVars):
        return True

