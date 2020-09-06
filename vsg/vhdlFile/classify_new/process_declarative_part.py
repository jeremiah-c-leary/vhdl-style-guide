

from vsg.vhdlFile.classify_new import process_declarative_item

'''
    process_declarative_part ::=
        { process_declarative_item }
'''


def detect(iToken, lObjects):
    return process_declarative_item.detect(iToken, lObjects)
