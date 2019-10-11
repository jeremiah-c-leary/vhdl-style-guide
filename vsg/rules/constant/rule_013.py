
from vsg import rule
from vsg import utils


class rule_013(rule.rule):
    '''
    General rule 013 checks capitalization consistency of constant names.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'constant', '013')
        self.fixable = True
        self.solution = 'Inconsistent capitalization of word'
        self.phase = 6
        self.lLowerCaseWords = []
        self.lCaseWords = []
        self.dDatabase = create_database()

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isConstant:
            self.dDatabase['constant'].append(utils.extract_class_identifier_list(oLine)[0])
        if oLine.insideArchitecture:
            if oLine.insideProcess:
                lWords = extract_word_list(oLine)
                check_violations(self, lWords, iLineNumber)
            if oLine.isInstantiationPortAssignment:
                lWords = extract_word_list(oLine)
                check_violations(self, lWords, iLineNumber)
            if oLine.insideConcurrent:
                lWords = extract_word_list(oLine)
                check_violations(self, lWords, iLineNumber)
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
        if len(self.dFix['violations'][iLineNumber]) > 1:
            sSolution = self.solution + 's: ' + ', '.join(self.dFix['violations'][iLineNumber])
        else:
            sSolution = self.solution + ': ' + ', '.join(self.dFix['violations'][iLineNumber])
        return sSolution


def create_database():

    dDatabase = {}
    dDatabase['constant'] = []

    return dDatabase


def extract_word_list(oLine):

    if oLine.isProcessKeyword:
        sLine = oLine.line[oLine.line.find(':'):]
    elif oLine.isInstantiationPortAssignment:
        sLine = oLine.line[oLine.line.find('=>'):]
    else:
        sLine = oLine.line

    return utils.extract_non_keywords(sLine)


def check_violations(self, lWords, iLineNumber):

    for sWord in lWords:
        if sWord.lower() in map(str.lower, self.dDatabase['constant']):
            if sWord not in self.dDatabase['constant']:
                self.add_violation(iLineNumber)
                try:
                    self.dFix['violations'][iLineNumber].append(sWord)
                except KeyError:
                    self.dFix['violations'][iLineNumber] = []
                    self.dFix['violations'][iLineNumber].append(sWord)


def get_replacement_word(self, sWord):
    for sNewWord in self.dDatabase['constant']:
        if sNewWord.lower() == sWord.lower():
            return sNewWord
