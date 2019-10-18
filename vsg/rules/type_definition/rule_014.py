
from vsg import rule
from vsg import utils


class rule_014(rule.rule):
    '''
    General rule 014 checks capitalization consistency of type names.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'type', '014')
        self.fixable = True
        self.solution = 'Inconsistent capitalization of word'
        self.phase = 6
        self.lLowerCaseWords = []
        self.lCaseWords = []
        self.dDatabase = create_database()

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isTypeKeyword:
            self.dDatabase['type'].append(utils.extract_type_identifier(oLine)[0])
        if oLine.insideArchitecture:
            if oLine.insideConstant:
                lWords = extract_word_list(oLine)
                check_violations(self, lWords, iLineNumber)
            if oLine.isSignal:
                lWords = extract_word_list(oLine)
                check_violations(self, lWords, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            for sWord in self.dFix['violations'][iLineNumber]:
                sReplacementWord = get_replacement_word(self, sWord)
                utils.change_word(oFile.lines[iLineNumber], sWord, sReplacementWord, 20)

    def _get_solution(self, iLineNumber):
        sSolution = self.solution + ': ' + ', '.join(self.dFix['violations'][iLineNumber])
        return sSolution


def create_database():

    dDatabase = {}
    dDatabase['type'] = []

    return dDatabase


def extract_word_list(oLine):

    if oLine.isSignal:
        sLine = oLine.line[oLine.line.find(':') + 1:]
    else:
        sLine = oLine.line

    lWords = utils.extract_non_keywords(sLine)
    return lWords


def check_violations(self, lWords, iLineNumber):
    for sWord in lWords:
        if sWord.lower() in map(str.lower, self.dDatabase['type']):
            if sWord not in self.dDatabase['type']:
                self.add_violation(iLineNumber)
                try:
                    self.dFix['violations'][iLineNumber].append(sWord)
                except KeyError:
                    self.dFix['violations'][iLineNumber] = []
                    self.dFix['violations'][iLineNumber].append(sWord)


def get_replacement_word(self, sWord):
    for sNewWord in self.dDatabase['type']:
        if sNewWord.lower() == sWord.lower():
            return sNewWord
