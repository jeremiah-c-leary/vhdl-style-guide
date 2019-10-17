
from vsg import rule
from vsg import fix
from vsg import check
from vsg import utils


class rule_004(rule.rule):
    '''
    Signal rule 004 checks the signal name is lowercase.
    '''
    def __init__(self, name='signal', identifier='004'):
        rule.rule.__init__(self, name, identifier)
        self.phase = 6
        self.solution = 'Change signal name to lowercase.'

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isSignal:
            for sWord in utils.extract_class_identifier_list(oLine):
                check.is_lowercase(self, sWord, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            for sWord in utils.extract_class_identifier_list(oLine):
                fix.lower_case(oLine, sWord)
