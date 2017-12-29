
from vsg.rules import line_above_rule


class rule_009(line_above_rule):
    '''
    Case rule 009 ensures a blank line exists above the "end case" keywords.
    '''

    def __init__(self):
        line_above_rule.__init__(self, 'case', '009', 'isEndCaseKeyword')
