
from vsg.vhdlFile.classify_new import block_declarative_item

'''
    block_declarative_part ::=
        { block_declarative_item }
'''


def detect(iCurrent, lObjects):
    return block_declarative_item.detect(iCurrent, lObjects)
