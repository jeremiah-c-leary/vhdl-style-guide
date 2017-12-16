
from vsg.rules import indent_rule


class rule_007(indent_rule):
    '''
    Architecture rule 007 checks for spaces at the beginning of the line for the "begin" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'architecture', '007', 'isArchitectureBegin')
