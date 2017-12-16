
from vsg.rules import indent_rule


class rule_008(indent_rule):
    '''
    Architecture rule 008 checks for spaces at the beginning of the line for the "end architecture" keywords.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'architecture', '008', 'isEndArchitecture')
