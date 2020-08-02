
from vsg.token import port_clause as token


def port_clause(dVars, lTokens, lObjects, oLine):
    '''
    Classifies port clauses:

        port ( port_list ) ;
    '''
    for iToken, sToken in enumerate(lTokens):
        if not dVars['bPortClauseKeywordFound']:
            classify_keyword(sToken, iToken, lObjects, dVars)
        else:
            if not dVars['bPortClauseOpenParenthesisFound']:
                classify_open_parenthesis(sToken, iToken, lObjects, dVars)
            else:
                classify_semicolon(sToken, iToken, lObjects, dVars)
                classify_close_parenthesis(sToken, iToken, lObjects, dVars)


def classify_keyword(sToken, iToken, lObjects, dVars):
    if sToken.lower() == 'port':
        lObjects[iToken] = token.keyword(sToken)
        dVars['bPortClauseKeywordFound'] = True


def classify_open_parenthesis(sToken, iToken, lObjects, dVars):
    if sToken == '(':
        lObjects[iToken] = token.open_parenthesis()
        dVars['bPortClauseOpenParenthesisFound'] = True


def classify_close_parenthesis(sToken, iToken, lObjects, dVars):
    if sToken == ')':
        lObjects[iToken] = token.close_parenthesis()


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = token.semicolon()
        dVars['bPortClauseKeywordFound'] = False
        dVars['bPortClauseOpenParenthesisFound'] = False
