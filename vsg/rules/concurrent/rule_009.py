
import copy

from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils

lTokenPairs = []
lTokenPairs.append([token.concurrent_conditional_signal_assignment.assignment, token.concurrent_conditional_signal_assignment.semicolon])


class rule_009(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'concurrent', '009')
        self.solution = 'Align with open parenthesis on previous line.'
        self.phase = 4
        self.lTokenPairs = lTokenPairs
        self.align_left = 'no'
        self.configuration.append('align_left')
        self.align_paren = 'yes'
        self.configuration.append('align_paren')
        self.wrap_at_when = 'yes'
        self.configuration.append('wrap_at_when')
        self.align_when_keywords = 'no'
        self.configuration.append('align_when_keywords')

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def analyze(self, oFile):
        lToi = self._get_tokens_of_interest(oFile)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
#            print('='*5 + str(iLine) + '='*70)

            iFirstLine, iFirstLineIndent = _get_first_line_info(iLine, oFile)

            iFirstColumn, iNextColumn, iLastColumn = _find_first_column(oFile, oToi, self.align_left, iFirstLineIndent, self.indentSize)
            iAssignColumn = oFile.get_column_of_token_index(oToi.get_start_index())
            iColumn = iAssignColumn

#            dActualIndent = {}

#            dActualIndent[iLine] = iFirstLineIndent
            lParens = []
            lWhens = []
            lElses = []
            dIndex = {}
            lStructure = []

            bStartsWithParen = _starts_with_paren(lTokens) 

            dActualIndent = _build_actual_indent_dict(iLine, lTokens, iFirstLineIndent)

            dIndex = _build_index_dict(iLine, lTokens)

            lActualStructure, iLastLine  = _build_structure_list(iLine, iColumn, lTokens)
            lStructure = copy.deepcopy(lActualStructure)
            if iFirstLine == iLastLine:
                continue

            iFirstIndent = _find_first_indent(self.align_left, bStartsWithParen, dActualIndent, self.indentSize, iAssignColumn)

#            print(lStructure)
            dExpectedIndent, lStructure = _apply_align_left_option(self.align_left, lStructure, dActualIndent, bStartsWithParen, self.indentSize, iAssignColumn, iFirstIndent)
#            print(lStructure)
            dExpectedIndent, lStructure = _apply_align_paren_option(self.align_paren, lStructure, dExpectedIndent, bStartsWithParen, self.indentSize, iAssignColumn, iFirstIndent)
#            print('#'*80)
#            print(lStructure)
            dExpectedIndent, lStructure = _apply_align_when_keywords_option(self.align_when_keywords, lStructure, dExpectedIndent, bStartsWithParen, self.indentSize, iAssignColumn, iFirstIndent)
            dExpectedIndent, lStructure = _apply_align_paren_option(self.align_paren, lStructure, dExpectedIndent, bStartsWithParen, self.indentSize, iAssignColumn, iFirstIndent)
            dExpectedIndent, lStructure = _apply_wrap_at_when_option(self.wrap_at_when, lStructure, dExpectedIndent, bStartsWithParen, self.indentSize, iAssignColumn, iFirstIndent)
            if self.wrap_at_when == 'yes' and self.align_paren == 'yes':
                dExpectedIndent, lStructure = _apply_align_paren_after_when(lStructure, dExpectedIndent, bStartsWithParen, self.indentSize, iAssignColumn, iFirstIndent)
#            print(lStructure)
#            print(lActualStructure)

#            print(f'Actual = {dActualIndent}')
#            print(f'Expect = {dExpectedIndent}')
#            print(f'Index  = {dIndex}')
#            print(f'dIndex = {dIndex}')
            for iLine in range(iFirstLine + 1, iLastLine + 1):
                if dActualIndent[iLine] == dExpectedIndent[iLine]:
                    continue

                dAction = {}
                dAction['type'] = 'indent'
                dAction['line'] = iLine
                dAction['column'] = dExpectedIndent[iLine]

                if dActualIndent[iLine] > 0:
                    dAction['action'] = 'adjust'
                else:
                    dAction['action'] = 'insert'

                sSolution = 'Adjust indent to column ' + str(dExpectedIndent[iLine])
                iToken = dIndex[iLine]
                oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution)
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

            if self.align_when_keywords == 'yes':
                for dActual, dExpect in zip(lActualStructure, lStructure):
                    if dActual['type'] == 'when':
                        if dExpect['adjust'] != 0:
                            dAction = {}
                            dAction['type'] = 'when'
                            dAction['line'] = dExpect['line']
                            dAction['column'] = dExpect['column']
                            dAction['adjust'] = dExpect['adjust']
                            sSolution = 'Align when with other whens at column ' + str(dExpect['column'])
                            oViolation = violation.New(dAction['line'], oToi.extract_tokens(dActual['iToken'] - 1, dActual['iToken'] - 1), sSolution)
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)


        self._sort_violations()

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
#        print(dAction)
        if dAction['type'] == 'when':
            iSpace = len(lTokens[0].get_value())
            iNewSpace = iSpace + dAction['adjust']
            lTokens[0].set_value(' '*iNewSpace)
        if dAction['type'] == 'indent':
            if dAction['action'] == 'adjust':
                lTokens[0].set_value(' '*dAction['column'])
            else:
                lTokens.insert(0, parser.whitespace(' '*dAction['column']))

        oViolation.set_tokens(lTokens)


def calculate_start_column(oFile, oToi):
    iReturn = oFile.get_column_of_token_index(oToi.get_start_index())
    iReturn += len(oToi.get_tokens()[0].get_value())
    iReturn += 1
#    print(f'Start Column = {iReturn}')
    return iReturn


def _find_first_column(oFile, oToi, sAlignLeft, iIndentSize, iIndentStep):
    iStartIndex = oToi.get_start_index()
    if sAlignLeft == 'yes':
        iIndentLevel = oFile.get_indent_of_line_at_index(iStartIndex)
        iFirstColumn = iIndentLevel * iIndentSize + iIndentStep
        if is_token_before_carriage_return(parser.open_parenthesis, oToi.get_tokens()):
            iNextColumn = iFirstColumn + iIndentStep
            iLastColumn = iIndentSize * iIndentLevel
        else:
            iNextColumn = iIndentSize * iIndentLevel
            iLastColumn = iIndentSize * iIndentLevel
    else:
        iFirstColumn = oFile.get_column_of_token_index(iStartIndex)
        iNextColumn = iFirstColumn
        iLastColumn = iFirstColumn
#    print(f'({iFirstColumn, iNextColumn, iLastColumn}')
    return iFirstColumn, iNextColumn, iLastColumn


def is_token_before_carriage_return(tToken, lTokens):
    for oToken in lTokens:
        if isinstance(oToken, tToken):
            return True
        if isinstance(oToken, parser.carriage_return):
            return False
    return False


def _set_column_adjustment(iToken, lTokens):
    iReturn = 0
    if isinstance(lTokens[iToken + 1], parser.whitespace):
        if isinstance(lTokens[iToken + 2], parser.close_parenthesis):
            iReturn = -1
    else:
        if isinstance(lTokens[iToken + 1], parser.close_parenthesis):
            iReturn = -1
    return iReturn


def _set_indent(iToken, lTokens):
    iReturn = 0
    if isinstance(lTokens[iToken + 1], parser.whitespace):
        iReturn = len(lTokens[iToken + 1].get_value())
    else:
        iReturn = 0
    return iReturn


def _apply_align_left_option(sConfig, lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
#    print('--> _apply_align_left_option  <-' + '-'*70)
    iFirstLine = _get_first_line(dActualIndent)
    iLastLine = _get_last_line(dActualIndent)
#    print(f'iFirstLine = {iFirstLine} | iLastLine = {iLastLine}')
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]
#    print(iIndent) 


#    print(iFirstIndent)

    iIndent = iFirstIndent

    bWhenFound = False
    iParens = 0
    lWhenIndent = []
    lParens = []
    for dStruct in lStructure:
        if dStruct['type'] == 'when':
            bWhenFound = True
        elif dStruct['type'] == 'else':
            bWhenFound = False
        elif dStruct['type'] == 'return' and bWhenFound:
            if iParens == 0:
                lWhenIndent.append(dStruct['line'])
        elif dStruct['type'] == 'open':
            iParens +=1
            lParens.append(dStruct)
        elif dStruct['type'] == 'close':
            iParens -= 1
            lParens.append(dStruct)

#    print(f'lWhenIndent = {lWhenIndent}')
            
    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')

        lTemp = []
        for dParen in lParens:
            if dParen['line'] == iLine:
                lTemp.append(dParen)

        if len(lTemp) == 0:
            dExpectedIndent[iLine + 1] = iIndent

        else:

            for dTemp in lTemp:
                if dTemp['type'] == 'open':
                    iParens += 1
                else:
                    iParens -= 1
                    if dTemp['begin_line']:
                        dExpectedIndent[iLine] -= iIndentStep 

        if iLine == iFirstLine:
            if bStartsWithParen:
                iIndent = iFirstIndent + iParens * iIndentStep
            else: 
                if iParens == 0:
                    iIndent = iFirstIndent
                else:
                    iIndent = iFirstIndent + iParens * iIndentStep
        else:
            if iParens == 0:
                iIndent = iFirstIndent
            else:
                iIndent = iFirstIndent + iParens * iIndentStep + iIndentStep

#        print(f'Prev = {iIndent}')
#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')
#        print(f'iLine + 1 = {iLine + 1}')
        if (iLine + 1) in lWhenIndent:
            iIndent = iFirstIndent + iIndentStep
#        print(f'indent = {iIndent} | iPerens = {iParens}')
#        print(f'Next = {iIndent}')
        dExpectedIndent[iLine + 1] = iIndent

    lReturnStructure = _update_structure(dExpectedIndent, dActualIndent, lStructure)
    return dExpectedIndent, lReturnStructure


def _apply_align_paren_option(sConfig, lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
#    print('--> _apply_align_paren_option <-' + '-'*70)
    if sConfig == 'no':
        return dActualIndent, lStructure 
    iFirstLine = _get_first_line(dActualIndent)
    iLastLine = _get_last_line(dActualIndent)

    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    if bStartsWithParen:
       iIndent = dActualIndent[iFirstLine]
       iColumn = iIndent
       lColumn = [dActualIndent[iFirstLine]]
    else:
       iIndent = iFirstIndent
       iColumn = iIndent
       lColumn = [iIndent]

#    print('*'*80)
#    print(lParens)

    bWhenFound = False
    iParens = 0
    lWhenIndent = []
    lParens = []
    for dStruct in lStructure:
        if dStruct['type'] == 'when':
            bWhenFound = True
        elif dStruct['type'] == 'else':
            bWhenFound = False
        elif dStruct['type'] == 'return' and bWhenFound:
            if iParens == 0:
                lWhenIndent.append(dStruct['line'])
        elif dStruct['type'] == 'open':
            iParens +=1
            lParens.append(dStruct)
        elif dStruct['type'] == 'close':
            iParens -= 1
            lParens.append(dStruct)

    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')
        lTemp = []
        for dParen in lParens:
            if dParen['line'] == iLine:
                lTemp.append(dParen)

#        print(f'lTemp = {lTemp}')
        iTemp = lColumn[-1]
        for dTemp in lTemp:
            if dTemp['type'] == 'open':
                iParens += 1
                if iLine == iFirstLine:
                    iColumn = dTemp['column'] + iIndentStep - 1
                else:
                    iColumn = dTemp['column'] + (iTemp - dActualIndent[iLine]) + iIndentStep - 1
#                print(f"iColumn = {dTemp['column']} + ({iTemp} - {dActualIndent[iLine]}) + {iIndentStep} - 1 = {iColumn}")
                lColumn.append(iColumn)
                dExpectedIndent[iLine + 1] = iColumn
            else:
                iParens -= 1
                lColumn.pop()
                dExpectedIndent[iLine + 1] = lColumn[-1]
                if dTemp['begin_line']:
                    dExpectedIndent[iLine] = dExpectedIndent[iLine] - iIndentStep

#        print(f'iParens = {iParens}')


        if len(lTemp) == 0:
            if bStartsWithParen:
                dExpectedIndent[iLine + 1] = lColumn[-1]
            else:
                if iParens == 0:
                    dExpectedIndent[iLine + 1] = lColumn[-1]
                else:
                    dExpectedIndent[iLine + 1] = lColumn[-1]

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')

        if (iLine + 1) in lWhenIndent:
            dExpectedIndent[iLine + 1] = iFirstIndent + iIndentStep

    lReturnStructure = _update_structure(dExpectedIndent, dActualIndent, lStructure)
    return dExpectedIndent, lReturnStructure


def _apply_align_when_keywords_option(sConfig, lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
#    print('--> _apply_align_when_keywords_option <-' + '-'*70)
    if sConfig == 'no':
        return dActualIndent, lStructure 
    iFirstLine = _get_first_line(dActualIndent)
    iLastLine = _get_last_line(dActualIndent)

    iWhenMax = -1
    for dStruct in lStructure:
        if dStruct['type'] == 'when':
            iWhenMax = max(iWhenMax, dStruct['column'])

#    print(f'iWhenMax = {iWhenMax}')

    lNewStruct = []
    bAdjust = False
    for dStruct in lStructure:
        if dStruct['type'] == 'when':
            iAdjust = iWhenMax - dStruct['column']
            if iAdjust != 0:
                bAdjust = True
            dStruct['adjust'] = iAdjust
        if dStruct['type'] == 'return':
            bAdjust = False
        if bAdjust:
            dStruct['column'] += iAdjust 
        lNewStruct.append(dStruct)

    return dActualIndent, lNewStruct


def _apply_wrap_at_when_option(sConfig, lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
#    print('--> _apply_wrap_at_when_option <-' + '-'*70)
    if sConfig == 'no':
        return dActualIndent, lStructure 
    iFirstLine = _get_first_line(dActualIndent)
    iLastLine = _get_last_line(dActualIndent)

    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    bWhenFound = False
    dWhenIndent = {}
    lParens = []
    for dStruct in lStructure:
        if dStruct['type'] == 'when':
            bWhenFound = True
            iColumn = dStruct['column']
        elif dStruct['type'] == 'else':
            bWhenFound = False
        elif dStruct['type'] == 'return' and bWhenFound:
            dTemp = {}
            dTemp['column'] = iColumn
            dWhenIndent[dStruct['line']] = dTemp
        elif dStruct['type'] == 'open':
            lParens.append(dStruct)
        elif dStruct['type'] == 'close':
            lParens.append(dStruct)

    iWhenIndent = -1
    iParensLast = 0
    iParens = 0
    
    for iLine in range(iFirstLine, iLastLine):

        lTemp = []
        for dParen in lParens:
            if dParen['line'] == iLine:
                lTemp.append(dParen)

        for dTemp in lTemp:
            if dTemp['type'] == 'open':
                iParens += 1
            else:
                iParens -= 1

        if iLine + 1 in dWhenIndent:
            if iLine in dWhenIndent:
                iWhenIndent = dExpectedIndent[iLine] + (iParens * iIndentStep)
            else:
                iWhenIndent = dWhenIndent[iLine + 1]['column'] + 4 + 1 + (iParens * iIndentStep)
            dExpectedIndent[iLine + 1] = iWhenIndent
        else:
            dExpectedIndent[iLine + 1] = dActualIndent[iLine + 1]
 
    lReturnStructure = _update_structure(dExpectedIndent, dActualIndent, lStructure)
    return dExpectedIndent, lReturnStructure


def _apply_align_paren_after_when(lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
#    print('--> _apply_align_paren_option <-' + '-'*70)
    iFirstLine = _get_first_line(dActualIndent)
    iLastLine = _get_last_line(dActualIndent)

    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    if bStartsWithParen:
       iIndent = dActualIndent[iFirstLine]
       iColumn = iIndent
       lColumn = [dActualIndent[iFirstLine]]
    else:
       iIndent = iFirstIndent
       iColumn = iIndent
       lColumn = [iIndent]

#    print('*'*80)
#    print(lParens)

    bWhenFound = False
    iParens = 0
    lWhenIndent = []
    lParens = []
    for dStruct in lStructure:
        if dStruct['type'] == 'when':
            bWhenFound = True
        elif dStruct['type'] == 'else':
            bWhenFound = False
        elif dStruct['type'] == 'return' and bWhenFound:
            if iParens == 0:
                lWhenIndent.append(dStruct['line'])
        elif dStruct['type'] == 'open':
            iParens +=1
            lParens.append(dStruct)
        elif dStruct['type'] == 'close':
            iParens -= 1
            lParens.append(dStruct)

    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')
        lTemp = []
        for dParen in lParens:
            if dParen['line'] == iLine:
                lTemp.append(dParen)

#        print(f'lTemp = {lTemp}')
        iTemp = lColumn[-1]
        for dTemp in lTemp:
            if dTemp['type'] == 'open':
                iParens += 1
                if iLine == iFirstLine:
                    iColumn = dTemp['column'] + iIndentStep - 1
                else:
                    iColumn = dTemp['column'] + (iTemp - dActualIndent[iLine]) + iIndentStep - 1
#                print(f"iColumn = {dTemp['column']} + ({iTemp} - {dActualIndent[iLine]}) + {iIndentStep} - 1 = {iColumn}")
                lColumn.append(iColumn)
                dExpectedIndent[iLine + 1] = iColumn
            else:
                iParens -= 1
                lColumn.pop()
                dExpectedIndent[iLine + 1] = lColumn[-1]
                if dTemp['begin_line']:
                    dExpectedIndent[iLine] = dExpectedIndent[iLine] - iIndentStep

#        print(f'iParens = {iParens}')


        if len(lTemp) == 0:
            if bStartsWithParen:
                dExpectedIndent[iLine + 1] = lColumn[-1]
            else:
                if iParens == 0:
                    dExpectedIndent[iLine + 1] = lColumn[-1]
                else:
                    dExpectedIndent[iLine + 1] = lColumn[-1]

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')

        if (iLine + 1) in lWhenIndent and iParens == 0:
            dExpectedIndent[iLine + 1] = dActualIndent[iLine + 1]

    lReturnStructure = _update_structure(dExpectedIndent, dActualIndent, lStructure)
    return dExpectedIndent, lReturnStructure


def _analyze_align_paren_no_align_left_yes_wrap_at_when_no(iFirstLine, iLastLine, lParens, iIndentStep, dActualIndent, bStartsWithParen, lStructure):
    print('--> _analyze_align_paren_no_align_left_yes_wrap_at_when_no <-' + '-'*70)
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]
#    print(iIndent) 
    if bStartsWithParen: 
        iFirstIndent = dActualIndent[iFirstLine]
    else:
        iFirstIndent = dActualIndent[iFirstLine] + iIndentStep

    iIndent = iFirstIndent

    bWhenFound = False
    iParens = 0
    lWhenIndent = []
    for dStruct in lStructure:
        if dStruct['type'] == 'when':
            bWhenFound = True
        elif dStruct['type'] == 'else':
            bWhenFound = False
        elif dStruct['type'] == 'return' and bWhenFound:
            if iParens == 0:
                lWhenIndent.append(dStruct['line'])
        elif dStruct['type'] == 'open':
            iParens +=1
        elif dStruct['type'] == 'close':
            iParens -= 1

    print(lWhenIndent)
            
    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')

        lTemp = []
        for dParen in lParens:
            if dParen['line'] == iLine:
                lTemp.append(dParen)

        if len(lTemp) == 0:
            dExpectedIndent[iLine + 1] = iIndent
            continue

        for dTemp in lTemp:
            if dTemp['type'] == 'open':
                iParens += 1
            else:
                iParens -= 1
                if dTemp['begin_line']:
                    dExpectedIndent[iLine] -= iIndentStep 

        if iLine == iFirstLine:
            if bStartsWithParen:
                iIndent = iFirstIndent + iParens * iIndentStep
            else: 
                if iParens == 0:
                    iIndent = iFirstIndent + iParens * iIndentStep
                else:
                    iIndent = iFirstIndent + iParens * iIndentStep - iIndentStep + iIndentStep
        else:
            if iParens == 0:
                iIndent = iFirstIndent + iParens * iIndentStep
            else:
                iIndent = iFirstIndent + iParens * iIndentStep + iIndentStep

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')
        if iLine + 1 in lWhenIndent:
            iIndent = iFirstIndent + iIndentStep

#        print(f'indent = {iIndent} | iPerens = {iParens}')
        dExpectedIndent[iLine + 1] = iIndent

    return dExpectedIndent


def _analyze_align_paren_true(iFirstLine, iLastLine, lParens, dActualIndent, iIndentStep, bStartsWithParen, iAssignColumn):
    print('--> _analyze_align_paren_true <-' + '-'*70)
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    if bStartsWithParen:
       iAdjust = 0
       iIndent = dActualIndent[iFirstLine]
       iColumn = iIndent
       lColumn = [dActualIndent[iFirstLine]]
    else:
       iAdjust = iAssignColumn
       iIndent = iAssignColumn + 2 + 1
       iColumn = iIndent
       lColumn = [iIndent]

#    print('*'*80)
#    print(lParens)

    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')
        lTemp = []
        for dParen in lParens:
            if dParen['line'] == iLine:
                lTemp.append(dParen)

#        print(f'lTemp = {lTemp}')
        iTemp = lColumn[-1]
        for dTemp in lTemp:
            if dTemp['type'] == 'open':
                iParens += 1
                if iLine == iFirstLine:
                    iColumn = dTemp['column'] + iIndentStep - 1
                else:
                    iColumn = dTemp['column'] + (iTemp - dActualIndent[iLine]) + iIndentStep - 1
#                print(f"iColumn = {dTemp['column']} + ({iTemp} - {dActualIndent[iLine]}) + {iIndentStep} - 1 = {iColumn}")
                lColumn.append(iColumn)
                dExpectedIndent[iLine + 1] = iColumn
            else:
                iParens -= 1
                lColumn.pop()
                dExpectedIndent[iLine + 1] = lColumn[-1]
                if dTemp['begin_line']:
                    dExpectedIndent[iLine] = dExpectedIndent[iLine] - iIndentStep

#        print(f'iParens = {iParens}')


        if len(lTemp) == 0:
            if bStartsWithParen:
                dExpectedIndent[iLine + 1] = lColumn[-1]
            else:
                if iParens == 0:
                    dExpectedIndent[iLine + 1] = lColumn[-1]
                else:
                    dExpectedIndent[iLine + 1] = lColumn[-1]

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')

    return dExpectedIndent


def _analyze_align_paren_true_align_left_true(iFirstLine, iLastLine, lParens, dActualIndent, iIndentStep, bStartsWithParen, iAssignColumn):
    print('--> _analyze_align_paren_true_align_left_true <-' + '-'*70)
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    if bStartsWithParen:
       iAdjust = 0
       iIndent = dActualIndent[iFirstLine]
       iColumn = iIndent
       lColumn = [dActualIndent[iFirstLine]]
    else:
       iAdjust = iAssignColumn
       iIndent = iAssignColumn + 2 + 1
       iColumn = iIndent
       lColumn = [iIndent]

#    print('*'*80)
#    print(lParens)

    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')
        lTemp = []
        for dParen in lParens:
            if dParen['line'] == iLine:
                lTemp.append(dParen)

#        print(f'lTemp = {lTemp}')
        iTemp = lColumn[-1]
        for dTemp in lTemp:
            if dTemp['type'] == 'open':
                iParens += 1
                if iLine == iFirstLine:
                    iColumn = dTemp['column'] + iIndentStep - 1
                else:
                    iColumn = dTemp['column'] + (iTemp - dActualIndent[iLine]) + iIndentStep - 1
#                print(f"iColumn = {dTemp['column']} + ({iTemp} - {dActualIndent[iLine]}) + {iIndentStep} - 1 = {iColumn}")
                lColumn.append(iColumn)
                dExpectedIndent[iLine + 1] = iColumn
            else:
                iParens -= 1
                lColumn.pop()
                dExpectedIndent[iLine + 1] = lColumn[-1]
                if dTemp['begin_line']:
                    dExpectedIndent[iLine] = dExpectedIndent[iLine] - iIndentStep

#        print(f'iParens = {iParens}')

        if len(lTemp) == 0:
            if bStartsWithParen:
                dExpectedIndent[iLine + 1] = lColumn[-1]
            else:
                if iParens == 0:
                    dExpectedIndent[iLine + 1] = lColumn[-1]
                else:
                    dExpectedIndent[iLine + 1] = lColumn[-1]

        if iLine == iFirstLine:
            dExpectedIndent[iLine + 1] = iParens * iIndentStep + dActualIndent[iFirstLine]
            lColumn[-1] = iParens * iIndentStep + dActualIndent[iFirstLine] 
            if iParens == 0 and not bStartsWithParen:
                dExpectedIndent[iLine + 1] = iIndentStep + dActualIndent[iFirstLine]
                lColumn[-1] = iIndentStep + dActualIndent[iFirstLine] 
        else:
            if iParens == 1:
                dExpectedIndent[iLine + 1] = iParens * iIndentStep + dActualIndent[iFirstLine]
                lColumn[-1] = iParens * iIndentStep + dActualIndent[iFirstLine] 

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')

    return dExpectedIndent


def _analyze_align_paren_no_align_left_no(iFirstLine, iLastLine, lParens, dActualIndent, iIndentStep, bStartsWithParen, iAssignColumn):
    print('--> _analyze_align_paren_no <-' + '-'*70)
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]
#    print(iIndent) 
    if bStartsWithParen: 
        iFirstIndent = dActualIndent[iFirstLine]
    else:
        iFirstIndent = iAssignColumn + 2 + 1

    iIndent = iFirstIndent

    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')

        lTemp = []
        for dParen in lParens:
            if dParen['line'] == iLine:
                lTemp.append(dParen)

        if len(lTemp) == 0:
            dExpectedIndent[iLine + 1] = iIndent
            continue

        for dTemp in lTemp:
            if dTemp['type'] == 'open':
                iParens += 1
            else:
                iParens -= 1
                if dTemp['begin_line']:
                    dExpectedIndent[iLine] -= iIndentStep 

        if iLine == iFirstLine:
            if bStartsWithParen:
                iIndent = iFirstIndent + iParens * iIndentStep
            else: 
                if iParens == 0:
                    iIndent = iFirstIndent + iParens * iIndentStep
                else:
                    iIndent = iFirstIndent + iParens * iIndentStep - iIndentStep + iIndentStep
        else:
            if iParens == 0:
                iIndent = iFirstIndent + iParens * iIndentStep
            else:
                iIndent = iFirstIndent + iParens * iIndentStep + iIndentStep

#        print(f'indent = {iIndent} | iPerens = {iParens}')
        dExpectedIndent[iLine + 1] = iIndent

    return dExpectedIndent


def _analyze_align_paren_yes_align_left_no_wrap_at_when_yes(iFirstLine, iLastLine, lParens, dActualIndent, iIndentStep, bStartsWithParen, iAssignColumn, lStructure):
    print('--> _analyze_align_paren_yes_align_left_no_wrap_at_when_yes <-' + '-'*70)
#    print(f'lStructure = {lStructure}')
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    if bStartsWithParen:
       iAdjust = 0
       iIndent = dActualIndent[iFirstLine]
       iColumn = iIndent
       lColumn = [dActualIndent[iFirstLine]]
    else:
       iAdjust = iAssignColumn
       iIndent = iAssignColumn + 2 + 1
       iColumn = iIndent
       lColumn = [iIndent]

#    print('*'*80)
#    print(lParens)

    bWhenFound = False
    iParens = 0
    lWhenIndent = []
    for dStruct in lStructure:
        if dStruct['type'] == 'when':
            bWhenFound = True
        elif dStruct['type'] == 'else':
            bWhenFound = False
        elif dStruct['type'] == 'return' and bWhenFound:
            if iParens == 0:
                lWhenIndent.append(dStruct['line'])
        elif dStruct['type'] == 'open':
            iParens +=1
        elif dStruct['type'] == 'close':
            iParens -= 1
            
#    print(f'lWhenIndent = {lWhenIndent}')

    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')
        lTemp = []
        for dParen in lParens:
            if dParen['line'] == iLine:
                lTemp.append(dParen)

        for dStruct in lStructure:
            if dStruct['line'] == iLine:
                if dStruct['type'] == 'when':
                    iWhenColumn = dStruct['column']

#        print(f'lTemp = {lTemp}')
        iTemp = lColumn[-1]
        for dTemp in lTemp:
            if dTemp['type'] == 'open':
                iParens += 1
                if iLine == iFirstLine:
                    iColumn = dTemp['column'] + iIndentStep - 1
                else:
                    iColumn = dTemp['column'] + (iTemp - dActualIndent[iLine]) + iIndentStep - 1
#                print(f"iColumn = {dTemp['column']} + ({iTemp} - {dActualIndent[iLine]}) + {iIndentStep} - 1 = {iColumn}")
                lColumn.append(iColumn)
                dExpectedIndent[iLine + 1] = iColumn
            else:
                iParens -= 1
                lColumn.pop()
                dExpectedIndent[iLine + 1] = lColumn[-1]
                if dTemp['begin_line']:
                    dExpectedIndent[iLine] = dExpectedIndent[iLine] - iIndentStep

#        print(f'iParens = {iParens}')


        if len(lTemp) == 0:
            if bStartsWithParen:
                dExpectedIndent[iLine + 1] = lColumn[-1]
            else:
                if iParens == 0:
                    dExpectedIndent[iLine + 1] = lColumn[-1]
                else:
                    dExpectedIndent[iLine + 1] = lColumn[-1]

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')
        if iLine + 1 in lWhenIndent:
            if not bWhenFound:
#                print(f'dExpectedIndent[iLine] = {dExpectedIndent[iLine]} | dActualIndent[iLine] = {dActualIndent[iLine]} | iWhenColumn = {iWhenColumn}')
                dExpectedIndent[iLine + 1] = dExpectedIndent[iLine] + iWhenColumn - dActualIndent[iLine] + 5
                bWhenFound = True
            else:
                dExpectedIndent[iLine + 1] = dExpectedIndent[iLine]
        else:
            bWhenFound = False

    return dExpectedIndent


def _starts_with_paren(lTokens):
 
    iToken = utils.find_next_non_whitespace_token(1, lTokens)
    if isinstance(lTokens[iToken], parser.open_parenthesis):
        return True
    return False


def _get_first_line_info(iLine, oFile):
    lTemp = oFile.get_tokens_from_line(iLine)
    iIndent = len(lTemp.get_tokens()[0].get_value())
    return iLine, iIndent


def _build_actual_indent_dict(iLine, lTokens, iFirstLineIndent):    
    dReturn = {}
    dReturn[iLine] = iFirstLineIndent
     
    for iToken, oToken in enumerate(lTokens):

        iLine = utils.increment_line_number(iLine, oToken)

        if isinstance(oToken, parser.blank_line):
            continue

        if isinstance(oToken, parser.carriage_return):
            dReturn[iLine] = _set_indent(iToken, lTokens)
            continue

    return dReturn


def _build_index_dict(iLine, lTokens):
    dReturn = {}

    for iToken, oToken in enumerate(lTokens):

        iLine = utils.increment_line_number(iLine, oToken)

        if isinstance(oToken, parser.blank_line):
            continue

        if isinstance(oToken, parser.carriage_return):
            dReturn[iLine] = iToken + 1
            continue

    return dReturn


def _build_structure_list(iLine, iColumn, lTokens):

    lStructure = []

    for iToken, oToken in enumerate(lTokens):

        iLine = utils.increment_line_number(iLine, oToken)

        if isinstance(oToken, parser.blank_line):
            continue

        if isinstance(oToken, parser.carriage_return):
            iColumn = 0
            dReturn = {}
            dReturn['type'] = 'return'
            dReturn['line'] = iLine
            lStructure.append(dReturn)
            continue

        iColumn += len(oToken.get_value())

        if isinstance(oToken, parser.close_parenthesis):
            dParen = {}
            dParen['type'] = 'close'
            dParen['line'] = iLine
            dParen['column'] = iColumn
            dParen['begin_line'] = utils.does_token_start_line(iToken, lTokens)
            lStructure.append(dParen)

        if isinstance(oToken, parser.open_parenthesis):
            dParen = {}
            dParen['type'] = 'open'
            dParen['line'] = iLine
            dParen['column'] = iColumn
            lStructure.append(dParen)

        if oToken.get_value().lower() == 'when':
            dWhen = {}
            dWhen['type'] = 'when'
            dWhen['line'] = iLine
            dWhen['column'] = iColumn - 4
            dWhen['iToken'] = iToken
            lStructure.append(dWhen)

        if oToken.get_value().lower() == 'else':
            dElse = {}
            dElse['type'] = 'else'
            dElse['line'] = iLine
            dElse['column'] = iColumn - 4
            dElse['iToken'] = iToken
            lStructure.append(dElse)

    return lStructure, iLine


def _get_first_line(dActualIndent):
    lLines = list(dActualIndent.keys())
    lLines.sort()
    iLine = lLines[0]
    return iLine


def _get_last_line(dActualIndent):
    lLines = list(dActualIndent.keys())
    lLines.sort()
    iLine = lLines[-1]
    return iLine


def _update_structure(dExpectedIndent, dActualIndent, lStructure):
    iFirstLine = _get_first_line(dActualIndent)
    iLastLine = _get_last_line(dActualIndent)
    lReturn = []
    for iLine in range(iFirstLine, iLastLine + 1):
        iDeltaIndent = dExpectedIndent[iLine] - dActualIndent[iLine]
        for dStruct in lStructure:
            if dStruct['line'] == iLine:
                if dStruct['type'] != 'return':
                    dStruct['column'] += iDeltaIndent
                lReturn.append(dStruct)
    return lReturn


def _find_first_indent(sConfig, bStartsWithParen, dActualIndent, iIndentStep, iAssignColumn):
    iFirstLine = _get_first_line(dActualIndent)
    if sConfig == 'yes':
        if bStartsWithParen: 
            iFirstIndent = dActualIndent[iFirstLine]
        else:
            iFirstIndent = dActualIndent[iFirstLine] + iIndentStep
    else:
        iFirstIndent = iAssignColumn + 2 + 1
    return iFirstIndent

