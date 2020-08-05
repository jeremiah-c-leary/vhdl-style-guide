import re


def variable(self, dVars, lTokens, lObjects, oLine):
    '''
    [ shared ] variable identifer_list : subtype_indication [ := expression ]
    '''

    if re.match('^\s*variable', oLine.lineLower):
        oLine.isVariable = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']

