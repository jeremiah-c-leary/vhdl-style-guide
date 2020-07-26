import re

from vsg import parser


def library(dVars, lTokens, lObjects, oLine):

    '''
    Classifies library declarations.

    library logical_name [, logical_name] ;

    Modifies the following variables:

      * bInsideLibrary
    '''

    for iToken, sToken in enumerate(lTokens):
        if dVars['bInsideLibrary']:

            classify_library_logical_name(sToken, iToken, lObjects, dVars)

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


def classify_library_logical_name(sToken, iToken, lObjects, dVars):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.library_logical_name(sToken)


def classify_library_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'library':
        lObjects[iToken] = parser.library_keyword(sToken)
        dVars['bInsideLibrary'] = True
