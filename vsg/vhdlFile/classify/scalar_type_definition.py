
from vsg.vhdlFile.classify import enumeration_type_definition
from vsg.vhdlFile.classify import integer_type_definition
from vsg.vhdlFile.classify import floating_type_definition
from vsg.vhdlFile.classify import physical_type_definition


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    scalar_type_definition ::= [§ 5.2.1]
        enumeration_type_definition
      | integer_type_definition
      | floating_type_definition
      | physical_type_definition
    '''
    if enumeration_type_definition.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if integer_type_definition.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if floating_type_definition.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if physical_type_definition.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):

    enumeration_type_definition.clear_flags(dVars)
    integer_type_definition.clear_flags(dVars)
    floating_type_definition.clear_flags(dVars)
    physical_type_definition.clear_flags(dVars)

