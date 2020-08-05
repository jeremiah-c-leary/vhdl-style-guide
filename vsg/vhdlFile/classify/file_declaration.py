
from vsg import parser
from vsg.token import file_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    file identifier_list : subtype_indication [ [ open file_open_kind_expression ] is file_logic_name ]
    '''

    if not dVars['bFileKeywordFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['bFileColonFound']:
            if classify_colon(oObject, iObject, lObjects, dVars):
                return True

            if classify_comma(oObject, iObject, lObjects):
                return True 

            if classify_identifier(oObject, iObject, lObjects):
                return True 

        else:

            if classify_semicolon(oObject, iObject, lObjects, dVars):
                return True

            file_open_information(oObject, iObject, lObjects, dVars)

            if not dVars['bFileOpenKeywordFound'] and not dVars['bFileIsKeywordFound']:

                if classify_subtype_indication(oObject, iObject, lObjects):
                    return True 

    return False
              

def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'file':
        lObjects[iObject] = file_declaration.keyword(sValue)
        dVars['bFileKeywordFound'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = file_declaration.identifier(oObject.get_value)
        return True
    return False


def classify_comma(oObject, iObject, lObjects):
    if oObject.get_value() == ',':
        lObjects[iObject] = file_declaration.comma()
        return True
    return False


def classify_colon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':':
        lObjects[iObject] = file_declaration.colon()
        dVars['bFileColonFound'] = True
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = file_declaration.subtype_indication(oObject.get_value())
        return True
    return False


def classify_open_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'open':
        lObjects[iObject] = file_declaration.open_keyword(sValue)
        dVars['bFileOpenKeywordFound'] = True 
        dVars['bFileIsKeywordFound'] = False
        return True
    return False


def classify_file_open_kind_expression(oObject, iObject, lObjects):
    if type(oObject) == parser.item and oObject.get_value().lower() != 'is':
        lObjects[iObject] = file_declaration.open_kind_expression(oObject.get_value())
        return True
    return False


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue== 'is':
        lObjects[iObject] = file_declaration.is_keyword(sValue)
        dVars['bFileOpenKeywordFound'] = False
        dVars['bFileIsKeywordFound'] = True 
        return True
    return False


def classify_file_logical_name(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = file_declaration.logical_name(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = file_declaration.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['bFileKeywordFound'] = False
    dVars['bFileColonFound'] = False
    dVars['bFileOpenKeywordFound'] = False
    dVars['bFileIsKeywordFound'] = False


def file_open_information(oObject, iObject, lObjects, dVars):

    if not dVars['bFileOpenKeywordFound']:

        if classify_open_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if classify_file_open_kind_expression(oObject, iObject, lObjects):
            return True 
    
    if not dVars['bFileIsKeywordFound']:

        if classify_is_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if classify_file_logical_name(oObject, iObject, lObjects):
            return True 

    return False
