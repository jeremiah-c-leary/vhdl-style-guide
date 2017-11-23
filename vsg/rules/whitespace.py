
from vsg import rule
import re


class whitespace_rule(rule.rule):

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'whitespace'
        self.phase = 2


class rule_001(whitespace_rule):
    '''Whitespace rule 001 checks spaces at the end of lines.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Remove trailing whitespace.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.line.endswith(' '):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'\s+$', '', oLine.line))


class rule_002(whitespace_rule):
    '''Whitespace rule 002 checks for tabs in lines'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Replace tabs with spaces.'
        self.phase = 0

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if '\t' in oLine.line:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.replace('\t', '  '))


class rule_003(whitespace_rule):
    '''Whitespace rule 003 checks for spaces before semicolons'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove spaces before semicolons.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if ' ;' in oLine.line:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'(\s+;)', r';', oLine.line))


class rule_004(whitespace_rule):
    '''Whitespace rule 004 checks for spaces before commas.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Remove spaces before commas.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if ' ,' in oLine.line:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'(\s+,)', r',', oLine.line))


class rule_005(whitespace_rule):
    '''Whitespace rule 005 checks for spaces after an open parenthesis.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Remove spaces after open (.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComment:
                continue
            if oLine.hasComment:
                sLine = oLine.line[:oLine.line.find('--')]
            else:
                sLine = oLine.line
            if re.match('^.*\(\s+', sLine):
                if not re.match('^.*\(\s+[0-9]', sLine):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iCommentIndex = oLine.line.find('--')
            if iCommentIndex == -1:
                oLine.update_line(re.sub(r'\((\s+)([A-Za-z_\(])', r'(\2', oLine.line))
            else:
                sLine = oLine.line[:iCommentIndex]
                sLine = re.sub(r'\((\s+)([A-Za-z_\(])', r'(\2', sLine)
                sLine = sLine + oLine.line[iCommentIndex:]
                oLine.update_line(sLine)


class rule_006(whitespace_rule):
    '''Whitespace rule 006 checks for spaces after an open parenthesis.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Remove spaces before close ).'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.hasComment:
                sLine = oLine.line[:oLine.line.find('--')]
            else:
                sLine = oLine.line
            if re.match('^.*\s+\)', sLine) and not re.match('^\s+\)', sLine):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iCommentIndex = oLine.line.find('--')
            if iCommentIndex == -1:
                oLine.update_line(re.sub(r'\s+\)', r')', oLine.line))
            else:
                sLine = oLine.line[:iCommentIndex]
                sLine = re.sub(r'\s+\)', r')', sLine)
                sLine = sLine + oLine.line[iCommentIndex:]
                oLine.update_line(sLine)


class rule_007(whitespace_rule):
    '''Whitespace rule 007 checks for spaces after a comma.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Add a space after the comma.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if re.match('^.*,\S', oLine.line) and not re.match('^.*--.*,\S', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r',(\S)', r', \1', oLine.line))
