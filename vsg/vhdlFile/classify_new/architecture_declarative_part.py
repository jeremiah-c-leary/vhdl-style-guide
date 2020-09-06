

from vsg.vhdlFile.classify_new import block_declarative_item

'''
    architecture_declarative_part ::=
        { block_declarative_item }
'''


def detect(iToken, lObjects):
    return block_declarative_item.detect(iToken, lObjects)
