
from vsg import rule
from vsg import utils


class rule_015(rule.rule):
    '''
    General rule 014 checks capitalization consistency of signal names.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'signal', '015')
        self.fixable = False
        self.solution = 'multiple signals defined in a single declaration'
        self.phase = 1
        self.consecutive = 2
        self.configuration.append('consecutive')

    def _pre_analyze(self):
        self.sFullLine = ''
        self.iFailureLine = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isSignal:
            self.sFullLine = ''
            self.iFailureLine = iLineNumber
        if oLine.insideSignal:
            self.sFullLine += oLine.line
        if oLine.isEndSignal:
            if self.sFullLine.count(',') > self.consecutive - 1:
                self.add_violation(self.iFailureLine)

#    def _fix_violations(self, oFile):
#        for iLineNumber in self.violations:
#            for sWord in self.dFix['violations'][iLineNumber]:
#                sReplacementWord = get_replacement_word(self, sWord)
#                if oFile.lines[iLineNumber].isInstantiationPortAssignment:
#                    oLine = oFile.lines[iLineNumber]
#                    sLine = oLine.line
#                    iIndex = sLine.index('>')
#                    oLine.update_line(sLine[iIndex:])
#                    utils.change_word(oLine, sWord, sReplacementWord, 20)
#                    sNewLine = sLine[0:iIndex] + oLine.line
#                    oFile.lines[iLineNumber].update_line(sNewLine)
#                else:
#                    utils.change_word(oFile.lines[iLineNumber], sWord, sReplacementWord, 20)


