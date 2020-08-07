import re


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
