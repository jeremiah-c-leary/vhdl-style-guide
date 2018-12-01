
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Wait rule 001 checks for the proper indentation of the "wait" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'wait', '001', 'isWait')
