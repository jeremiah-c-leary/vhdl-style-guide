
from vsg.token import delay_mechanism as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    delay_mechanism ::=
        transport
      | [ reject *time*_expression ] inertial
    '''

    if classify_transport_keyword(oObject, iObject, lObjects, dVars):
        return True

    if classify_reject_keyword(oObject, iObject, lObjects, dVars):
        return True

    if classify_inertial_keyword(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_transport_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'transport':
        lObjects[iObject] = token.transport_keyword(sValue)
        return True
    return False


def classify_reject_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'reject':
        lObjects[iObject] = token.reject_keyword(sValue)
        return True
    return False


def classify_inertial_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'inertial':
        lObjects[iObject] = token.inertial_keyword(sValue)
        return True
    return False


def clear_flags(dVars):
    return True
