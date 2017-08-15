
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
        self.description = 'Change "entity" keyword to lowercase.'

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
        self.description = 'Change "is" keyword to lowercase.'

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


class rule_008(entity_rule):
    '''Entity rule 008 checks for a "entity" in the line above the port keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '008'
        self.description = 'Remove lines between port and entity keywords.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*port', sLine.lower()):
                if not re.match('^\s*entity', lines[iLineNumber - 1].lower()):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_009(entity_rule):
    '''Entity rule 009 checks indentation of the "port" keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '009'
        self.description = 'Change indent of "port" keyword to 2 spaces.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*port', sLine.lower()):
                if not re.match('^\s\sport', sLine.lower()):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_010(entity_rule):
    '''Entity rule 010 checks spacing between "port" and the open parenthesis.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '010'
        self.description = 'Change spacing between "port" and "(" to one space.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*port', sLine.lower()):
                if not re.match('^\s*port \(', sLine.lower()):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_011(entity_rule):
    '''Entity rule 011 checks indentation of ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '011'
        self.description = 'Change indent of "port" keyword to 4 spaces.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    break
            if fPortMapFound:
                if not re.match('^\s*$', sLine):
                    if not re.match('^\s\s\s\s\w', sLine):
                        lFailureLines.append(iLineNumber + 1)
            if re.match('^\s*port', sLine.lower()) and fEntityFound:
                fPortMapFound = True
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_012(entity_rule):
    '''Entity rule 012 checks for a single space after the colon in a port declaration for "in" ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '012'
        self.description = 'Reduce number of spaces after the colon to 1.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    break
            if fPortMapFound:
                if not re.match('^\s*$', sLine):
                    if re.match('^.*:\s*in', sLine.lower()):
                        if not re.match('^.*:\sin', sLine.lower()):
                            lFailureLines.append(iLineNumber + 1)
            if re.match('^\s*port', sLine.lower()) and fEntityFound:
                fPortMapFound = True
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_013(entity_rule):
    '''Entity rule 013 checks for three spaces after the colon in a port declaration for "out" ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '013'
        self.description = 'Change number of spaces before "out" to 3.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    break
            if fPortMapFound:
                if not re.match('^\s*$', sLine):
                    if re.match('^.*:\s*out', sLine.lower()):
                        if not re.match('^.*:\s\s\sout', sLine.lower()):
                            lFailureLines.append(iLineNumber + 1)
            if re.match('^\s*port', sLine.lower()) and fEntityFound:
                fPortMapFound = True
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_014(entity_rule):
    '''Entity rule 014 checks for four spaces after the "in" keyword in a port declaration for "in" ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '014'
        self.description = 'Change the number of spaces after the "in" keyword to four spaces.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    break
            if fPortMapFound:
                if not re.match('^\s*$', sLine):
                    if re.match('^.*:\s*in\s', sLine.lower()):
                        if not re.match('^.*:\s*in\s\s\s\s\w', sLine.lower()):
                            lFailureLines.append(iLineNumber + 1)
            if re.match('^\s*port', sLine.lower()) and fEntityFound:
                fPortMapFound = True
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_015(entity_rule):
    '''Entity rule 015 checks for a single space after "out" keyword in a port declaration for "out" ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '015'
        self.description = 'Change the number of spaces after the "out" keyword to one space.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    break
            if fPortMapFound:
                if not re.match('^\s*$', sLine):
                    if re.match('^.*:\s*out\s', sLine.lower()):
                        if not re.match('^.*:\s*out\s\w', sLine.lower()):
                            lFailureLines.append(iLineNumber + 1)
            if re.match('^\s*port', sLine.lower()) and fEntityFound:
                fPortMapFound = True
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_016(entity_rule):
    '''Entity rule 016 checks for a single space after "inout" keyword in a port declaration for "inout" ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '016'
        self.description = 'Change the number of spaces after the "inout" keyword to one space.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    break
            if fPortMapFound:
                if not re.match('^\s*$', sLine):
                    if re.match('^.*:\s*inout\s', sLine.lower()):
                        if not re.match('^.*:\s*inout\s\w', sLine.lower()):
                            lFailureLines.append(iLineNumber + 1)
            if re.match('^\s*port', sLine.lower()) and fEntityFound:
                fPortMapFound = True
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines

