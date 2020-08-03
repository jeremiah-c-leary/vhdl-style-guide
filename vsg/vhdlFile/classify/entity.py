import re

from vsg.token import entity as token
from vsg import parser


def legacy(self, dVars, oLine):
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



def beginning(oObject, iObject, lObjects, dVars):
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
    if not dVars['bEntityKeywordFound']:
        classify_keyword(oObject, iObject, lObjects, dVars)
    else:
        if not dVars['bEntityIdentifierFound']:
            classify_identifier(oObject, iObject, lObjects, dVars)
        else:
            if not dVars['bEntityIsKeywordFound']:
                classify_is_keyword(oObject, iObject, lObjects, dVars)


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'entity':
        lObjects[iObject] = token.keyword(sValue)
        dVars['bEntityKeywordFound'] = True 


def classify_identifier(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item:
        lObjects[iObject] = token.identifier(sValue)
        dVars['bEntityIdentifierFound'] = True


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = token.is_keyword(sValue)
        dVars['bEntityIsKeywordFound'] = True



def ending(oObject, iObject, lObjects, dVars):
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

    '''

    if dVars['bEntityIsKeywordFound']:
        if not dVars['bEntityBeginKeywordFound']:
            classify_begin_keyword(oObject, iObject, lObjects, dVars)
        if not dVars['bEntityEndKeywordFound']:
            classify_end_keyword(oObject, iObject, lObjects, dVars)
        else:
            if classify_end_entity_keyword(oObject, iObject, lObjects, dVars):
                return
            classify_simple_name(oObject, iObject, lObjects, dVars)
            classify_semicolon(oObject, iObject, lObjects, dVars)


def classify_begin_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'begin':
        lObjects[iObject] = token.begin_keyword(sValue)
        dVars['bEntityBeginKeywordFound'] = True


def classify_end_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = token.end_keyword(sValue)
        dVars['bEntityEndKeywordFound'] = True 


def classify_end_entity_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'entity':
        lObjects[iObject] = token.end_entity_keyword(sValue)
        return True
    return False


def classify_simple_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.simple_name(oObject.get_value())


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        dVars['bEntityKeywordFound'] = False
        dVars['bEntityIdentifierFound'] = False
        dVars['bEntityIsKeywordFound'] = False
        dVars['bEntityBeginKeywordFound'] = False
        dVars['bEntityEndKeywordFound'] = False
