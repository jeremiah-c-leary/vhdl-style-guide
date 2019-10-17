
from vsg import rule
from vsg import check
from vsg import fix
from vsg import utils


class rule_017(rule.rule):
    '''
    Generic rule 017 checks the generic type is lowercase.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generic'
        self.identifier = '017'
        self.solution = 'Change generic type to lowercase.'
        self.phase = 6

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isGenericDeclaration:
            sLine = oLine.line.split(':')[1].lstrip()
            if '(' in sLine:
                sLine = sLine.split('(')[0].rstrip()
            if utils.is_vhdl_keyword(sLine.split()[0]):
                check.is_lowercase(self, sLine.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line.split(':')[1].lstrip()
            if '(' in sLine:
                sLine = sLine.split('(')[0].rstrip()
            sWord = sLine.split()[0]
            fix.lower_case(oLine, sWord)
