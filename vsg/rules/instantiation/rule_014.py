
from vsg import rule
from vsg import line


class rule_014(rule.rule):
    '''
    Instantiation rule 014 checks the closing ) for the generic map is on it's own line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '014'
        self.solution = 'Place closing ) on it\'s own line.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isInstantiationGenericEnd and (oLine.isInstantiationGenericAssignment or oLine.isInstantiationGenericKeyword):
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            _remove_closing_parenthesis(oFile, iLineNumber)
            _add_closing_parenthesis_on_new_line(oFile, iLineNumber)


def _remove_closing_parenthesis(oFile, iLineNumber):
    oLine = oFile.lines[iLineNumber]
    sLine = oLine.lineNoComment
    iIndex = sLine.rfind(')')
    sLine = oLine.line
    sLine = sLine[:iIndex] + sLine[iIndex + 1:]
    oLine.update_line(sLine)
    oFile.lines[iLineNumber].isInstantiationGenericEnd = False


def _add_closing_parenthesis_on_new_line(oFile, iLineNumber):
    oFile.lines.insert(iLineNumber + 1, line.line('  )'))
    oFile.lines[iLineNumber + 1].isInstantiationGenericAssignement = False
    oFile.lines[iLineNumber + 1].isInstantiationGenericEnd = True
    oFile.lines[iLineNumber + 1].insideInstantiation = True
    oFile.lines[iLineNumber + 1].indentLevel = oFile.lines[iLineNumber].indentLevel - 1

