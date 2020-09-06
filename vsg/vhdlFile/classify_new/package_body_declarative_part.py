
#from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import package_body_declarative_item

'''
    package_body_declarative_part ::=
        { package_body_declarative_item }
'''


def detect(iToken, lObjects):
    return package_body_declarative_item.detect(iToken, lObjects)
