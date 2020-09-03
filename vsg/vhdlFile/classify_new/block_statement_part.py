
from vsg.vhdlFile import utils


from vsg.vhdlFile.classify_new import concurrent_statement

'''
    block_statement_part ::=
        { concurrent_statement }
'''


def detect(iCurrent, lObjects):
    return concurrent_statement.detect(iCurrent, lObjects)
