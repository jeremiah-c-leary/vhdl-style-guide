

from vsg.token import range_constraint as token

from vsg.vhdlFile.classify import vhdl_range


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    unbounded_array_definition ::=
        array ( index_subtype_definition { , index_subtype_definition } )
        of element_subtype_indication

    LIMITIATION:  index_subtype_definition and element_subtype_indication are not parsed.
    ''' 

    if not dVars['range_constraint']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if vhdl_range.tokenize(oObject, iObject, lObjects, dVars):
            return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'range':
        lObjects[iObject] = token.keyword(sValue)
        dVars['range_constraint']['keyword'] = True 
        return True
    return False


def clear_flags(dVars):
    dVars['range_constraint']['keyword'] = False
    vhdl_range.clear_flags(dVars)
