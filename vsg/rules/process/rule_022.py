
from vsg.rules import line_below_rule


class rule_022(line_below_rule):
    '''
    Process rule 022 checks for a blank line below the "begin" keyword.
    '''

    def __init__(self):
        line_below_rule.__init__(self, 'process', '022', 'isProcessBegin')
