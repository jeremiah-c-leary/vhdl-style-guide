
from vsg.vhdlFile.classify_new import entity_statement

'''
    entity_statement_part ::=
        { entity_statement }
'''


def detect(iCurrent, lObjects):
    return entity_statement.detect(iCurrent, lObjects)
