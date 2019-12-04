'''
This module contains functions for rules to perform their checks.
'''

import re


def multiline_alignment(self, iColumn, oLine, iLineNumber, dParenthesis=None):
    '''
    Checks the alignment of multiline statements.

    Parameters:

      self: (rule object)

      iColumn: (integer)

      oLine: (line object)

      iLineNumber: (integer)

      dParenthesis: (dictionary)
    '''
    if dParenthesis is None:
        if not re.match('\s{' + str(iColumn) + '}\S', oLine.line):
            self.add_violation(iLineNumber)
            self.dFix['violations'][iLineNumber] = {}
            self.dFix['violations'][iLineNumber]['column'] = iColumn
    else:
#        print(dParenthesis)
        iTotalOpenParenthesis = 0
        iTotalCloseParenthesis = 0
        for iIndex in range(dParenthesis[iLineNumber]['begin'], iLineNumber):
            iTotalOpenParenthesis = iTotalOpenParenthesis + len(dParenthesis[iIndex]['open'])
            iTotalCloseParenthesis = iTotalCloseParenthesis + len(dParenthesis[iIndex]['closed'])
            sDebug = '[LineNumber]' + str(iIndex)
            sDebug += '[TotalOpenParenthesis]' + str(iTotalOpenParenthesis)
            sDebug += '[TotalCloseParenthesis]' + str(iTotalCloseParenthesis)
#            print(sDebug)
            if iTotalOpenParenthesis == iTotalCloseParenthesis:
                if not dParenthesis[iLineNumber]['character'] == iColumn:
                    self.add_violation(iLineNumber)
                    self.dFix['violations'][iLineNumber] = {}
                    self.dFix['violations'][iLineNumber]['column'] = iColumn
            else:
                iParenthesisColumn = find_right_most_open_parenthesis(dParenthesis, iLineNumber)
#                print('[iPrenthesisColumn]' + str(iParenthesisColumn))
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
            

def find_right_most_open_parenthesis(dParenthesis, iLineNumber):
#    print('[Entering find_right_most_open_parenthesis]')
    lOpenParenthesis = []
#    print('[iLineNumber]' + str(iLineNumber))
#    print(dParenthesis[iLineNumber]['begin'])
    for iIndex in range(dParenthesis[iLineNumber]['begin'], iLineNumber):
#        print('[iIndex]' + str(iIndex))
        for iOpenParenthesis in dParenthesis[iIndex]['open']:
            lOpenParenthesis.insert(0, iOpenParenthesis)
#        print('lOpenParenthesis before pop')
#        print(lOpenParenthesis)
        for iCloseParenthesis in dParenthesis[iIndex]['closed']:
            lOpenParenthesis.pop(0)
#        print('lOpenParenthesis after pop')
#        print(lOpenParenthesis)

#    print('[Exiting find_right_most_open_parenthesis]')
    if not len(lOpenParenthesis) == 0:
        return lOpenParenthesis[0]
    return None 
    
