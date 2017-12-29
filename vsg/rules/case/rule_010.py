
from vsg.rules import line_below_rule


class rule_010(line_below_rule):
    '''
    Case rule 010 ensures a blank line exists below the "end case" keywords.
    '''

    def __init__(self):
        line_below_rule.__init__(self, 'case', '010', 'isEndCaseKeyword')
