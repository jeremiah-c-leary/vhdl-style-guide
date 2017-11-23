
from vsg import rule
import re


class package_rule(rule.rule):

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'package'


class rule_001(package_rule):
    '''
    Package rule 001 checks for spaces at the beginning of the line.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword or oLine.isPackageEnd:
                self._check_indent(oLine, iLineNumber)

    def fix(self, oFile):
        self._fix_indent(oFile)


class rule_002(package_rule):
    '''
    Package rule 002 checks for a single space between "package" and "is" keywords.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove extra spaces between keywords.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                if len(oLine.line.split()) > 2:
                    if re.match('^\s*package\s+\S+\s+is', oLine.lineLower):
                        if not re.match('^\s*package\s\S+\sis', oLine.lineLower):
                            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'package')
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], 'is')


class rule_003(package_rule):
    '''
    Package rule 003 checks for a blank line above the package keyword.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Add blank line above package keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                self._is_blank_line_before(oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)


class rule_004(package_rule):
    '''
    Package rule 004 checks the package keyword is lower case.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change package keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                if not re.match('^\s*package', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'package')


class rule_005(package_rule):
    '''
    Package rule 005 checks if the "is" keyword is on the same line as the "package" keyword.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure "is" keyword is on the same line as the "package" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                lLine = oLine.lineLower.split()
                if len(lLine) < 3:
                    self.add_violation(iLineNumber)
                elif not lLine[2] == "is":
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*package\s+\w+)', r'\1 is', oLine.line, re.IGNORECASE))
            # Search for "is" on the next line
            iSearchIndex = iLineNumber
            while True:
                iSearchIndex += 1
                oLine = oFile.lines[iSearchIndex]
                if re.match('^\s*is', oLine.line, re.IGNORECASE):
                    oLine.update_line(re.sub(r'^(\s*)is', r'\1  ', oLine.line))
                    if re.match('^\s*$', oLine.line):
                        oLine.update_line('')
                        oLine.isBlank = True
                        break
                if not oLine.isBlank:
                    break


class rule_006(package_rule):
    '''
    Package rule 006 checks for the "end" and "package" keyword are lower case.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Ensure "end" and "package" keywords are lower case.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                if re.match('^\s*end\s+package', oLine.lineLower):
                    if not re.match('^\s*end\s+package', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'end')
            self._lower_case(oFile.lines[iLineNumber], 'package')


class rule_007(package_rule):
    '''
    Package rule 007 checks for the "package" keyword on the end package declaration.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'End of package follows this format: end package <package name>.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                if not re.match('^\s*end\s+package', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iIndex = oLine.lineLower.find('end') + len('end')
            oLine.update_line(oLine.line[:iIndex] + ' package' + oLine.line[iIndex:])


class rule_008(package_rule):
    '''
    Package rule 008 checks the package name is upper case on the closing "end package" line.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Uppercase package name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                if re.match('^\s*end\s+package\s+\w', oLine.lineLower):
                    lLine = oLine.line.split()
                    self._is_uppercase(lLine[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[2])


class rule_009(package_rule):
    '''
    Package rule 009 checks for a single space between the "end" and "package" keywords and component name.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Single space between "end" and "package" keywords and component name.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                if re.match('^\s*end\s+package\s+\w', oLine.lineLower):
                    if not re.match('^\s*end\spackage\s\w', oLine.lineLower):
                        self.add_violation(iLineNumber)
                elif re.match('^\s*end\s+package', oLine.lineLower):
                    if not re.match('^\s*end\spackage', oLine.lineLower):
                        self.add_violation(iLineNumber)
                elif re.match('^\s*end\s+\w', oLine.lineLower):
                    if not re.match('^\s*end\s\w', oLine.lineLower):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'end')
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'package')


class rule_010(package_rule):
    '''
    Package rule 010 checks the package name is upper case in the package declaration.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Upper case package name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                if re.match('^\s*package\s+\w+', oLine.lineLower):
                    lLine = oLine.line.split()
                    self._is_uppercase(lLine[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[1])


class rule_011(package_rule):
    '''
    Package rule 011 checks for a blank line below the package keyword.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Add blank line below package keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                self._is_blank_line_after(oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_below(oFile, iLineNumber)


class rule_012(package_rule):
    '''
    Package rule 012 checks for a blank line above the "end package" keywords.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Add blank line above the "end package" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                self._is_blank_line_before(oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)


class rule_013(package_rule):
    '''
    Package rule 013 checks the "is" keyword is lower case.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Change "is" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                if re.match('^\s*package\s+\w+\s+is', oLine.lineLower):
                    if not re.match('^\s*\w+\s+\w+\s+is', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'is')


class rule_014(package_rule):
    '''
    Package rule 014 checks for the package name exists on the same line as the "end" and "package" keywords.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'End of package follows this format: end package <package name>.'
        self.phase = 1
        self.fixable = False  # User must add package name

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                lLine = oLine.lineLower.replace(';', '').split()
                if len(lLine) < 3 and lLine[1] == 'package':
                    self.add_violation(iLineNumber)
