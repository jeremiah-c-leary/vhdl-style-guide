
from vsg import rule
from vsg import utils


class rule_002(rule.rule):
    '''
    General rule 002 checks capitalization consistency of subtype names.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'subtype', '002')
        self.fixable = True
        self.solution = 'Inconsistent capitalization of word'
        self.phase = 6
        self.lLowerCaseWords = []
        self.lCaseWords = []
        self.dDatabase = create_database()

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isSubtypeKeyword:
            self.dDatabase['subtype'].append(oLine.line.split()[1])  # ToDo: Does it need separate function?
        if oLine.insideArchitecture:
            check_in_constant(self, oLine, iLineNumber)
            check_in_signal(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            sWord = dViolation['subtype']
            iLineNumber = utils.get_violation_linenumber(dViolation)
            sReplacementWord = get_replacement_word(self, sWord)
            utils.change_word(oFile.lines[iLineNumber], sWord, sReplacementWord, 20)

    def _get_solution(self, iLineNumber):
        lTemp = []
        for dViolation in self.violations:
            if iLineNumber == utils.get_violation_linenumber(dViolation):
                lTemp.append(dViolation['subtype'])
        if len(lTemp) > 1:
            sSolution = self.solution + 's: ' + ', '.join(lTemp)
        else:
            sSolution = self.solution + ': ' + lTemp[0]
        return sSolution


def check_in_constant(self, oLine, iLineNumber):
    if oLine.insideConstant:
        lWords = extract_word_list(oLine)
        check_violations(self, lWords, iLineNumber)


def check_in_signal(self, oLine, iLineNumber):
    if oLine.isSignal:
        lWords = extract_word_list(oLine)
        check_violations(self, lWords, iLineNumber)


def create_database():

    dDatabase = {}
    dDatabase['subtype'] = []

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
        if sWord.lower() in map(str.lower, self.dDatabase['subtype']):
            if sWord not in self.dDatabase['subtype']:
                dViolation = utils.create_violation_dict(iLineNumber)
                dViolation['subtype'] = sWord
                self.add_violation(dViolation)


def get_replacement_word(self, sWord):
    for sNewWord in self.dDatabase['subtype']:
        if sNewWord.lower() == sWord.lower():
            return sNewWord
