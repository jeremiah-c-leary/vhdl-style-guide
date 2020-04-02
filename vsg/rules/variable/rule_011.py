
from vsg import rule
from vsg import utils


class rule_011(rule.rule):
    '''
    Variable rule 011 checks capitalization consistency of variable names.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'variable', '011')
        self.fixable = True
        self.solution = 'Inconsistent capitalization of word'
        self.phase = 6
        self.lLowerCaseWords = []
        self.lCaseWords = []
        self.dDatabase = create_database()

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isVariable:
            self.dDatabase['variable'].append(utils.extract_class_identifier_list(oLine)[0])
        if oLine.insideProcess:
            lWords = extract_word_list(oLine)
            check_violations(self, lWords, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            sWord = dViolation['variable']
            iLineNumber = utils.get_violation_line_number(dViolation)
            sReplacementWord = get_replacement_word(self, sWord)
            utils.change_word(oFile.lines[iLineNumber], sWord, sReplacementWord, 20)

    def _get_solution(self, iLineNumber):
        lVariables = []
        for dViolation in self.violations:
            if utils.get_violation_line_number(dViolation) == iLineNumber:
                lVariables.append(dViolation['variable'])
        if len(lVariables) > 1:
            sSolution = self.solution + 's: ' + ', '.join(lVariables)
        else:
            sSolution = self.solution + ': ' + lVariables[0]
        return sSolution


def create_database():

    dDatabase = {}
    dDatabase['variable'] = []

    return dDatabase


def extract_word_list(oLine):

    sLine = oLine.line

    return utils.extract_non_keywords(sLine)


def check_violations(self, lWords, iLineNumber):

    for sWord in lWords:
        if sWord.lower() in map(str.lower, self.dDatabase['variable']):
            if sWord not in self.dDatabase['variable']:
                dViolation = utils.create_violation_dict(iLineNumber)
                dViolation['variable'] = sWord
                self.add_violation(dViolation)


def get_replacement_word(self, sWord):
    for sNewWord in self.dDatabase['variable']:
        if sNewWord.lower() == sWord.lower():
            return sNewWord
