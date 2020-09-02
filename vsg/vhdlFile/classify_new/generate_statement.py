
from vsg.vhdlFile.classify_new import for_generate_statement
#from vsg.vhdlFile.classify_new import if_generate_statement
#from vsg.vhdlFile.classify_new import case_generate_statement


def detect(iObject, lObjects):
    '''
    generate_statement ::=
        for_generate_statement
      | if_generate_statement
      | case_generate_statement
    '''

    iReturn = for_generate_statement.detect(iObject, lObjects)
    if iReturn != iObject:
        return iReturn

#    if if_generate_statement.is_it(iObject, oObject, lObjects, lNewObjects, dVars):
#        return True
#
#    if case_generate_statement.is_it(iObject, oObject, lObjects, lNewObjects, dVars):
#        return True

    return iReturn
