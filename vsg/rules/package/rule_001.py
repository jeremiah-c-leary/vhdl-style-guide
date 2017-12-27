
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Package rule 001 checks for spaces at the beginning of the line.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'package', '001', 'isPackageKeyword')
