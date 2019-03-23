
from vsg import rule
from vsg import utils


class rule_013(rule.rule):
    '''Generic rule 013 checks for a generic keyword on the same line as a generic declaration.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generic'
        self.identifier = '013'
        self.solution = 'Move generic declaration to it\'s own line.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isGenericDeclaration and oLine.isGenericKeyword:
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utils.copy_line(oFile, iLineNumber)
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.split('(')[0] + ' (')
            oLine.isGenericDeclaration = False
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line('  ' + oLine.line.split('(')[1])
            oLine.isGenericKeyword = False
            oLine.isGenericDeclaration = True
            oLine.insideGenericMap = True
            oLine.indentLevel = oFile.lines[iLineNumber].indentLevel + 1
