
from vsg.rules.package import package_rule
from vsg import check


class rule_012(package_rule):
    '''
    Package rule 012 checks for a blank line above the "end package" keywords.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Add blank line above the "end package" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                check.is_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)
