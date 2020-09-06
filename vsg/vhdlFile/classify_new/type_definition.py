

from vsg.vhdlFile.classify_new import file_type_definition

'''
    type_definition ::=
        scalar_type_definition
      | composite_type_definition
      | access_type_definition
      | file_type_definition
      | protected_type_definition
'''


def detect(iToken, lObjects):

    iReturn = file_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
