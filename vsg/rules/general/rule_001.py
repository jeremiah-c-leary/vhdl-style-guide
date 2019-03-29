
from vsg import rule
from vsg import utils


class rule_001(rule.rule):
    '''
    General rule 001 checks capitalization consistency of non VHDL keywords.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'general', '001')
        self.fixable = False
        self.solution = 'Inconsistent capitalization of word'
        self.phase = 6
        self.lLowerCaseWords = []
        self.lCaseWords = []

    def _analyze(self, oFile, oLine, iLineNumber):
        lWords = utils.extract_non_keywords(oLine.line)
        for sWord in lWords:
            if not sWord.lower() in self.lLowerCaseWords:
                self.lLowerCaseWords.append(sWord.lower())
                self.lCaseWords.append(sWord)
            else:
                if not sWord in self.lCaseWords:
                    self.add_violation(iLineNumber)
                    try:
                        self.dFix['violations'][iLineNumber].append(sWord)
                    except KeyError:
                        self.dFix['violations'][iLineNumber] = []
                        self.dFix['violations'][iLineNumber].append(sWord)

    def _get_solution(self, iLineNumber):
        if len(self.dFix['violations'][iLineNumber]) > 1:
            sSolution = self.solution + 's: ' + ', '.join(self.dFix['violations'][iLineNumber])
        else:
            sSolution = self.solution + ': ' + ', '.join(self.dFix['violations'][iLineNumber])
        return sSolution
