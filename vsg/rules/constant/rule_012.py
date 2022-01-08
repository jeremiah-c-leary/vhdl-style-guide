
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import alignment
from vsg.vhdlFile import utils

lTokenPairs = []
lTokenPairs.append([token.constant_declaration.assignment_operator, token.constant_declaration.semicolon])


class rule_012(alignment.Rule):
    '''
    This rule checks the alignment of multiline constants that contain arrays.

    Refer to section `Configuring Multiline Indent Rules <configuring.html#configuring-multiline-indent-rules>`_ for options.

    .. NOTE:: The structure of multiline array constants is handled by the rule `constant_016 <constant_rules.html#constant-016>`_.

    **Violation**

    .. code-block:: vhdl

       constant rom : romq_type :=
       (
                0,
            65535,
            32768
         );

    **Fix**

    .. code-block:: vhdl

       constant rom : romq_type :=
       (
         0,
         65535,
         32768
       );
    '''

    def __init__(self):
        alignment.Rule.__init__(self, 'constant', '012')
        self.subphase = 2
        self.lTokenPairs = lTokenPairs
        self.align_left = False
        self.configuration.append('align_left')
        self.align_paren = True
        self.configuration.append('align_paren')

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        lToi = remove_non_arrays(lToi)
        return lToi

    def analyze(self, oFile):
        self._print_debug_message('Analyzing rule: ' + self.unique_id)
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

            for iToken, oToken in enumerate(lTokens):

                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.blank_line):
                    continue

                if isinstance(oToken, parser.carriage_return):
                    iColumn = 0
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

            if not self.align_paren and self.align_left:
                dExpectedIndent = _analyze_align_paren_false(iFirstLine, iLastLine, lParens, self.indentSize, dActualIndent)
            if self.align_paren and not self.align_left:
                dExpectedIndent = _analyze_align_paren_true(iFirstLine, iLastLine, lParens, dActualIndent, self.indentSize, iAssignColumn)
            if self.align_paren and self.align_left:
                dExpectedIndent = _analyze_align_paren_true_align_left_true(iFirstLine, iLastLine, lParens, dActualIndent, self.indentSize, iAssignColumn)

#            print(f'Actual = {dActualIndent}')
#            print(f'Expect = {dExpectedIndent}')
#            print(f'Index  = {dIndex}')

            for iLine in range(iFirstLine, iLastLine + 1):
                if dActualIndent[iLine] == dExpectedIndent[iLine]:
                    continue

                dAction = {}
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


    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
#        print(dAction)
        if dAction['action'] == 'adjust':
            lTokens[0].set_value(' '*dAction['column'])
        else:
            rules_utils.insert_whitespace(lTokens, 0, dAction['column'])

        oViolation.set_tokens(lTokens)


def _set_indent(iToken, lTokens):
    iReturn = 0
    if isinstance(lTokens[iToken + 1], parser.whitespace):
        iReturn = len(lTokens[iToken + 1].get_value())
    else:
        iReturn = 0
    return iReturn


def _analyze_align_paren_false(iFirstLine, iLastLine, lParens, iIndentStep, dActualIndent):
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]
#    print(iIndent)
    iFirstIndent = dActualIndent[iFirstLine]

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

        iIndent = iFirstIndent + iParens * iIndentStep

#        print(f'indent = {iIndent} | iPerens = {iParens}')
        dExpectedIndent[iLine + 1] = iIndent

    return dExpectedIndent


def _analyze_align_paren_true(iFirstLine, iLastLine, lParens, dActualIndent, iIndentStep, iAssignColumn):
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    iIndent = dActualIndent[iFirstLine]
    iColumn = iIndent
    lColumn = [dActualIndent[iFirstLine]]

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
            dExpectedIndent[iLine + 1] = lColumn[-1]

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')

    return dExpectedIndent


def _analyze_align_paren_true_align_left_true(iFirstLine, iLastLine, lParens, dActualIndent, iIndentStep, iAssignColumn):
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    iIndent = dActualIndent[iFirstLine]
    iColumn = iIndent
    lColumn = [dActualIndent[iFirstLine]]

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
            dExpectedIndent[iLine + 1] = lColumn[-1]

        if iLine == iFirstLine:
            dExpectedIndent[iLine + 1] = iParens * iIndentStep + dActualIndent[iFirstLine]
            lColumn[-1] = iParens * iIndentStep + dActualIndent[iFirstLine]
        else:
            if iParens == 1:
                dExpectedIndent[iLine + 1] = iParens * iIndentStep + dActualIndent[iFirstLine]
                lColumn[-1] = iParens * iIndentStep + dActualIndent[iFirstLine]

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')

    return dExpectedIndent


def starts_with_paren(lTokens):

    iToken = utils.find_next_non_whitespace_token(1, lTokens)
    if isinstance(lTokens[iToken], parser.open_parenthesis):
        return True
    return False


def _get_first_line_info(iLine, oFile):
    lTemp = oFile.get_tokens_from_line(iLine)
    iIndent = len(lTemp.get_tokens()[0].get_value())
    return iLine, iIndent


def remove_non_arrays(lToi):
    lReturn = []
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if starts_with_paren(lTokens):
            lReturn.append(oToi)
    return lReturn
