
from vsg.rules import line_below_rule


class rule_007(line_below_rule):
    '''
    Function rule 007 enforces a blank line below the "function" keyword.
    '''

    def __init__(self):
        line_below_rule.__init__(self, 'function', '007', 'isFunctionEnd')
