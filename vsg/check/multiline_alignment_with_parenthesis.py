'''
This module contains functions for rules to perform their checks.
'''


def multiline_alignment_with_parenthesis(self, iColumn, oLine, iLineNumber, dParenthesis):
    '''
    Checks the alignment of multiline statements taking parenthesis into account.

    Parameters:

      self: (rule object)

      iColumn: (integer)

      oLine: (line object)

      iLineNumber: (integer)

      dParenthesis: (dictionary)
    '''
    for iIndex in range(dParenthesis[iLineNumber]['begin'], iLineNumber):
        iParenthesisColumn = _find_right_most_open_parenthesis(dParenthesis, iLineNumber)
        if iParenthesisColumn is None:
            if not dParenthesis[iLineNumber]['character'] == iColumn:
                self.add_violation(iLineNumber)
                self.dFix['violations'][iLineNumber] = {}
                self.dFix['violations'][iLineNumber]['column'] = iColumn
        else:
            if not dParenthesis[iLineNumber]['character'] == iParenthesisColumn + 1:
                self.add_violation(iLineNumber)
                self.dFix['violations'][iLineNumber] = {}
                self.dFix['violations'][iLineNumber]['column'] = iParenthesisColumn + 1
                offset = iParenthesisColumn + 1 - dParenthesis[iLineNumber]['character']
                for iIndex in range(len(dParenthesis[iLineNumber]['open'])):
                    dParenthesis[iLineNumber]['open'][iIndex] += offset


def _find_right_most_open_parenthesis(dParenthesis, iLineNumber):
    lOpenParenthesis = []
    for iIndex in range(dParenthesis[iLineNumber]['begin'], iLineNumber):
        for iOpenParenthesis in dParenthesis[iIndex]['open']:
            lOpenParenthesis.insert(0, iOpenParenthesis)
        for iCloseParenthesis in dParenthesis[iIndex]['closed']:
            lOpenParenthesis.pop(0)

    if not len(lOpenParenthesis) == 0:
        return lOpenParenthesis[0]
    return None
