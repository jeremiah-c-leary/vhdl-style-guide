import re

from vsg.token import component as token
from vsg import parser


def component(dVars, lTokens, lObjects, oLine):
    '''
    Classifies component declarations.

    component identifier [ is ]
        [ local_generic_clause ]
        [ local_port_clause ]
    end component [ component_simple_name ] ;

    Sets the following line attributes:

      * isComponentDeclaration
      * insideComponent
      * indentLevel
      * isComponentEnd

    Modifies the following variables:

      * iCurrentIndentLevel
    '''
    # Check Component declarations
    if re.match('^\s*component', oLine.lineLower) and not oLine.insideComponent:
        oLine.isComponentDeclaration = True
        oLine.insideComponent = True
        oLine.indentLevel = 1
        dVars['iCurrentIndentLevel'] += 1

    if re.match('^\s*end\s+component', oLine.lineLower):
        oLine.isComponentEnd = True
        oLine.indentLevel = 1
        dVars['iCurrentIndentLevel'] -= 1

    for iToken, sToken in enumerate(lTokens):
        if not dVars['bComponentKeywordFound']:
            classify_keyword(sToken, iToken, lObjects, dVars, oLine)
        else:
            if not dVars['bComponentIdentifierFound']:
                classify_identifier(sToken, iToken, lObjects, dVars, oLine)
            else:
                if not dVars['bComponentIsKeywordFound']:
                    classify_is_keyword(sToken, iToken, lObjects, dVars, oLine)

                if not dVars['bComponentEndKeywordFound']:
                    classify_end_keyword(sToken, iToken, lObjects, dVars, oLine)
                else:
                    classify_end_component_keyword(sToken, iToken, lObjects, dVars, oLine)
                    classify_semicolon(sToken, iToken, lObjects, dVars, oLine)
                    classify_simple_name(sToken, iToken, lObjects, dVars, oLine)


def classify_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'component':
        lObjects[iToken] = token.keyword(sToken)
        dVars['bComponentKeywordFound'] = True 


def classify_identifier(sToken, iToken, lObjects, dVars, oLine):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = token.identifier(sToken)
        dVars['bComponentIdentifierFound'] = True


def classify_is_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'is':
        lObjects[iToken] = token.is_keyword(sToken)
        dVars['bComponentIsKeywordFound'] = True


def classify_end_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'end':
        lObjects[iToken] = token.end_keyword(sToken)
        dVars['bComponentEndKeywordFound'] = True 


def classify_end_component_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'component':
        lObjects[iToken] = token.end_component_keyword(sToken)


def classify_simple_name(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() != 'component' and sToken != ';' and not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = token.simple_name(sToken)


def classify_semicolon(sToken, iToken, lObjects, dVars, oLine):
    if sToken == ';':
        lObjects[iToken] = token.semicolon(sToken)
        dVars['bComponentKeywordFound'] = False
        dVars['bComponentIdentifierFound'] = False
        dVars['bComponentIsKeywordFound'] = False
        dVars['bComponentEndKeywordFound'] = False
