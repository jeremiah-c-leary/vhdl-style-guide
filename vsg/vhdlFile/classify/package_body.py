
from vsg.vhdlFile.classify import package_body_declarative_part
from vsg.token import package_body
from vsg import parser


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    package_body ::=
        package body package_simple_name is
            package_body_declarative_part
        end [ package body ] [ package_simple_name ] ;
    '''

    if not dVars['bPackageBodyPackageKeywordFound']:

        if classify_package_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:
        if not dVars['bPackageBodyBodyKeywordFound']:

            if classify_package_body_body_keyword(oObject, iObject, lObjects, dVars):
                return True 
        else:

            if not dVars['bPackageBodyIdentifierFound']:

                if classify_package_identifier(oObject, iObject, lObjects, dVars):
                    return True 

            else:
                if not dVars['bPackageBodyIsKeywordFound']:

                    if classify_package_is_keyword(oObject, iObject, lObjects, dVars):
                        return True 

                else:
                    if not dVars['bPackageBodyEndKeywordFound']:

                        if package_body_declarative_part.tokenize(oObject, iObject, lObjects, dVars):
                            return True

                        if classify_package_end_keyword(oObject, iObject, lObjects, dVars):
                            return True 

                    else:

                        if classify_package_semicolon(oObject, iObject, lObjects, dVars):
                            return True 

                        if classify_end_package_keyword(oObject, iObject, lObjects, dVars):
                            return True 

                        if classify_package_body_end_body_keyword(oObject, iObject, lObjects, dVars):
                            return True 

                        if classify_package_simple_name(oObject, iObject, lObjects, dVars):
                            return True 

    return False



def classify_package_keyword(oObject, iObject, lObjects, dVars):
    if oObject.get_value().lower() == 'package':
        dVars['bPackageBodyPackageKeywordFound'] = True 
        return True
    return False


def classify_package_body_body_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'body':
        lObjects[iObject] = package_body.body_keyword(sValue)
        dVars['bPackageBodyBodyKeywordFound'] = True 
        return True
    return False


def classify_package_identifier(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = package_body.simple_name(oObject.get_value())
        dVars['bPackageBodyIdentifierFound'] = True
        return True
    return False


def classify_package_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = package_body.is_keyword(sValue)
        dVars['bPackageBodyIsKeywordFound'] = True
        return True
    return False


def classify_package_end_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = package_body.end_keyword(sValue)
        dVars['bPackageBodyEndKeywordFound'] = True 
        return True
    return False


def classify_end_package_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'package':
        lObjects[iObject] = package_body.end_package_keyword(sValue)
        return True
    return False


def classify_package_body_end_body_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'body':
        lObjects[iObject] = package_body.end_body_keyword(sValue)
        return True
    return False


def classify_package_simple_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = package_body.end_simple_name(oObject.get_value())
        return True
    return False


def classify_package_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = package_body.semicolon(oObject.get_value())
        clear_flags(dVars)
        return True
    return False



def clear_flags(dVars):
    dVars['bPackageBodyPackageKeywordFound'] = False
    dVars['bPackageBodyIdentifierFound'] = False
    dVars['bPackageBodyIsKeywordFound'] = False
    dVars['bPackageBodyEndKeywordFound'] = False
    dVars['bPackageBodyBodyKeywordFound'] = False

