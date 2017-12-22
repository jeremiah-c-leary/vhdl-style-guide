
from vsg.rules import line_below_rule


class rule_011(line_below_rule):
    '''
    Package rule 011 checks for a blank line below the package keyword.
    '''

    def __init__(self):
        line_below_rule.__init__(self, 'package', '011', 'isPackageKeyword')
