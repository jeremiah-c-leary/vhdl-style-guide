
from vsg.vhdlFile.classify import case_generate_statement
from vsg.vhdlFile.classify import for_generate_statement
from vsg.vhdlFile.classify import if_generate_statement


def detect(iToken, lObjects):
    '''
    generate_statement ::=
        for_generate_statement
      | if_generate_statement
      | case_generate_statement
    '''

    iCurrent = for_generate_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = if_generate_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = case_generate_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iCurrent
