
from vsg.rules import line_below_rule


class rule_011(line_below_rule):
    '''
    Type 011 checks for a blank line below the "type" declaration.
    '''

    def __init__(self):
        line_below_rule.__init__(self, 'type', '011', 'isTypeEnd')
