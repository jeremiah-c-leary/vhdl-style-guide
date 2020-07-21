import re

from vsg import parser


def use(dVars, lTokens, lObjects, oLine):

    '''
    Classifies library declarations.

    use identifier ;

    Sets the following line attributes:

      * isLibraryUse

    Modifies the following variables:

      * bInsideUse
    '''

    ## This will be depricated when the object method is done for libraries
    if not oLine.insideEntity and not oLine.insideArchitecture and not oLine.insidePackage and not oLine.insidePackageBody:
        check_use_keyword(oLine)

    for iToken, sToken in enumerate(lTokens):
        if dVars['bInsideUse']:

            classify_use_identifier(sToken, iToken, lObjects, dVars)

            classify_semicolon(sToken, iToken, lObjects, dVars)

        else:
            classify_use_keyword(sToken, iToken, lObjects, dVars)


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = parser.use_semicolon()
        dVars['bInsideUse'] = False


def classify_use_identifier(sToken, iToken, lObjects, dVars):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.use_identifier(sToken)


def classify_use_keyword(sToken, iToken, lObjects, dVars):
    if sToken.lower() == 'use':
        lObjects[iToken] = parser.use_keyword(sToken)
        dVars['bInsideUse'] = True



def check_use_keyword(oLine):
    if re.match('^\s*use', oLine.lineLower):
        oLine.isLibraryUse = True
        oLine.indentLevel = 1
