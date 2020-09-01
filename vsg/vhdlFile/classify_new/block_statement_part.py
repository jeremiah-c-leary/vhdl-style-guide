
from vsg import parser
from vsg.vhdlFile import utils

#from vsg.token import block_statement as token

from vsg.vhdlFile.classify_new import concurrent_statement
#from vsg.vhdlFile.classify import block_declarative_part
#from vsg.vhdlFile.classify import block_statement_part

'''
    block_statement_part ::=
        { concurrent_statement }
'''


def detect(iCurrent, lObjects):
    return concurrent_statement.detect(iCurrent, lObjects)
