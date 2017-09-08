
import rule
import re


def is_entity(fFlag, oLine):
    if re.match('\s*entity', oLine.lower()):
        return True
    return fFlag


class port_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'port'


class rule_001(port_rule):
    '''Entity rule 001 checks for a blank line above the port keyword.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Remove blank lines above "port" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                if oFile.lines[iLineNumber - 1].isBlank:
                    self.add_violation(iLineNumber)


class rule_002(port_rule):
    '''Entity rule 002 checks indentation of the "port" keyword.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Change indent of "port" keyword to 2 spaces.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                self._checkIndent(oLine, iLineNumber)


class rule_003(port_rule):
    '''Entity rule 003 checks spacing between "port" and the open parenthesis.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Change spacing between "port" and "(" to one space.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                if not re.match('^\s*\S+\s\(', oLine.line):
                    self.add_violation(iLineNumber)


class rule_004(port_rule):
    '''Entity rule 004 checks indentation of ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change indent of port to 4 spaces.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and not oLine.isEndPortMap:
                self._checkIndent(oLine, iLineNumber)


class rule_005(port_rule):
    '''Entity rule 005 checks for a single space after the colon in a port declaration for "in" and "inout" ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Reduce number of spaces after the colon to 1.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*in', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\sin', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_006(port_rule):
    '''Entity rule 006 checks for one space after the colon in a port declaration for "out" ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Change number of spaces before "out" to 3.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*out', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\sout', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_007(port_rule):
    '''Entity rule 007 checks for four spaces after the "in" keyword in a port declaration for "in" ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Change the number of spaces after the "in" keyword to four spaces.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*in\s', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\s*in\s\s\s\s\S+', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_008(port_rule):
    '''Entity rule 008 checks for three spaces after "out" keyword in a port declaration for "out" ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Change the number of spaces after the "out" keyword to three spaces.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*out', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\s*out\s\s\s\S+', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_009(port_rule):
    '''Entity rule 009 checks for a single space after "inout" keyword in a port declaration for "inout" ports.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Change the number of spaces after the "inout" keyword to one space.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*inout', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\s*inout\s\S+', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_010(port_rule):
    '''Entity rule 010 checks port names are uppercase.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Uppercase port name.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                lLine = oLine.line.split()
                if lLine[0] != lLine[0].upper():
                    self.add_violation(iLineNumber)


class rule_011(port_rule):
    '''Entity rule 011 checks port names have I_, O_ or IO_ prefixes.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Add proper prefix or suffix indicating port direction.'
        self.port_direction = 'Prefix'

    def configure(self, dConfig):
        if 'port_direction' in dConfig['entity']['rule_011']:
            self.port_direction = dConfig['entity']['rule_011']['port_direction']

    def analyze(self, oFile):
        if not self.port_direction:
            self.violations = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                lLine = oLine.lineLower.split()
                if self.port_direction == 'Prefix':
                    if not(lLine[0].startswith('i_') or lLine[0].startswith('o_') or lLine[0].startswith('io_')):
                        self.add_violation(iLineNumber)
                if self.port_direction == 'Suffix':
                    if not(lLine[0].endswith('_i') or lLine[0].endswith('_o') or lLine[0].endswith('_io') or \
                           lLine[0].endswith('_i,') or lLine[0].endswith('_o,') or lLine[0].endswith('_io,')):
                        self.add_violation(iLineNumber)


class rule_012(port_rule):
    '''Entity rule 012 checks for default assignments in port declarations.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Remove default assignment in port declaration'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^.*:=', oLine.line):
                    self.add_violation(iLineNumber)


class rule_013(port_rule):
    '''Entity rule 013 checks for multiple ports declared on single line.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Place multiple ports on their own lines.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^.*,.*:', oLine.line):
                    self.add_violation(iLineNumber)


class rule_014(port_rule):
    '''Entity rule 014 checks the closing parenthesis for ports are on a line by itself.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Closing parenthesis must be on a line by itself and above the "end" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndPortMap:
                if not re.match('^\s*\)', oLine.line):                 
                    self.add_violation(iLineNumber)


class rule_015(port_rule):
    '''Entity rule 015 checks the indentation of closing parenthesis for port maps.'''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Indention of closing parenthesis should be two spaces.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndPortMap and not oLine.isPortDeclaration:
                self._checkIndent(oLine, iLineNumber)

