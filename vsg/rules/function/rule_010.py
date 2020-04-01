
from vsg import rule
from vsg import utils


class rule_010(rule.rule):
    '''
    General rule 010 checks capitalization consistency of function names.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'function', '010')
        self.fixable = True
        self.solution = 'Inconsistent capitalization of word'
        self.phase = 6
        self.dDatabase = create_database()

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isFunctionKeyword:
            self.dDatabase['function'].append(oLine.line.split()[1])  # TODO: Think if this can be solved in better way.
        if oLine.insideArchitecture:
            if oLine.insideProcess or oLine.insideConcurrent:
                lWords = extract_word_list(oLine)
                check_violations(self, lWords, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            sWord = dViolation['name']
            sReplacementWord = get_replacement_word(self, sWord)
            utils.change_word(utils.get_violating_line(oFile, dViolation), sWord, sReplacementWord, 20)

    def _get_solution(self, iLineNumber):
        lFunctions = []
        for dViolation in self.violations:
            if iLineNumber == utils.get_violation_linenumber(dViolation):
                lFunctions.append(dViolation['name'])
        if len(lFunctions) > 1:
            sSolution = self.solution + 's: ' + ', '.join(lFunctions)
        else:
            sSolution = self.solution + ': ' + lFunctions[0]
        return sSolution


def create_database():

    dDatabase = {}
    dDatabase['function'] = []

    return dDatabase


def extract_word_list(oLine):

    sLine = oLine.line

    lWords = utils.extract_non_keywords(sLine)
    return lWords


def check_violations(self, lWords, iLineNumber):
    for sWord in lWords:
        if sWord.lower() in map(str.lower, self.dDatabase['function']):
            if sWord not in self.dDatabase['function']:
                dViolation = utils.create_violation_dict(iLineNumber)
                dViolation['name'] = sWord
                self.add_violation(dViolation)
#                try:
#                    self.dFix['violations'][iLineNumber].append(sWord)
#                except KeyError:
#                    self.dFix['violations'][iLineNumber] = []
#                    self.dFix['violations'][iLineNumber].append(sWord)


def get_replacement_word(self, sWord):
    for sNewWord in self.dDatabase['function']:
        if sNewWord.lower() == sWord.lower():
            return sNewWord
