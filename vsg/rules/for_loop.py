
from vsg import rule
import re


class for_loop_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'for_loop'



class rule_001(for_loop_rule):
    '''For loop rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        for_loop_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isForLoopKeyword or oLine.isForLoopEnd:
                self._check_indent(oLine, iLineNumber)


#class rule_002(for_loop_rule):
#    '''For loop.g rule 002 checks the if boolean expression is enclosed in ()'s.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '002'
#        self.solution = 'Enclose boolean expression in ()\'s.'
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isFor loop.gKeyword:
#                if not re.match('^\s*if\s*\(', oLine.lineLower):
#                    self.add_violation(iLineNumber)
#            if oLine.isElseFor loop.gKeyword:
#                if re.match('^\s*elsif\s+\w', oLine.lineLower):
#                    self.add_violation(iLineNumber)
#
#
#class rule_003(for_loop_rule):
#    '''For loop.g rule 003 checks there is a single space between the if keyword and the (.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '003'
#        self.solution = 'Ensure only a single space exists between the "if" keyword and the (.' 
#        self.phase = 2
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isFor loop.gKeyword:
#                if re.match('^\s*if\s*\(', oLine.lineLower):
#                    if not re.match('^\s*if\s\(', oLine.lineLower):
#                        self.add_violation(iLineNumber)
#
#
#class rule_004(for_loop_rule):
#    '''For loop.g rule 004 checks there is a single space between the ) and "then" keyword.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '004'
#        self.solution = 'Ensure only a single space exists between the ) and "then" keyword.' 
#        self.phase = 2
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isThenKeyword:
#                if re.match('^\s*.*\)\s*then', oLine.lineLower):
#                    if not re.match('^\s*.*\)\sthen', oLine.lineLower):
#                        self.add_violation(iLineNumber)
#
#
#class rule_005(for_loop_rule):
#    '''For loop.g rule 005 checks there is a single space between the "elsif" keyword and the (.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '005'
#        self.solution = 'Ensure only a single space exists between the "elsif" keyword and the (.' 
#        self.phase = 2
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isElseFor loop.gKeyword:
#                if re.match('^\s*elsif\s*\(', oLine.lineLower):
#                    if not re.match('^\s*elsif\s\(', oLine.lineLower):
#                        self.add_violation(iLineNumber)
#
#
#class rule_006(for_loop_rule):
#    '''For loop.g rule 006 checks for an empty line after the then keyword.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '006'
#        self.solution = 'Remove blank line(s) after the "then" keyword.' 
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isThenKeyword and not oFile.lines[iLineNumber + 2].isCaseKeyword and not oLine.isEndFor loop.gKeyword:
#                self._is_no_blank_line_after(oFile, iLineNumber)
#
#
#class rule_007(for_loop_rule):
#    '''For loop.g rule 007 checks for an empty line before the "elsif" keyword.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '007'
#        self.solution = 'Remove blank line(s) before the "elsif" keyword.' 
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isElseFor loop.gKeyword:
#                self._is_no_blank_line_before(oFile, iLineNumber)
#
#
#class rule_008(for_loop_rule):
#    '''For loop.g rule 008 checks for an empty line before the "end if" keyword.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '008'
#        self.solution = 'Remove blank line(s) before the "end if" keyword.' 
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndFor loop.gKeyword and not oFile.lines[iLineNumber - 2].isEndCaseKeyword and not oLine.isIfKeyword:
#                self._is_no_blank_line_before(oFile, iLineNumber)
#
#
#class rule_009(for_loop_rule):
#    '''For loop.g rule 009 checks the alignment of multiline boolean expressions.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '009'
#        self.solution = 'Align with space after ( in first line of boolean expression.' 
#        self.phase = 5
#
#    def analyze(self, oFile):
#        fCheckAlignment = False
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isFor loop.gKeyword and oLine.isThenKeyword:
#                continue
#            if oLine.isElseFor loop.gKeyword and oLine.isThenKeyword:
#                continue
#            if oLine.isFor loop.gKeyword:
#                if re.match('^\s+if\s\(', oLine.lineLower):
#                    iAlignmentColumn = oLine.lineLower.find('(')
#                    fCheckAlignment = True
#                continue
#            if oLine.isElseFor loop.gKeyword:
#                if re.match('^\s+elsif\s\(', oLine.lineLower):
#                    iAlignmentColumn = oLine.lineLower.find('(')
#                    fCheckAlignment = True
#                continue
#            if oLine.insideFor loop.g and fCheckAlignment:
#                if not re.match('^\s{' + str(iAlignmentColumn + 1) + '}\S', oLine.line):
#                    self.add_violation(iLineNumber)
#            if oLine.isThenKeyword:
#                fCheckAlignment = False
#
#
#class rule_010(for_loop_rule):
#    '''For loop.g rule 010 checks for an empty line before the "else" keyword.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '010'
#        self.solution = 'Remove blank line(s) before the "else" keyword.' 
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isElseKeyword and not oFile.lines[iLineNumber - 2].isEndCaseKeyword and not oLine.isFor loop.gKeyword:
#                self._is_no_blank_line_before(oFile, iLineNumber)
#
#
#class rule_011(for_loop_rule):
#    '''For loop.g rule 011 checks for an empty line after the "else" keyword.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '011'
#        self.solution = 'Remove blank line(s) after the "else" keyword.' 
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isElseKeyword and not oFile.lines[iLineNumber + 2].isCaseKeyword and not oLine.isEndFor loop.gKeyword:
#                self._is_no_blank_line_after(oFile, iLineNumber)
#
#
#class rule_012(for_loop_rule):
#    '''For loop.g rule 012 checks for code after the "then" keyword.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '012'
#        self.solution = 'Move code after "then" or "else" keyword to the next line.' 
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isThenKeyword:
#                if re.match('^.*\sthen\s+\w', oLine.lineLower):
#                    self.add_violation(iLineNumber)
#            elif oLine.isElseKeyword:
#                if re.match('^.*\selse\s+\w', oLine.lineLower):
#                    self.add_violation(iLineNumber)
#               
#
#class rule_013(for_loop_rule):
#    '''For loop.g rule 013 checks the "else" keyword is on it's own line.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '013'
#        self.solution = 'Move "else" keyword to it\'s own line.' 
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isElseKeyword:
#                if not re.match('^\s*else', oLine.lineLower):
#                    self.add_violation(iLineNumber)
#
#
#class rule_014(for_loop_rule):
#    '''For loop.g rule 014 checks the "end if" keyword is on it's own line.'''
#
#    def __init__(self):
#        for_loop_rule.__init__(self)
#        self.identifier = '014'
#        self.solution = 'Move "end if" keyword to it\'s own line.' 
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndFor loop.gKeyword:
#                if not re.match('^\s*end\s+if', oLine.lineLower):
#                    self.add_violation(iLineNumber)

