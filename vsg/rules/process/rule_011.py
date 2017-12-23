
from vsg.rules import line_below_rule


class rule_011(line_below_rule):
    '''
    Process rule 010 checks for a blank line after the "end process" keywords.
    '''

    def __init__(self):
        line_below_rule.__init__(self, 'process', '011', 'isEndProcess')
