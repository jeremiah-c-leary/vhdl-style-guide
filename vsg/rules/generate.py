
from vsg import rule
import re


class generate_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generate'


class rule_001(generate_rule):
    '''Generate rule 001 checks for spaces at the beginning of the line.'''

    def __init__(self):
        generate_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword or oLine.isGenerateBegin or oLine.isGenerateEnd:
                self._check_indent(oLine, iLineNumber)


class rule_002(generate_rule):
    '''Generate rule 002 checks for a single space between the label and :.'''

    def __init__(self):
        generate_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists before the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword:
                if not re.match('^\s*\w+\s:', oLine.line):
                    self.add_violation(iLineNumber)


class rule_003(generate_rule):
    '''Generate rule 003 checks for a blank line after the "end generate" keywords.'''

    def __init__(self):
        generate_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Add blank line below the "end generate" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateEnd:
                self._is_blank_line_after(oFile, iLineNumber)


class rule_004(generate_rule):
    '''Generate rule 004 checks for a blank line before the "generate" keyword.'''

    def __init__(self):
        generate_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Add blank line above the "generate" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword:
                self._is_blank_line_before(oFile, iLineNumber)


class rule_005(generate_rule):
    '''Generate rule 005 checks the generate label is uppercase.'''

    def __init__(self):
        generate_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Uppercase generate label.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword:
                lLine = oLine.line.split(':')
                if not lLine[0] == lLine[0].upper():
                    self.add_violation(iLineNumber)

#class rule_002(generate_rule):
#    '''Generate rule 002 checks for a single space between "generate", "of", and "is" keywords.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '002'
#        self.solution = 'Remove extra spaces after generate keyword.'
#        self.phase = 2
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateKeyword:
#                if len(oLine.line.split()) > 4:
#                    if not re.match('^\s*generate\s\S+\sof\s\S+\sis', oLine.lineLower):
#                        self.add_violation(iLineNumber)
#
#
#class rule_003(generate_rule):
#    '''Generate rule 003 checks for a blank line above the generate keyword.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '003'
#        self.solution = 'Add blank line above generate keyword.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateKeyword:
#                self._is_blank_line_before(oFile, iLineNumber)
#
#
#class rule_004(generate_rule):
#    '''Generate rule 004 checks the generate keyword is lower case.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '004'
#        self.solution = 'Change generate keyword to lowercase.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateKeyword:
#                if not re.match('^\s*generate', oLine.line):
#                    self.add_violation(iLineNumber)
#
#
#class rule_005(generate_rule):
#    '''Generate rule 005 checks if the "of" keyword is on the same line as the "generate" keyword.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '005'
#        self.solution = 'Ensure "of" keyword is on the same line as the "generate" keyword.'
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateKeyword:
#                lLine = oLine.lineLower.split()
#                if len(lLine) < 3:
#                    self.add_violation(iLineNumber)
#                elif not lLine[2] == "of":
#                    self.add_violation(iLineNumber)
#
#
#class rule_006(generate_rule):
#    '''Generate rule 006 checks if the "is" keyword is on the same line as the "generate" keyword.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '006'
#        self.solution = 'Ensure "is" keyword is on the same line as the "generate" keyword.'
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateKeyword:
#                lLine = oLine.lineLower.split()
#                if len(lLine) < 5:
#                    self.add_violation(iLineNumber)
#                elif not lLine[4] == "is":
#                    self.add_violation(iLineNumber)
#
#
#class rule_007(generate_rule):
#    '''Generate rule 007 checks for spaces at the beginning of the line for the "begin" keyword.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '007'
#        self.solution = 'Ensure proper indentation.'
#        self.phase = 4
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateBegin:
#                self._check_indent(oLine, iLineNumber)
#
#
#class rule_008(generate_rule):
#    '''Generate rule 008 checks for spaces at the beginning of the line for the "end generate" keywords.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '008'
#        self.solution = 'Ensure proper indentation.'
#        self.phase = 4
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndGenerate:
#                self._check_indent(oLine, iLineNumber)
#
#
#class rule_009(generate_rule):
#    '''Generate rule 009 checks for the "end" and "generate" keyword are lower case.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '009'
#        self.solution = 'Ensure "end" and "generate" keywords are lower case.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndGenerate:
#                if re.match('^\s*end\s\s*generate', oLine.lineLower):
#                    if not re.match('^\s*end\s\s*generate', oLine.line):
#                        self.add_violation(iLineNumber)
#
#
#class rule_010(generate_rule):
#    '''Generate rule 010 checks for the entity name exists on the same line as the "end" and "generate" keywords.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '010'
#        self.solution = 'End of generate follows this format: end generate <generate name>.'
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndGenerate:
#                lLine = oLine.line.split()
#                if len(lLine) > 2:
#                    if lLine[2].startswith('--'):
#                        self.add_violation(iLineNumber)
#                else:
#                    self.add_violation(iLineNumber)
#
#
#class rule_011(generate_rule):
#    '''Generate rule 011 checks the entity name is upper case on the closing "end generate" line.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '011'
#        self.solution = 'Uppercase generate name.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndGenerate:
#                lLine = oLine.line.split()
#                if len(lLine) > 2:
#                    if not lLine[2].startswith('--'):
#                        self._is_uppercase(lLine[2], iLineNumber)
#
#
#class rule_012(generate_rule):
#    '''Generate rule 012 checks for a single space between the "end" and "generate" keywords.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '012'
#        self.solution = 'Single space between "end" and "generate" keywords.'
#        self.phase = 2
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndGenerate:
#                if (len(oLine.line.split()) > 1):
#                    if re.match('^\s*end\s+generate', oLine.lineLower):
#                        if not re.match('^\s*end\sgenerate', oLine.lineLower):
#                            self.add_violation(iLineNumber)
#
#
#class rule_013(generate_rule):
#    '''Generate rule 013 checks the generate name is upper case in the generate declaration.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '013'
#        self.solution = 'Upper case generate name.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateKeyword:
#                if re.match('^\s*\S+\s\s*\S+\s\s*of\s\s*\S+\s\s*is', oLine.lineLower):
#                    lLine = oLine.line.split()
#                    self._is_uppercase(lLine[1], iLineNumber)
#
#
#class rule_014(generate_rule):
#    '''Generate rule 013 checks the entity name is upper case in the generate declaration.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '014'
#        self.solution = 'Upper case entity name.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateKeyword:
#                if re.match('^\s*\S+\s\s*\S+\s\s*of\s\s*\S+\s\s*is', oLine.lineLower):
#                    lLine = oLine.line.split()
#                    self._is_uppercase(lLine[3], iLineNumber)
#
#
#class rule_015(generate_rule):
#    '''Generate rule 015 checks for a blank line below the generate keyword.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '015'
#        self.solution = 'Add blank line below generate keyword.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateKeyword:
#                self._is_blank_line_after(oFile, iLineNumber)
#
#
#class rule_016(generate_rule):
#    '''Generate rule 016 checks for a blank line above the "begin" keyword.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '016'
#        self.solution = 'Add blank line above the "begin" keyword.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateBegin:
#                self._is_blank_line_before(oFile, iLineNumber)
#
#
#class rule_017(generate_rule):
#    '''Generate rule 017 checks for a blank line below the "begin" keyword.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '017'
#        self.solution = 'Add blank line below the "begin" keyword.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateBegin:
#                self._is_blank_line_after(oFile, iLineNumber)
#
#
#class rule_018(generate_rule):
#    '''Generate rule 018 checks for a blank line above the "end generate" keywords.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '018'
#        self.solution = 'Add blank line above the "end generate" keywords.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndGenerate:
#                self._is_blank_line_before(oFile, iLineNumber)
#
#
#class rule_019(generate_rule):
#    '''Generate rule 019 checks the "of" keyword is lower case.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '019'
#        self.solution = 'Change "of" keyword to lowercase.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateKeyword:
#                if re.match('^\s*\w+\s+\w+\s+of', oLine.lineLower):
#                    if not re.match('^\s*\w+\s+\w+\s+of', oLine.line):
#                        self.add_violation(iLineNumber)
#
#
#class rule_020(generate_rule):
#    '''Generate rule 020 checks the "is" keyword is lower case.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '020'
#        self.solution = 'Change "is" keyword to lowercase.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateKeyword:
#                if re.match('^\s*generate\s+\w+\s+of\s+\w+\s+is', oLine.lineLower):
#                    if not re.match('^\s*\w+\s+\w+\s+\w+\s+\w+\s+is', oLine.line):
#                        self.add_violation(iLineNumber)
#
#
#class rule_021(generate_rule):
#    '''Generate rule 021 checks the "begin" keyword is lower case.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '021'
#        self.solution = 'Change "begin" keyword to lowercase.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isGenerateBegin:
#                if not re.match('^\s*begin', oLine.line):
#                    self.add_violation(iLineNumber)
#
#
#class rule_022(generate_rule):
#    '''Generate rule 022 checks for a single space after the "end generate" keywords and the generate name.'''
#
#    def __init__(self):
#        generate_rule.__init__(self)
#        self.identifier = '022'
#        self.solution = 'Ensure a single space exists between "generate" and the generate name.'
#        self.phase = 2
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndGenerate:
#                if re.match('^\s*end\s+generate\s+\w', oLine.lineLower):
#                    if not re.match('^\s*end\s+generate\s\w', oLine.lineLower):
#                        self.add_violation(iLineNumber)

