
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Package rule 001 checks for spaces at the beginning of the line.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'package', '001', 'isPackageKeyword')

#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isPackageKeyword or oLine.isPackageEnd:
#                check.indent(self, oLine, iLineNumber)
#
#    def _fix_violations(self, oFile):
#        for iLineNumber in self.violations:
#            fix.indent(self, oFile.lines[iLineNumber])
