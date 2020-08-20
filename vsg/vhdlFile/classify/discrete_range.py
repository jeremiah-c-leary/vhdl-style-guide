

def tokenize(oObject, iObject, lObjects, dVars):
    '''
    discrete_range ::=
        *discrete*_subtype_indication | range

    LIMITATION:  Further classification into subtype_indication and range is not performed.
    '''
    
    if classify_object(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_object(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        return True
    return False


def clear_flags(dVars):
    for_generate_statement.clear_flags(dVars)
