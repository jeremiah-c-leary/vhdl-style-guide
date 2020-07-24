import re

from vsg import parser


def library(dVars, lTokens, lObjects, oLine):

    '''
    Classifies library declarations.

    library identifier [, identifier] ;

    Sets the following line attributes:

      * isLibrary

    Modifies the following variables:

      * bInsideLibrary
    '''

    ## This will be depricated when the object method is done for libraries
    if not oLine.insideEntity and not oLine.insideArchitecture and not oLine.insidePackage and not oLine.insidePackageBody:
        check_library_keyword(oLine)

    for iToken, sToken in enumerate(lTokens):
        if dVars['bInsideLibrary']:

            classify_library_identifier(sToken, iToken, lObjects, dVars)

            classify_comma(sToken, iToken, lObjects, dVars)

            classify_semicolon(sToken, iToken, lObjects, dVars)

        else:
            classify_library_keyword(sToken, iToken, lObjects, dVars, oLine)


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = parser.library_semicolon()
        dVars['bInsideLibrary'] = False


def classify_comma(sToken, iToken, lObjects, dVars):
    if sToken == ',':
        lObjects[iToken] = parser.library_comma()


def classify_library_identifier(sToken, iToken, lObjects, dVars):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.library_identifier(sToken)


def classify_library_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'library':
        lObjects[iToken] = parser.library_keyword(sToken)
        dVars['bInsideLibrary'] = True
        if iToken < 2:
            oLine.indentLevel = dVars['iCurrentIndentLevel']



def check_library_keyword(oLine):
    if re.match('^\s*library', oLine.lineLower):
        oLine.isLibrary = True
        oLine.indentLevel = 0
