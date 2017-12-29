
from vsg.rules import line_below_rule


class rule_008(line_below_rule):
    '''
    Case rule 008 ensures a blank line exists below the "case" keyword.
    '''

    def __init__(self):
        line_below_rule.__init__(self, 'case', '008', 'isCaseIsKeyword')
