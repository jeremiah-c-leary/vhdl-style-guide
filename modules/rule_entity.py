
import rule
import re


def is_entity(fFlag, oLine):
    if re.match('\s*entity', oLine.lower()):
        return True
    return fFlag


class entity_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'


class rule_001(entity_rule):
    '''Entity rule 001 checks for spaces before the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Remove spaces before entity keyword.'

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                self._checkIndent(oLine, iLineNumber)


class rule_002(entity_rule):
    '''Entity rule 002 checks for a single space after the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove extra spaces after entity keyword.'

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                if re.match('^\s*\w+\s\s+', oLine.line):
                    self.add_violation(iLineNumber)


class rule_003(entity_rule):
    '''Entity rule 003 checks for a blank line above the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Add blank line above entity keyword.'

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                if not oFile.lines[iLineNumber - 1].isBlank:
                    self.add_violation(iLineNumber)


class rule_004(entity_rule):
    '''Entity rule 004 checks the entity keyword is lower case.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change "entity" keyword to lowercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                if not re.match('^\s*entity', oLine.line):
                    self.add_violation(iLineNumber)


class rule_005(entity_rule):
    '''Entity rule 005 checks the is keyword is on the same line as the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Add "is" keyword to same line as "entity" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                if not re.match('^.*\s\s*is', oLine.lineLower):
                    self.add_violation(iLineNumber)

class rule_006(entity_rule):
    '''Entity rule 006 checks the "is" keyword is lower case.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Change "is" keyword to lowercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    if not re.match('^\s*\S+\s+\S+\s\s*is', oLine.line):
                        self.add_violation(iLineNumber)

class rule_007(entity_rule):
    '''Entity rule 007 checks for a single space before the "is" keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove extra spaces before "is" keyword.'

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                if re.match('^.*\s\s+is', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_008(entity_rule):
    '''Entity rule 008 checks the entity name is uppercase in the entity declaration line.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Change entity name to all uppercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                lLine = oLine.line.split()
                if lLine[1] != lLine[1].upper():
                    self.add_violation(iLineNumber)


class rule_009(entity_rule):
    '''Entity rule 009 checks for spaces before the "end" keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Remove spaces before the "end" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                self._checkIndent(oLine, iLineNumber)


class rule_010(entity_rule):
    '''Entity rule 010 checks the "end" keyword is lowercase.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Change "end" keyword to lowercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                if not re.match('^\s*end', oLine.line):
                    self.add_violation(iLineNumber)


class rule_011(entity_rule):
    '''Entity rule 011 checks for a single space after the "end" keyword'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Reduce spaces after "end" keyword to one.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                if re.match('^\s*\w+\s\s+\w', oLine.line):
                    self.add_violation(iLineNumber)


class rule_012(entity_rule):
    '''Entity rule 012 checks entity name is uppercase in "end" keyword line.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Uppercase entity name.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    if lLine[2] != lLine[2].upper():
                        self.add_violation(iLineNumber)


class rule_013(entity_rule):
    '''Entity rule 013 checks for a single space after the "entity" keyword in the closing of the entity.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Reduce spaces after "entity" keyword to one.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                if re.match('^\s*\S+\s\s*\S+\s\s+', oLine.line):
                    self.add_violation(iLineNumber)


class rule_014(entity_rule):
    '''Entity rule 014 checks the "entity" keyword is lower case in the closing of the entity.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Change "entity" keyword to lower case.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                lLine = oLine.line.split()
                if len(lLine) >= 3:
                    if not lLine[1] == 'entity':
                        self.add_violation(iLineNumber)


class rule_015(entity_rule):
    '''Entity rule 015 checks the "end" keyword, "entity" keyword, and entity name are on the same line.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'The "end" keyword, "entity" keyword and entity name need to be on the same line.'

    def analyze(self, oFile):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                lLine = oLine.line.split()
                if not len(lLine) >= 3:
                    if not (lLine[0] == 'end' and lLine[1] == 'entity' and not lLine[2].startswith('--')):
                        self.add_violation(iLineNumber)
