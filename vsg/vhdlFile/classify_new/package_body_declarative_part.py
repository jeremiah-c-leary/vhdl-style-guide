
#from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import package_declarative_item

'''
    package_declarative_part ::=
        { package_declarative_item }
'''


def detect(iToken, lObjects):
    return package_declarative_item.detect(iToken, lObjects)
