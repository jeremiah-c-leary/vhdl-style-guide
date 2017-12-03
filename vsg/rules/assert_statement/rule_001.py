
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Assert rule 001 checks for spaces at the beginning of the line.
    '''

    def __init__(self):
        indent_rule.__init__(self)
        self.name = 'assert'
        self.identifier = '001'
        self.sTrigger = 'insideAssert'
