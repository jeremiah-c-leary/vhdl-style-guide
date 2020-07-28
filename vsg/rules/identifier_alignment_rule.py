from vsg import rule
from vsg import utils


class identifier_alignment_rule(rule.rule):
    '''
    Identifier alignment rule checks the alignment of declaration identifiers.
    '''
    def __init__(self, name, identifier, sStartTrigger, sEndTrigger):
        rule.rule.__init__(self, name, identifier)
        self.phase = 5
        self.sStartTrigger = sStartTrigger
        self.sEndTrigger = sEndTrigger
        self.lUnless = []

        self.blank_line_ends_group = True
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = True
        self.configuration.append('comment_line_ends_group')

    def _pre_analyze(self):
        self.bRegionFound = False
        self.bGroupFound = False
        self.lGroup = []

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__[self.sStartTrigger]:
            self.bRegionFound = True
        if self.bRegionFound:
            if isDeclaration(oLine, self.lUnless):
                self.bGroupFound = True
            if self.bGroupFound:
                if is_end_group(self, oLine):
                    analyzeGroup(self, self.lGroup)
                    self.bGroupFound = False
                    self.lGroup = []
                    if oLine.__dict__[self.sEndTrigger]:
                        self.bRegionFound = False
                else:
                    if isDeclaration(oLine, self.lUnless):
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


def isDeclaration(oLine, lUnless):
    '''
    Checks if line meets criteria for being included in an alignment check.
    
    Parameters:

      oLine : (line object)

    Return: (boolean)
    '''
    if oLine.isSignal or oLine.isConstant or oLine.isVariable or oLine.isSubtypeKeyword or oLine.isTypeKeyword or oLine.isFileKeyword or oLine.isAttributeKeyword:
        if len(lUnless) == 0:
            return True
        for sUnless in lUnless:
            if oLine.__dict__[sUnless]:
                return False
        return True
    return False


def is_end_group(self, oLine):
    '''
    Determines boundary of a group of lines.

    Parameters:

      self : (self)

      oLine : (line object)

    Returns: (boolean)
    '''
    if self.blank_line_ends_group:
        if oLine.isBlank:
            return True
    if self.comment_line_ends_group: 
        if oLine.isComment:
            return True
    if oLine.__dict__[self.sEndTrigger]:
        return True
    return False


def analyzeGroup(self, lLines):
    '''
    Checks alignment of identifiers in a group of lines.

    Parameters:

      lLines : (list of line objects)

    Returns: (nothing)
    '''
    iTargetColumn = length_of_longest_declaration_keyword(lLines) + 1
    for oLine, iLineNumber in lLines:
        iCurrentColumn = len(oLine.tokens[0]) + len(oLine.separators[1])
        if not iCurrentColumn == iTargetColumn:
            dViolation = utils.create_violation_dict(iLineNumber)
            dViolation['columnAdjust'] = iTargetColumn - iCurrentColumn
            dViolation['targetColumn'] = len(oLine.separators[0]) + iTargetColumn
            self.add_violation(dViolation)


def length_of_longest_declaration_keyword(lGroup):
    '''
    Finds the longest length of declaration keyword.

    Parameters:

      lGroup : (list of line objects)

    Returns: (integer)
    '''
    iReturn = 0
    for oLine, iLineNumber in lGroup:
        iReturn = max(iReturn, len(oLine.tokens[0]))
    return iReturn

