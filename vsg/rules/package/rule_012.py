
from vsg.rules import line_above_rule


class rule_012(line_above_rule):
    '''
    Package rule 012 checks for a blank line above the "end package" keywords.
    '''

    def __init__(self):
        line_above_rule.__init__(self, 'package', '012', 'isPackageEnd')
