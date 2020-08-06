
from vsg.vhdlFile.classify import architecture_body
from vsg.vhdlFile.classify import package_body


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    secondary_unit ::=
        architecture_body
      | package_body
    '''    
    if architecture_body.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if package_body.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False
