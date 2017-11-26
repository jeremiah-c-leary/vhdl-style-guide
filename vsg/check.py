
import re

def indent(self, oLine, iLineNumber):
    '''Adds a violation if the indent of the line does not match the desired level.'''
    if not re.match('^\s{' + str(self.indentSize * oLine.indentLevel) + '}\S', oLine.line):
        self.add_violation(iLineNumber)
