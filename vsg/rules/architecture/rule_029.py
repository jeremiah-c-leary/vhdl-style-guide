from vsg import rule
from vsg import utils


class rule_029(rule.rule):
    '''
    Architecture rule 029 checks the alignment of declaration identifiers in the architecture declarative region.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '029')
        self.phase = 5
#        self.solution = _get_solution

    def _pre_analyze(self):
        self.bGroupFound = False
        self.lGroup = []

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideArchitectureDeclarativeRegion:
            if isDeclaration(oLine):
                self.bGroupFound = True
            if self.bGroupFound:
                if oLine.isBlank or oLine.isComment:
                    analyzeGroup(self, self.lGroup)
                    self._pre_analyze()
                else:
                    if isDeclaration(oLine):
                        self.lGroup.append([oLine, iLineNumber])
        
    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            iNewSpaces = dViolation['columnAdjust'] + len(oLine.separators[1])
            oLine.separators[1] = ' ' * iNewSpaces
            oLine.update_line_from_tokens()


    def _get_solution(self, iLineNumber):
        for dViolation in self.violations:
            if dViolation['lines'][0]['number'] == iLineNumber:
                return 'Move identifier to column ' + str(dViolation['targetColumn'] + 1)
        return 'Unknown'

def isDeclaration(oLine):
    if oLine.isSignal or oLine.isConstant or oLine.isVariable or oLine.isSubtypeKeyword or oLine.isTypeKeyword or oLine.isFileKeyword:
        return True
    return False


def analyzeGroup(self, lLines):
    iTargetColumn = length_of_longest_declaration_keyword(lLines) + 1
    for oLine, iLineNumber in lLines:
        iCurrentColumn = len(oLine.tokens[0]) + len(oLine.separators[1])
        if not iCurrentColumn == iTargetColumn:
            dViolation = utils.create_violation_dict(iLineNumber)
            dViolation['columnAdjust'] = iTargetColumn - iCurrentColumn
            dViolation['targetColumn'] = len(oLine.separators[0]) + iTargetColumn
            self.add_violation(dViolation)


def length_of_longest_declaration_keyword(lGroup):
    iReturn = 0
    for oLine, iLineNumber in lGroup:
        iReturn = max(iReturn, len(oLine.tokens[0]))
    return iReturn

