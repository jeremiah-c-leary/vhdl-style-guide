
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Signal rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'signal', '001', 'isSignal')
