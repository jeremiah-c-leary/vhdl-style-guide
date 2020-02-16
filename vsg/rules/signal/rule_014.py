
from vsg import rule
from vsg import utils


class rule_014(rule.rule):
    '''
    Signal rule 014 checks capitalization consistency of signal names.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'signal', '014')
        self.fixable = True
        self.solution = 'Inconsistent capitalization of signal'
        self.phase = 6
        self.dDatabase = create_database()

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isSignal:
            self.dDatabase['signal'].extend(utils.extract_class_identifier_list(oLine))
        if oLine.insideArchitecture:
            if oLine.insideProcess and not oLine.isEndProcess and not oLine.isProcessDeclarative:
                lWords = extract_word_list(oLine)
                check_violations(self, lWords, iLineNumber)
            if oLine.isInstantiationPortAssignment:
                lWords = extract_word_list(oLine)
                check_violations(self, lWords, iLineNumber)
            if oLine.insideConcurrent:
                lWords = extract_word_list(oLine)
                check_violations(self, lWords, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            sWord = dViolation['signal']
            iLineNumber = dViolation['lineNumber']
            sReplacementWord = get_replacement_word(self, sWord)
            if oFile.lines[iLineNumber].isInstantiationPortAssignment:
                oLine = oFile.lines[iLineNumber]
                sLine = oLine.line
                iIndex = sLine.index('>')
                oLine.update_line(sLine[iIndex:])
                utils.change_word(oLine, sWord, sReplacementWord, 20)
                sNewLine = sLine[0:iIndex] + oLine.line
                oFile.lines[iLineNumber].update_line(sNewLine)
            else:
                utils.change_word(oFile.lines[iLineNumber], sWord, sReplacementWord, 20)

    def _get_solution(self, iLineNumber):
        lSignals = []
        for dViolation in self.violations:
            if dViolation['lineNumber'] == iLineNumber:
                lSignals.append(dViolation['signal'])
        if len(lSignals) > 1:
            sSolution = self.solution + 's: ' + ', '.join(lSignals)
        else:
            sSolution = self.solution + ': ' + lSignals[0]
        return sSolution


def create_database():

    dDatabase = {}
    dDatabase['signal'] = []

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
        if sWord.lower() in map(str.lower, self.dDatabase['signal']):
            if sWord not in self.dDatabase['signal']:
                dViolation = utils.create_violation_dict(iLineNumber)
                dViolation['signal'] = sWord
                self.add_violation(dViolation)
#                try:
#                    self.dFix['violations'][iLineNumber].append(sWord)
#                except KeyError:
#                    self.dFix['violations'][iLineNumber] = []
#                    self.dFix['violations'][iLineNumber].append(sWord)


def get_replacement_word(self, sWord):
    for sNewWord in self.dDatabase['signal']:
        if sNewWord.lower() == sWord.lower():
            return sNewWord
