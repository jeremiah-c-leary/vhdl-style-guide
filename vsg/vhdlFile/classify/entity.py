import re


def entity(self, dVars, oLine):
    '''
    Classifies entity declarations.

    entity identifier is
        [ port ( port_interface_list ) ;]
        { entity_declarative_item }
    [begin
        { concurrent_assertion_statement
        | passive_concurrent_procedure_call_statement
        | passive_process_statement } ]
    end [entity] [identifier] ;

    Sets the following line attributes:

      * hasEntity
      * isEntityDeclaration
      * identLevel
      * insideEntity
      * isEndEntityDeclaration

    Modifies the following variables:

      * iCurrentIndentLevel
    '''
    # Check for entity
    if re.match('^\s*entity', oLine.lineLower):
        self.hasEntity = True
        oLine.isEntityDeclaration = True
        dVars['iCurrentIndentLevel'] = 1
        oLine.indentLevel = 0
        oLine.insideEntity = True
    # Check for the end of the entity
    if re.match('^\s*end', oLine.lineLower) and not oLine.insidePortMap and not oLine.insideGenericMap and oLine.insideEntity:
        oLine.isEndEntityDeclaration = True
        oLine.indentLevel = 0
        dVars['iCurrentIndentLevel'] = 0
