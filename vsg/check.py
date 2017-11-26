
import re

def indent(self, oLine, iLineNumber):
    '''Adds a violation if the indent of the line does not match the desired level.'''
    if not re.match('^\s{' + str(self.indentSize * oLine.indentLevel) + '}\S', oLine.line):
        self.add_violation(iLineNumber)

def is_no_blank_line_after(self, oFile, iLineNumber): 
    '''Adds a violation if the line after iLineNumber is blank.
       This is typically used to compress lines together.'''
    if oFile.lines[iLineNumber + 1].isBlank:
        self.add_violation(iLineNumber)

def is_no_blank_line_before(self, oFile, iLineNumber):
    '''Adds a violation if the line before iLineNumber is blank.
       This is typically used to compress lines together.'''
    if oFile.lines[iLineNumber - 1].isBlank:
        self.add_violation(iLineNumber)

def is_blank_line_after(self, oFile, iLineNumber): 
    '''Adds a violation if the line after iLineNumber is not blank.
       This is typically used to compress lines together.'''
    if not oFile.lines[iLineNumber + 1].isBlank:
        self.add_violation(iLineNumber)

def is_blank_line_before(self, oFile, iLineNumber):
    '''Adds a violation if the line before iLineNumber is not blank.
       This is typically used to compress lines together.'''
    if not oFile.lines[iLineNumber - 1].isBlank:
        self.add_violation(iLineNumber)

