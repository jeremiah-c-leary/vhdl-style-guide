
from vsg import rule
from vsg import line
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

    def fix(self,oFile):
        self._fix_indent(oFile)


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

    def fix(self, oFile):
        self.analyze(oFile)
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'signal')
        self._clear_violations()


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

    def fix(self, oFile):
        self.analyze(oFile)
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'signal')
        self._clear_violations()


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

    def fix(self, oFile):
        self.analyze(oFile)
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[1])
        self._clear_violations()


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

    def fix(self, oFile):
        self.analyze(oFile)
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], ':')
        self._clear_violations()


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

    def fix(self, oFile):
        self.analyze(oFile)
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], ':')
        self._clear_violations()

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

    def fix(self, oFile):
        ''' This rule will not be automatically fixed.'''
        return


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
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isEndArchitecture:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, ':', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isSignal:
                  lGroup.append(oLine)
                else:
                  lGroup.append(line.line('Removed line'))

    def fix(self, oFile):
        self._fix_keyword_alignment(oFile)


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

    def fix(self, oFile):
        self.analyze(oFile)
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line.split()[3]
            if '(' in sLine:
                self._lower_case(oLine, sLine.split('(')[0])
            else:
                self._lower_case(oLine, sLine.split()[3])

        self._clear_violations()
