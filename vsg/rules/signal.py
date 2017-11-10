
from vsg import rule
import re


class signal_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'signal'


class rule_001(signal_rule):
    '''Signal rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                self._check_indent(oLine, iLineNumber)


class rule_002(signal_rule):
    '''Signal rule 002 checks the "signal" keyword is lowercase.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Lowercase "signal" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)


class rule_003(signal_rule):
    '''Signal rule 003 checks there is a single space after the "signal" keyword.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove all but one space after the "signal" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if not re.match('^\s*signal\s\w', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_004(signal_rule):
    '''Signal rule 004 checks the signal name is lowercase.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change signal name to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                self._is_lowercase(oLine.line.split()[1], iLineNumber)


class rule_005(signal_rule):
    '''Signal rule 005 checks there is a single space after the colon.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure only a signal space after the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if not re.match('^\s*signal\s+.*\s*:\s\S', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_006(signal_rule):
    '''Signal rule 006 checks there is at least a single space before the colon.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Add a single space before the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if re.match('^\s*signal\s+.*\S:', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_007(signal_rule):
    '''Signal rule 007 checks for default assignments in signal declarations.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove default assignment.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if ':=' in oLine.line:
                    self.add_violation(iLineNumber)


class rule_008(signal_rule):
    '''Signal rule 008 checks for prefixes in signal names.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Remove default assignment.'
        self.prefixes = None
        self.phase = 7

    def analyze(self, oFile):
        if not self.prefixes:
            return
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isSignal:
                continue
            for sSignalName in oLine.line.split(':')[0].split():
                if sSignalName.lower() == 'signal':
                    continue
                fPrefixFound = False
                for sPrefixName in self.prefixes:
                    if sSignalName.startswith(sPrefixName):
                        fPrefixFound = True
                        break
                if not fPrefixFound:
                    self.add_violation(iLineNumber)


class rule_009(signal_rule):
    '''Signal rule 009 checks the colons are in the same column for all signals.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Align colon with right most colon.'
        self.phase = 5

    def analyze(self, oFile):
        iMaximumColumn = 0
        # Search for the largest column that contains the first colon
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isSignal:
                continue
            iCurrentColumn = oLine.line.find(':')
            if iMaximumColumn < iCurrentColumn:
                iMaximumColumn = iCurrentColumn
        self.solution = 'Align colon to column ' + str(iMaximumColumn + 1) + '.'
        # Compare each signals colon column to the largest found
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isSignal:
                continue
            iCurrentColumn = oLine.line.find(':')
            if not iMaximumColumn == oLine.line.find(':'):
                self.add_violation(iLineNumber)


class rule_010(signal_rule):
    '''Signal rule 010 checks the signal type is lowercase.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Change signal type to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if re.match('^\s*signal\s+\w+\s+:\s+\w', oLine.lineLower):
                    sLine = oLine.line.split()[3]
                    if '(' in sLine:
                        self._is_lowercase(sLine.split('(')[0], iLineNumber)
                    else:
                        self._is_lowercase(oLine.line.split()[3], iLineNumber)

