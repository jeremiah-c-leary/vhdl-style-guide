from vsg.rules import suffix_rule


class rule_016(suffix_rule):
    '''
    Package rule 016 checks for suffixes in package identifier.
    '''

    def __init__(self):
        suffix_rule.__init__(self, 'package', '016', 'isPackageKeyword')
        self.suffixes = ['_pkg']
        self.solution = 'Package'

    def _extract(self, oLine):
        return [oLine.line.split()[1]]
