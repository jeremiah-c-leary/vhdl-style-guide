
import rule
import re


class entity_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'


class rule_001(entity_rule):
    '''Entity rule 001 checks for spaces before the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '001'
        self.description = 'Remove spaces before entity keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s\s*entity', sLine.lower()):
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_002(entity_rule):
    '''Entity rule 002 checks for a single space after the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '002'
        self.description = 'Remove extra spaces after entity keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity\s\s+', sLine.lower()):
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_003(entity_rule):
    '''Entity rule 003 checks for a blank line above the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '003'
        self.description = 'Add blank line above entity keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity', sLine.lower()):
                if not re.match('^\s*$', lines[iLineNumber - 1]):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_004(entity_rule):
    '''Entity rule 004 checks the entity keyword is lower case.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '004'
        self.description = 'Change entity keyword to lowercase.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity', sLine.lower()):
                if not re.match('^\s*entity', sLine):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_005(entity_rule):
    '''Entity rule 005 checks the is keyword is on the same line as the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '005'
        self.description = 'Add "is" keyword to same line as "entity" keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity', sLine.lower()):
                if not re.match('^.*\s\s*is', sLine.lower()):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines

class rule_006(entity_rule):
    '''Entity rule 006 checks the "is" keyword is lower case.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '006'
        self.description = 'Change entity keyword to lowercase.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity', sLine.lower()):
                if not re.match('^.*\s\s*is', sLine):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines

class rule_007(entity_rule):
    '''Entity rule 007 checks for a single space before the "is" keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '007'
        self.description = 'Remove extra spaces before "is" keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity', sLine.lower()):
                if re.match('^.*\s\s+is', sLine.lower()):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


#class rule_007(entity_rule):
#    '''Entity rule 007 checks for a blank line above the entity keyword.'''
#
#    def __init__(self):
#        entity_rule.__init__(self)
#        self.identifier = '007'
#        self.description = 'Remove blank line above use keyword.'
#
#    def analyze(self, lines):
#        lFailureLines = []
#        for iLineNumber, sLine in enumerate(lines):
#            if re.match('^\s*use', sLine.lower()):
#                if re.match('^\s*$', lines[iLineNumber - 1]):
#                    lFailureLines.append(iLineNumber + 1)
#        self.violations = lFailureLines
#
#
#class rule_008(entity_rule):
#    '''Entity rule 008 checks indentation of the use keyword.'''
#
#    def __init__(self):
#        entity_rule.__init__(self)
#        self.identifier = '008'
#        self.description = 'Change indent of use keyword to 2 spaces.'
#
#    def analyze(self, lines):
#        lFailureLines = []
#        for iLineNumber, sLine in enumerate(lines):
#            if re.match('^\s*use', sLine.lower()):
#                if not re.match('^\s\suse', sLine.lower()):
#                    lFailureLines.append(iLineNumber + 1)
#        self.violations = lFailureLines
