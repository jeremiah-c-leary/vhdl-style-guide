
from vsg import rule
from vsg import fix
from vsg import check


class uppercase_package_name_rule(rule.rule):
    '''
    Package rule 008 checks the package name is upper case on the closing "end package" line.
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None):
        rule.rule.__init__(self, name, identifier)
        self.solution = 'Uppercase package name.'
        self.phase = 6
        self.sTrigger = sTrigger

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sTrigger] and check.has_package_name(oLine):
                check.is_uppercase(self, check.get_package_name(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(self, oFile.lines[iLineNumber], check.get_package_name(oFile.lines[iLineNumber]))
