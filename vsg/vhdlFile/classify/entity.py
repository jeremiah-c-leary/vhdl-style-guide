import re

from vsg import parser


def entity(self, dVars, lTokens, lObjects, oLine):
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

    for iToken, sToken in enumerate(lTokens):
        if not dVars['bEntityKeywordFound']:
            classify_entity_keyword(sToken, iToken, lObjects, dVars, oLine)
        else:
            if not dVars['bEntityIdentifierFound']:
                classify_entity_identifier(sToken, iToken, lObjects, dVars, oLine)
            else:
                if not dVars['bEntityIsKeywordFound']:
                    classify_entity_is_keyword(sToken, iToken, lObjects, dVars, oLine)
                else:
                    if not dVars['bEntityBeginKeywordFound']:
                        classify_entity_begin_keyword(sToken, iToken, lObjects, dVars, oLine)
                    else:
                        if not dVars['bEntityEndKeywordFound']:
                            classify_entity_end_keyword(sToken, iToken, lObjects, dVars, oLine)
                        else:
                            classify_end_entity_keyword(sToken, iToken, lObjects, dVars, oLine)
                            classify_entity_semicolon(sToken, iToken, lObjects, dVars, oLine)
                            classify_entity_simple_name(sToken, iToken, lObjects, dVars, oLine)


def classify_entity_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'entity':
        lObjects[iToken] = parser.entity_keyword(sToken)
        dVars['bEntityKeywordFound'] = True 


def classify_entity_identifier(sToken, iToken, lObjects, dVars, oLine):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.entity_identifier(sToken)
        dVars['bEntityIdentifierFound'] = True


def classify_entity_is_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'is':
        lObjects[iToken] = parser.entity_is_keyword(sToken)
        dVars['bEntityIsKeywordFound'] = True


def classify_entity_begin_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'begin':
        lObjects[iToken] = parser.entity_begin_keyword(sToken)
        dVars['bEntityBeginKeywordFound'] = True


def classify_entity_end_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'end':
        lObjects[iToken] = parser.entity_end_keyword(sToken)
        dVars['bEntityEndKeywordFound'] = True 


def classify_end_entity_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'entity':
        lObjects[iToken] = parser.entity_end_entity_keyword(sToken)


def classify_entity_simple_name(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() != 'entity' and sToken != ';' and not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.entity_simple_name(sToken)


def classify_entity_semicolon(sToken, iToken, lObjects, dVars, oLine):
    if sToken == ';':
        lObjects[iToken] = parser.entity_semicolon(sToken)
        dVars['bEntityKeywordFound'] = False
        dVars['bEntityIdentifierFound'] = False
        dVars['bEntityIsKeywordFound'] = False
        dVars['bEntityBeginKeywordFound'] = False
        dVars['bEntityEndKeywordFound'] = False
