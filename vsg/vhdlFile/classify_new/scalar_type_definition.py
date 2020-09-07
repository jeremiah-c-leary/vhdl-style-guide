

from vsg.vhdlFile.classify_new import enumeration_type_definition

'''
    scalar_type_definition ::=
        enumeration_type_definition
      | integer_type_definition
      | floating_type_definition
      | physical_type_definition
'''


def detect(iToken, lObjects):

    iReturn = enumeration_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
