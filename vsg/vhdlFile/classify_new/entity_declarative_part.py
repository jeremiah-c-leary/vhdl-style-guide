
#from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import entity_declarative_item

'''
    entity_declarative_part ::=
        { entity_declarative_item }
'''


def detect(iToken, lObjects):
    return entity_declarative_item.detect(iToken, lObjects)
