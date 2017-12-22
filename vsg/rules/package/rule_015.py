
from vsg.rules import indent_rule


class rule_015(indent_rule):
    '''
    Package rule 015 checks for spaces at the beginning of the line.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'package', '015', 'isPackageEnd')
