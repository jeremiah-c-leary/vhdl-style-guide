
from vsg import rule
import re


class port_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'port'


class rule_001(port_rule):
    '''Port rule 001 checks for a blank line above the port keyword.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Remove blank lines above "port" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                self._is_no_blank_line_before(oFile, iLineNumber)


class rule_002(port_rule):
    '''Port rule 002 checks indentation of the "port" keyword.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                self._check_indent(oLine, iLineNumber)


class rule_003(port_rule):
    '''Port rule 003 checks spacing between "port" and the open parenthesis.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Change spacing between "port" and "(" to one space.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                if not re.match('^\s*\S+\s\(', oLine.line):
                    self.add_violation(iLineNumber)


class rule_004(port_rule):
    '''Port rule 004 checks indentation of ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and not oLine.isEndPortMap:
                self._check_indent(oLine, iLineNumber)


class rule_005(port_rule):
    '''Port rule 005 checks for a single space after the colon in a port declaration for "in" and "inout" ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Reduce number of spaces after the colon to 1.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*in', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\sin', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_006(port_rule):
    '''Port rule 006 checks for one space after the colon in a port declaration for "out" ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Change number of spaces before "out" to 3.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*out', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\sout', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_007(port_rule):
    '''Port rule 007 checks for four spaces after the "in" keyword in a port declaration for "in" ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Change the number of spaces after the "in" keyword to four spaces.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*in\s', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\s*in\s\s\s\s\S+', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_008(port_rule):
    '''Port rule 008 checks for three spaces after "out" keyword in a port declaration for "out" ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Change the number of spaces after the "out" keyword to three spaces.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*out', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\s*out\s\s\s\S+', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_009(port_rule):
    '''Port rule 009 checks for a single space after "inout" keyword in a port declaration for "inout" ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Change the number of spaces after the "inout" keyword to one space.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*inout', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\s*inout\s\S+', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_010(port_rule):
    '''Port rule 010 checks port names are uppercase.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Uppercase port name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                self._is_uppercase(self._get_first_word(oLine), iLineNumber)


class rule_011(port_rule):
    '''Port rule 011 checks port names have I_, O_ or IO_ prefixes.

         The valid options for self.port_direction are:
            None (default)   No checks are made.
            Prefix           Checks for I_, O_, and IO_ in front of port names.
            Suffix           Checks for _I, _O, and _IO at the end of port names.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Add proper prefix or suffix indicating port direction.'
        self.port_direction = None
        self.phase = 7

    def analyze(self, oFile):
        if not self.port_direction:
            self.violations = []
        if self.port_direction == 'Prefix':
            self.solution = 'Add proper prefix indicating port direction.'
        if self.port_direction == 'Suffix':
            self.solution = 'Add proper suffix indicating port direction.'

        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and oLine.insideEntity:
                lLine = oLine.lineLower.split()
                if self.port_direction == 'Prefix':
                    if not(lLine[0].startswith('i_') or lLine[0].startswith('o_') or lLine[0].startswith('io_')):
                        self.add_violation(iLineNumber)
                if self.port_direction == 'Suffix':
                    if not(lLine[0].endswith('_i') or lLine[0].endswith('_o') or lLine[0].endswith('_io') or \
                           lLine[0].endswith('_i,') or lLine[0].endswith('_o,') or lLine[0].endswith('_io,')):
                        self.add_violation(iLineNumber)


class rule_012(port_rule):
    '''Port rule 012 checks for default assignments in port declarations.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Remove default assignment in port declaration'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^.*:=', oLine.line):
                    self.add_violation(iLineNumber)


class rule_013(port_rule):
    '''Port rule 013 checks for multiple ports declared on single line.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Place multiple ports on their own lines.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^.*,.*:', oLine.line):
                    self.add_violation(iLineNumber)


class rule_014(port_rule):
    '''Port rule 014 checks the closing parenthesis for ports are on a line by itself.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Closing parenthesis must be on a line by itself and above the "end" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndPortMap:
                if not re.match('^\s*\)', oLine.line):                 
                    self.add_violation(iLineNumber)


class rule_015(port_rule):
    '''Port rule 015 checks the indentation of closing parenthesis for port maps.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndPortMap and not oLine.isPortDeclaration:
                self._check_indent(oLine, iLineNumber)


class rule_016(port_rule):
    '''Port rule 016 checks for a port definition on the same line as the port keyword.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Move port definition to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                if re.match('^\s*port\s*\(\s*\S+\s*:', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_017(port_rule):
    '''Port rule 017 checks the "port" keyword is lowercase.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '017'
        self.solution = 'Change "port" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                if not re.match('^\s*port', oLine.line):
                    self.add_violation(iLineNumber)


class rule_018(port_rule):
    '''Port rule 018 checks the port type is lowercase.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '018'
        self.solution = 'Change port type to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                sLine = oLine.line.split(':')[1]
                if '(' in sLine:
                    sLine = sLine.split('(')[0]
                    self._is_lowercase(sLine, iLineNumber)
                else:
                    self._is_lowercase(sLine.split()[1],iLineNumber)


class rule_019(port_rule):
    '''Port rule 019 checks the port direction is lowercase.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '019'
        self.solution = 'Change port direction to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                sLine = oLine.line.split(':')[1]
                self._is_lowercase(sLine.split()[0],iLineNumber)


class rule_020(port_rule):
    '''Port rule 020 checks there is at least one space before the :.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '020'
        self.solution = 'Add a space before the :.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if not re.match('^.*\s+:',oLine.line):
                    self.add_violation(iLineNumber)

