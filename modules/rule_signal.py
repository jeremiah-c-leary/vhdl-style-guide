
import rule
import re

#TODO:
# check signal name is lower case
# check signal name prefixes
# check for single space after : to signal type
# check for := assignment
# check for alignment of :'s across multiple lines

class signal_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'signal'

    def _isSignal(self, sString):
        return re.match('^\s*signal', sString.lower())


class rule_001(signal_rule):
    '''Signal rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure there are only two spaces before signal keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isSignal(sLine):
                if not re.match('^\s\ssignal', sLine.lower()):
                    self.add_violation(iLineNumber)


class rule_002(signal_rule):
    '''Signal rule 002 checks the "signal" keyword is lowercase.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove spaces before signal keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isSignal(sLine):
                if not re.match('^\s*signal', sLine):
                    self.add_violation(iLineNumber)


class rule_003(signal_rule):
    '''Signal rule 003 checks there is a single space after the "signal" keyword.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove all but one space after the "signal" keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isSignal(sLine):
                if not re.match('^\s*signal\s\w', sLine.lower()):
                    self.add_violation(iLineNumber)


class rule_004(signal_rule):
    '''Signal rule 004 checks the signal name is lowercase.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change signal name to lowercase.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isSignal(sLine):
                if not self._isLowercase(sLine.split()[1]):
                    self.add_violation(iLineNumber)


class rule_005(signal_rule):
    '''Signal rule 005 checks there is a single space after the colon.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure only a signal space after the colon.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isSignal(sLine):
                if not re.match('^\s*signal\s+.*\s*:\s\w', sLine.lower()):
                    self.add_violation(iLineNumber)


class rule_006(signal_rule):
    '''Signal rule 006 checks there is at least a single space before the colon.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Add a single space before the colon.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isSignal(sLine):
                if re.match('^\s*signal\s+.*\w:', sLine.lower()):
                    self.add_violation(iLineNumber)


class rule_007(signal_rule):
    '''Signal rule 007 checks for default assignments in signal declarations.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove default assignment.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isSignal(sLine):
                if ':=' in sLine:
                    self.add_violation(iLineNumber)


class rule_008(signal_rule):
    '''Signal rule 008 checks for prefixes in signal names.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Remove default assignment.'
        self.prefixes = None

    def analyze(self, lines):
        if not self.prefixes:
            return
        for iLineNumber, sLine in enumerate(lines):
            if not self._isSignal(sLine):
                continue
            for sSignalName in sLine.split(':')[0].split():
                if sSignalName.lower() == 'signal':
                    continue
                fPrefixFound = False
                for sPrefixName in self.prefixes:
                    if sSignalName.startswith(sPrefixName):
                        fPrefixFound = True
                        break
                if not fPrefixFound:
                    self.add_violation(iLineNumber)


# check for alignment of :'s across multiple lines
