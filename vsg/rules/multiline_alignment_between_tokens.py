
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import alignment
from vsg.vhdlFile import utils


class multiline_alignment_between_tokens(alignment.Rule):
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

    def __init__(self, name, identifier, lTokenPairs, bExcludeLastToken=False):
        alignment.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 4
        self.lTokenPairs = lTokenPairs
        self.bExcludeLastToken = bExcludeLastToken
        self.align_left = 'no'
        self.configuration.append('align_left')
        self.align_paren = 'yes'
        self.configuration.append('align_paren')
        self.bIgnoreStartParen = False

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1], bExcludeLastToken=self.bExcludeLastToken)
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def analyze(self, oFile):
        lToi = self._get_tokens_of_interest(oFile)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
#            print('='*5 + str(iLine) + '='*70)

            iFirstLine, iFirstLineIndent = _get_first_line_info(iLine, oFile)

            iAssignColumn = oFile.get_column_of_token_index(oToi.get_start_index())
            iColumn = iAssignColumn

            dActualIndent = {}

            dActualIndent[iLine] = iFirstLineIndent
            lParens = []
            dIndex = {}

            bStartsWithParen = _starts_with_paren(lTokens)
            bSkipCommentLine = False

            for iToken, oToken in enumerate(lTokens):

                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.blank_line):
                    continue

                if bSkipCommentLine:
                   if not isinstance(oToken, parser.carriage_return):
                       continue

                if isinstance(oToken, parser.carriage_return):
                    iColumn = 0
                    bSkipCommentLine = rules_utils.does_line_start_with_comment(lTokens[iToken + 1:iToken + 3])
                    if bSkipCommentLine:
                        dActualIndent[iLine] = None
                    else:
                        dActualIndent[iLine] = _set_indent(iToken, lTokens)
                        dIndex[iLine] = iToken + 1
                    continue

                iColumn += len(oToken.get_value())

                if isinstance(oToken, parser.close_parenthesis):
                    dParen = {}
                    dParen['type'] = 'close'
                    dParen['line'] = iLine
                    dParen['column'] = iColumn
                    dParen['begin_line'] = utils.does_token_start_line(iToken, lTokens)
                    lParens.append(dParen)

                if isinstance(oToken, parser.open_parenthesis):
                    dParen = {}
                    dParen['type'] = 'open'
                    dParen['line'] = iLine
                    dParen['column'] = iColumn
                    lParens.append(dParen)

            iLastLine = iLine

            if iFirstLine == iLastLine:
                continue

            iFirstTokenLength = len(lTokens[0].get_value())

            if self.align_paren == 'no' and self.align_left == 'yes':
                dExpectedIndent = _analyze_align_paren_no(iFirstLine, iLastLine, lParens, self.indentSize, dActualIndent, bStartsWithParen, self.bIgnoreStartParen)
            if self.align_paren == 'yes' and self.align_left == 'no':
                dExpectedIndent = _analyze_align_paren_yes_align_left_no(iFirstLine, iLastLine, lParens, dActualIndent, self.indentSize, bStartsWithParen, iAssignColumn, iFirstTokenLength, self.bIgnoreStartParen)
            if self.align_paren == 'yes' and self.align_left == 'yes':
                dExpectedIndent = _analyze_align_paren_yes_align_left_yes(iFirstLine, iLastLine, lParens, dActualIndent, self.indentSize, bStartsWithParen, iAssignColumn, self.bIgnoreStartParen)
            if self.align_paren == 'no' and self.align_left == 'no':
                dExpectedIndent = _analyze_align_paren_no_align_left_no(iFirstLine, iLastLine, lParens, dActualIndent, self.indentSize, bStartsWithParen, iAssignColumn, self.bIgnoreStartParen)


#            print(f'Actual = {dActualIndent}')
#            print(f'Expect = {dExpectedIndent}')
#            print(f'Index  = {dIndex}')

            for iLine in range(iFirstLine, iLastLine + 1):
                if dActualIndent[iLine] is None:
                    continue
                if indents_match(dActualIndent[iLine], dExpectedIndent[iLine]):
                    continue

                oViolation = build_violation(iLine, oToi, iToken, dExpectedIndent, dIndex, dActualIndent)
                self.add_violation(oViolation)


    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
#        print(dAction)
        if dAction['action'] == 'adjust':
            lTokens[0].set_value(' '*dAction['column'])
        else:
            rules_utils.insert_whitespace(lTokens, 0, dAction['column'])

        oViolation.set_tokens(lTokens)


def build_violation(iLine, oToi, iToken, dExpectedIndent, dIndex, dActualIndent):
    sSolution = 'Adjust indent to column ' + str(dExpectedIndent[iLine])
    dAction = build_action_dictionary(iLine, dActualIndent, dExpectedIndent)
    iToken = dIndex[iLine]
    oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution)
    oViolation.set_action(dAction)
    return oViolation


def build_action_dictionary(iLine, dActualIndent, dExpectedIndent):
    dAction = {}
    dAction['line'] = iLine
    dAction['column'] = dExpectedIndent[iLine]

    if dActualIndent[iLine] > 0:
        dAction['action'] = 'adjust'
    else:
        dAction['action'] = 'insert'
    return dAction


def line_starts_with_comment(iActual):
    if iActual is None:
        return True
    return False


def indents_match(iActual, iExpected):
    if iActual == iExpected:
        return True
    return False


def calculate_start_column(oFile, oToi):
    iReturn = oFile.get_column_of_token_index(oToi.get_start_index())
    iReturn += len(oToi.get_tokens()[0].get_value())
    iReturn += 1
#    print(f'Start Column = {iReturn}')
    return iReturn


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


def _analyze_align_paren_no(iFirstLine, iLastLine, lParens, iIndentStep, dActualIndent, bStartsWithParen, bIgnoreStartParen):
#    print('--> _analyze_align_paren_no <-' + '-'*70)
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]
    if bStartsWithParen or bIgnoreStartParen:
        iFirstIndent = dActualIndent[iFirstLine]
    else:
        iFirstIndent = dActualIndent[iFirstLine] + iIndentStep

    iIndent = iFirstIndent

#    print(iIndent)
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

        iIndent = iFirstIndent + iParens * iIndentStep

#        print(f'indent = {iIndent} | iPerens = {iParens}')
        dExpectedIndent[iLine + 1] = iIndent
#        print(dExpectedIndent)

    return dExpectedIndent


def _analyze_align_paren_yes_align_left_no(iFirstLine, iLastLine, lParens, dActualIndent, iIndentStep, bStartsWithParen, iAssignColumn, iFirstTokenLength, bIgnoreStartParen):
#    print('--> _analyze_align_paren_yes_align_left_no <-' + '-'*70)
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

#    if bStartsWithParen:
#       iIndent = dActualIndent[iFirstLine]
#       iColumn = iIndent
#       lColumn = [dActualIndent[iFirstLine]]
#    else:
    if bIgnoreStartParen:
        iIndent = iAssignColumn + iFirstTokenLength
    else:
        iIndent = iAssignColumn + iFirstTokenLength + 1

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
                    iColumn = dTemp['column']
                else:
                    iColumn = dTemp['column'] + (iTemp - dActualIndent[iLine]) + iIndentStep - 1
#                print(f"iColumn = {dTemp['column']} + ({iTemp} - {dActualIndent[iLine]}) + {iIndentStep} - 1 = {iColumn}")
                lColumn.append(iColumn)
                if bIgnoreStartParen:
                    dExpectedIndent[iLine + 1] = iColumn + 1
                else:
                    dExpectedIndent[iLine + 1] = iColumn
            else:
                iParens -= 1
                lColumn.pop()
                if bIgnoreStartParen:
                    dExpectedIndent[iLine + 1] = lColumn[-1] + 1
                else:
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


def _analyze_align_paren_yes_align_left_yes(iFirstLine, iLastLine, lParens, dActualIndent, iIndentStep, bStartsWithParen, iAssignColumn, bIgnoreStartParen):
#    print('--> _analyze_align_paren_yes_align_left_yes <-' + '-'*70)
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    if bStartsWithParen:
       iIndent = dActualIndent[iFirstLine]
       iColumn = iIndent
       lColumn = [dActualIndent[iFirstLine]]
    else:
#       if bIgnoreStartParen:
#           iIndent = dActualIndent[iFirstLine]
#       else:
       iIndent = iAssignColumn + 2 + 1
       iColumn = iIndent
       lColumn = [iIndent]
#    print(iIndent)
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
            dExpectedIndent[iLine + 1] = iParens * iIndentStep + dActualIndent[iFirstLine] + iIndentStep
            lColumn[-1] = iParens * iIndentStep + dActualIndent[iFirstLine] + iIndentStep
            if iParens == 0 and not bStartsWithParen:
                dExpectedIndent[iLine + 1] = iIndentStep + dActualIndent[iFirstLine]
                lColumn[-1] = iIndentStep + dActualIndent[iFirstLine]
            elif iParens == 0 and bStartsWithParen:
                dExpectedIndent[iLine + 1] = dActualIndent[iFirstLine]
                lColumn[-1] = dActualIndent[iFirstLine]
            if bIgnoreStartParen:
                dExpectedIndent[iLine + 1] = dActualIndent[iFirstLine] + iIndentStep
                lColumn[-1] = dActualIndent[iFirstLine] + iIndentStep

        else:
            if iParens == 1:
                dExpectedIndent[iLine + 1] = iParens * iIndentStep + dActualIndent[iFirstLine]
                lColumn[-1] = iParens * iIndentStep + dActualIndent[iFirstLine]

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')

    return dExpectedIndent


def _analyze_align_paren_no_align_left_no(iFirstLine, iLastLine, lParens, dActualIndent, iIndentStep, bStartsWithParen, iAssignColumn, bIgnoreStartParen):
#    print('--> _analyze_align_paren_no <-' + '-'*70)
#    print(iAssignColumn)
#    print(lParens)
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]
#    print(iIndent)
    if bStartsWithParen:
        iFirstIndent = dActualIndent[iFirstLine]
    elif bIgnoreStartParen:
        iFirstIndent = lParens[0]['column'] + 1
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
            elif bIgnoreStartParen:
                iIndent = iFirstIndent
            else:
                if iParens == 0:
                    iIndent = iFirstIndent + iParens * iIndentStep
                else:
                    iIndent = iFirstIndent + iParens * iIndentStep - iIndentStep + iIndentStep
        else:
            if iParens == 0:
                iIndent = iFirstIndent + iParens * iIndentStep
            elif bIgnoreStartParen:
                iIndent = iFirstIndent + iParens * iIndentStep - iIndentStep
            else:
                iIndent = iFirstIndent + iParens * iIndentStep + iIndentStep

#        print(f'indent = {iIndent} | iPerens = {iParens}')
        dExpectedIndent[iLine + 1] = iIndent

    return dExpectedIndent


def _starts_with_paren(lTokens):
    iToken = utils.find_next_non_whitespace_token(1, lTokens)
    try:
        if isinstance(lTokens[iToken], parser.open_parenthesis):
            return True
    except IndexError:
        if isinstance(lTokens[0], parser.open_parenthesis):
            return True
    return False


def _get_first_line_info(iLine, oFile):
    lTemp = oFile.get_tokens_from_line(iLine)
    iIndent = len(lTemp.get_tokens()[0].get_value())
    return iLine, iIndent

