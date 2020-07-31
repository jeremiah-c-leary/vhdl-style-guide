import re

from vsg import parser


def package(self, dVars, lTokens, lObjects, oLine):
    '''
    package identifier is

    end [ package ] [ package_simple_name ] ;

    package body package_simple_name is

    end [ package body ] [ package_simple_name ] ;

    '''
    # Check package declarations
    if re.match('^\s*package', oLine.lineLower) and not oLine.insidePackage and not oLine.insidePackageBody:
        oLine.isPackageKeyword = True
        oLine.insidePackage = True
        oLine.indentLevel = 0
        dVars['iCurrentIndentLevel'] = 1
    if oLine.insidePackage:
        if not oLine.insideProcess and not oLine.insideCase and not oLine.insideComponent and not oLine.insideTypeRecord:
            if re.match('^\s*end\s+', oLine.lineLower):
                oLine.isPackageEnd = True
                oLine.indentLevel = 0
                dVars['iCurrentIndentLevel'] = 0


    for iToken, sToken in enumerate(lTokens):
        if not dVars['bPackageKeywordFound']:
            classify_package_keyword(sToken, iToken, lObjects, dVars, oLine)
        else:

            if classify_package_body_body_keyword(sToken, iToken, lObjects, dVars, oLine):
                reclassify_package_body_package_keyword(self, lObjects)

            if not dVars['bPackageIdentifierFound']:
                classify_package_identifier(sToken, iToken, lObjects, dVars, oLine)
            else:
                if not dVars['bPackageIsKeywordFound']:
                    classify_package_is_keyword(sToken, iToken, lObjects, dVars, oLine)
                else:
                    if not dVars['bPackageEndKeywordFound']:
                        classify_package_end_keyword(sToken, iToken, lObjects, dVars, oLine)
                    else:
                        classify_package_body_end_body_keyword(sToken, iToken, lObjects, dVars, oLine)
                        classify_end_package_keyword(sToken, iToken, lObjects, dVars, oLine)
                        classify_package_semicolon(sToken, iToken, lObjects, dVars, oLine)
                        classify_package_simple_name(sToken, iToken, lObjects, dVars, oLine)



def classify_package_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'package':
        lObjects[iToken] = parser.package_keyword(sToken)
        dVars['bPackageKeywordFound'] = True 


def classify_package_body_body_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'body':
        lObjects[iToken] = parser.package_body_body_keyword(sToken)
        dVars['bPackageBodyKeywordFound'] = True 
        return True
    return False


def classify_package_identifier(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() != 'body' and not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        if dVars['bPackageBodyKeywordFound']:
            lObjects[iToken] = parser.package_body_simple_name(sToken)
        else:
            lObjects[iToken] = parser.package_identifier(sToken)
        dVars['bPackageIdentifierFound'] = True


def classify_package_is_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'is':
        if dVars['bPackageBodyKeywordFound']:
            lObjects[iToken] = parser.package_body_is_keyword(sToken)
        else:
            lObjects[iToken] = parser.package_is_keyword(sToken)
        dVars['bPackageIsKeywordFound'] = True


def classify_package_end_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'end':
        if dVars['bPackageBodyKeywordFound']:
            lObjects[iToken] = parser.package_body_end_keyword(sToken)
        else:
            lObjects[iToken] = parser.package_end_keyword(sToken)
        dVars['bPackageEndKeywordFound'] = True 


def classify_end_package_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'package':
        if dVars['bPackageBodyKeywordFound']:
            lObjects[iToken] = parser.package_body_end_package_keyword(sToken)
        else:
            lObjects[iToken] = parser.package_end_package_keyword(sToken)


def classify_package_body_end_body_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'body':
        lObjects[iToken] = parser.package_body_end_body_keyword(sToken)


def classify_package_simple_name(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() != 'package' and sToken.lower() != 'body' and sToken != ';' and not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        if dVars['bPackageBodyKeywordFound']:
            lObjects[iToken] = parser.package_body_end_simple_name(sToken)
        else:
            lObjects[iToken] = parser.package_simple_name(sToken)


def classify_package_semicolon(sToken, iToken, lObjects, dVars, oLine):
    if sToken == ';':
        if dVars['bPackageBodyKeywordFound']:
            lObjects[iToken] = parser.package_body_semicolon(sToken)
        else:
            lObjects[iToken] = parser.package_semicolon(sToken)
        dVars['bPackageKeywordFound'] = False
        dVars['bPackageIdentifierFound'] = False
        dVars['bPackageIsKeywordFound'] = False
        dVars['bPackageEndKeywordFound'] = False
        dVars['bPackageBodyKeywordFound'] = False


def reclassify_package_body_package_keyword(self, lObjects):
    lObjects.reverse()
    bKeywordFound = False
    for iObject, oObject in enumerate(lObjects):
        if type(oObject) == parser.package_keyword:
            lObjects[iObject] = parser.package_body_package_keyword(oObject.get_value()) 
            bKeywordFound = True
            break
    lObjects.reverse()

    if not bKeywordFound:
        bBreak = False
        for oLine in self.lines[::-1]:
            myObjects = oLine.get_objects()
            myObjects.reverse()
            for iObject, oObject in enumerate(myObjects):
                if type(oObject) ==  parser.package_keyword:
                    myObjects[iObject] = parser.package_body_package_keyword(oObject.get_value()) 
                    bBreak = True
                    break
            myObjects.reverse()
            if bBreak:
                break
