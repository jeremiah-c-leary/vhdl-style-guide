
from vsg.rules import line_above_rule


class rule_007(line_above_rule):
    '''
    Case rule 007 ensures a blank line exists before the "case" keyword.
    '''

    def __init__(self):
        line_above_rule.__init__(self, 'case', '007', 'isCaseKeyword', 'isComment')
