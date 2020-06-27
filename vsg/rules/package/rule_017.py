from vsg.rules import prefix_rule


class rule_017(prefix_rule):
    '''
    Package rule 017 checks for prefixes in package identifier.
    '''

    def __init__(self):
        prefix_rule.__init__(self, 'package', '017', 'isPackageKeyword')
        self.prefixes = ['pkg_']
        self.solution = 'Package identifier'

    def _extract(self, oLine):
        return [oLine.line.split()[1]]
