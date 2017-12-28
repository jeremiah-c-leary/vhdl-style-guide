
from vsg.rules import line_above_rule


class rule_018(line_above_rule):
    '''
    Architecture rule 018 checks for a blank line above the "end architecture"
    keywords.
    '''

    def __init__(self):
        line_above_rule.__init__(self, 'architecture', '018', 'isEndArchitecture')
