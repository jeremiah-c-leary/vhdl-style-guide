
from vsg.rules import line_above_rule


class rule_023(line_above_rule):
    '''
    Process rule 023 checks for a blank line above the "end process" keywords.
    '''

    def __init__(self):
        line_above_rule.__init__(self, 'process', '023', 'isEndProcess')
