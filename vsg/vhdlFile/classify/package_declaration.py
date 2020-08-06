
from vsg import parser
from vsg.token import package_body
from vsg.token import package_declaration

from vsg.vhdlFile.classify import package_header
from vsg.vhdlFile.classify import package_declarative_part


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    package_declaration ::=
        package identifier is
            package_header
            package_declarative_part
        end [ package ] [ package_simple_name ] ;
    '''
    if not dVars['bPackageKeywordFound']:

        if not dVars['bPackageBodyEndKeywordFound']:

            if classify_package_keyword(oObject, iObject, lObjects, dVars):
                return True 

    else:

        if not dVars['bPackageIdentifierFound']:

            if classify_package_body_body_keyword(oObject, iObject, lObjects, dVars):
                clear_flags(dVars)
                return True

            if classify_package_identifier(oObject, iObject, lObjects, dVars):
                return True

        else:

            if not dVars['bPackageIsKeywordFound']:

                if classify_package_is_keyword(oObject, iObject, lObjects, dVars):
                    return True 

            else:
                if not dVars['bPackageEndKeywordFound']:

                    if package_header.tokenize(oObject, iObject, lObjects, dVars):
                        return True

                    if package_declarative_part.tokenize(oObject, iObject, lObjects, dVars):
                        return True

                    if classify_package_end_keyword(oObject, iObject, lObjects, dVars):
                        return True 

                else:

                    if classify_package_semicolon(oObject, iObject, lObjects, dVars):
                        return True 

                    if classify_end_package_keyword(oObject, iObject, lObjects, dVars):
                        return True 

                    if classify_package_simple_name(oObject, iObject, lObjects, dVars):
                        return True 
    return False


def classify_package_keyword(oObject, iObject, lObjects, dVars):
    if oObject.get_value().lower() == 'package':
        lObjects[iObject] = oObject
        dVars['bPackageKeywordFound'] = True 
        return True
    return False


def classify_package_body_body_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'body':
        lObjects[iObject] = package_body.body_keyword(sValue)
        dVars['bPackageBodyPackageKeywordFound'] = True 
        dVars['bPackageBodyBodyKeywordFound'] = True 
        return True
    return False


def classify_package_identifier(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = package_declaration.identifier(oObject.get_value())
        dVars['bPackageIdentifierFound'] = True
        return True
    return False


def classify_package_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = package_declaration.is_keyword(sValue)
        dVars['bPackageIsKeywordFound'] = True
        return True
    return False


def classify_package_end_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = package_declaration.end_keyword(sValue)
        dVars['bPackageEndKeywordFound'] = True 
        return True
    return False


def classify_end_package_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'package':
        lObjects[iObject] = package_declaration.end_package_keyword(sValue)
        return True
    return False


def classify_package_simple_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = package_declaration.simple_name(oObject.get_value())
        return True
    return False


def classify_package_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = package_declaration.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['bPackageKeywordFound'] = False
    dVars['bPackageIdentifierFound'] = False
    dVars['bPackageIsKeywordFound'] = False
    dVars['bPackageEndKeywordFound'] = False
    dVars['bPackageBodyKeywordFound'] = False
