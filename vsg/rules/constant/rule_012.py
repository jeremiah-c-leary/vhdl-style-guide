
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
            aToi = remove_non_arrays(aToi)
            populate_toi_parameters(aToi, oFile)
            aToi = remove_single_line_assignments(aToi)
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            dExpectedIndent = calculate_expected_indents(self, oToi)
            check_indents(self, dExpectedIndent, oToi)

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


def create_expected_indent_dict(iFirstLine, dActualIndent):
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]
    return dExpectedIndent


def get_parens_on_line(lParens, iLine):
    lReturn = []
    for dParen in lParens:
        if dParen['line'] == iLine:
            lReturn.append(dParen)
    return lReturn


def is_open_paren(dTemp):
    if dTemp['type'] == 'open':
        return True
    return False


def no_parens_on_line(lTemp):
    if len(lTemp) == 0:
        return True
    return False


def update_paren_depth(dParen, iParens):
    if is_open_paren(dParen):
        return iParens + 1
    else:
        return iParens - 1


def line_begins_with_close_paren(dParen):
    if not is_open_paren(dParen) and dParen['begin_line']:
        return True
    return False


def update_paren_depth_for_line(lLineParens, iParens):
    for dParen in lLineParens:
        iParens = update_paren_depth(dParen, iParens)
    return iParens


def set_current_line_indent(lLineParens, iLine, iIndentStep, dExpectedIndent):
    for dParen in lLineParens:
        if line_begins_with_close_paren(dParen):
            dExpectedIndent[iLine] -= iIndentStep


def _analyze_align_paren_false(oToi, iIndentStep):
    iFirstLine = oToi.iFirstLine
    iLastLine = oToi.iLastLine
    lParens = oToi.lParens
    dActualIndent = oToi.dActualIndent
    dExpectedIndent = create_expected_indent_dict(iFirstLine, dActualIndent)
#    print(iIndent)
    iFirstIndent = dActualIndent[iFirstLine]

    iIndent = iFirstIndent

    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')

        lLineParens = get_parens_on_line(lParens, iLine)

        if no_parens_on_line(lLineParens):
            dExpectedIndent[iLine + 1] = iIndent
            continue

        iParens = update_paren_depth_for_line(lLineParens, iParens)

        set_current_line_indent(lLineParens, iLine, iIndentStep, dExpectedIndent)

        iIndent = iFirstIndent + iParens * iIndentStep

#        print(f'indent = {iIndent} | iPerens = {iParens}')
        dExpectedIndent[iLine + 1] = iIndent

    return dExpectedIndent


def set_expected_column(iLine, oToi, dTemp, iIndentStep, iTemp):
    if iLine == oToi.iFirstLine:
        iColumn = dTemp['column'] + iIndentStep - 1
    else:
        iColumn = dTemp['column'] + (iTemp - oToi.dActualIndent[iLine]) + iIndentStep - 1
    return iColumn


def _analyze_align_paren_true(oToi, iIndentStep):
    iFirstLine = oToi.iFirstLine
    iLastLine = oToi.iLastLine
    lParens = oToi.lParens
    dActualIndent = oToi.dActualIndent
    iAssignColumn = oToi.iAssignColumn
    dExpectedIndent = create_expected_indent_dict(iFirstLine, dActualIndent)

    iIndent = dActualIndent[iFirstLine]
    iColumn = iIndent
    lColumn = [dActualIndent[iFirstLine]]

#    print('*'*80)
#    print(lParens)

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')
        lTemp = get_parens_on_line(lParens, iLine)

        if no_parens_on_line(lTemp):
            dExpectedIndent[iLine + 1] = lColumn[-1]
            continue

#        print(f'lTemp = {lTemp}')
        iTemp = lColumn[-1]
        for dTemp in lTemp:
            if is_open_paren(dTemp):
                iColumn = set_expected_column(iLine, oToi, dTemp, iIndentStep, iTemp)
#                print(f"iColumn = {dTemp['column']} + ({iTemp} - {dActualIndent[iLine]}) + {iIndentStep} - 1 = {iColumn}")
                lColumn.append(iColumn)
                dExpectedIndent[iLine + 1] = iColumn
            else:
                lColumn.pop()
                dExpectedIndent[iLine + 1] = lColumn[-1]
                if line_begins_with_close_paren(dTemp):
                    dExpectedIndent[iLine] = dExpectedIndent[iLine] - iIndentStep

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')

    return dExpectedIndent


def _analyze_align_paren_true_align_left_true(oToi, iIndentStep):
    iFirstLine = oToi.iFirstLine
    iLastLine = oToi.iLastLine
    lParens = oToi.lParens
    dActualIndent = oToi.dActualIndent
    iAssignColumn = oToi.iAssignColumn
    dExpectedIndent = create_expected_indent_dict(iFirstLine, dActualIndent)

    iIndent = dActualIndent[iFirstLine]
    iColumn = iIndent
    lColumn = [iColumn]

#    print('*'*80)
#    print(lParens)


    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')
        lTemp = get_parens_on_line(lParens, iLine)

        if no_parens_on_line(lTemp):
            dExpectedIndent[iLine + 1] = lColumn[-1]
            continue

#        print(f'lTemp = {lTemp}')
        iTemp = lColumn[-1]
        for dTemp in lTemp:
            if is_open_paren(dTemp):
                iColumn = set_expected_column(iLine, oToi, dTemp, iIndentStep, iTemp)
                lColumn.append(iColumn)
                dExpectedIndent[iLine + 1] = iColumn
            else:
                lColumn.pop()
                dExpectedIndent[iLine + 1] = lColumn[-1]
                if line_begins_with_close_paren(dTemp):
                    dExpectedIndent[iLine] = dExpectedIndent[iLine] - iIndentStep


        iParens = update_paren_depth_for_line(lTemp, iParens)

#        print(f'iParens = {iParens}')

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


def remove_single_line_assignments(lToi):
    lReturn = []
    for oToi in lToi:
        if oToi.iFirstLine != oToi.iLastLine:
            lReturn.append(oToi)
    return lReturn


def get_mapping_of_carriage_returns(oToi):
    dReturn = {}
    iLine, lTokens = utils.get_toi_parameters(oToi)
    for iToken, oToken in enumerate(lTokens):

        iLine = utils.increment_line_number(iLine, oToken)

        if isinstance(oToken, parser.carriage_return):
            dReturn[iLine] = iToken + 1
    return dReturn


def generate_paren_dicts(oToi):
    iLine, lTokens = utils.get_toi_parameters(oToi)

    iColumn = oToi.iAssignColumn

    lParens = []

    for iToken, oToken in enumerate(lTokens):

        iLine = utils.increment_line_number(iLine, oToken)

        iColumn = update_column_num(oToken, iColumn)

        update_close_paren_stats(lTokens, iLine, iColumn, iToken, lParens)
        update_open_paren_stats(oToken, iLine, iColumn, lParens)

    oToi.lParens = lParens


def update_actual_indent(oToi):
    iLine, lTokens = utils.get_toi_parameters(oToi)

    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if rules_utils.token_is_carriage_return(oToken):
            oToi.dActualIndent[iLine] = _set_indent(iToken, lTokens)


def update_column_num(oToken, iColumn):
    if rules_utils.token_is_carriage_return(oToken):
        return 0
    else:
        return iColumn + len(oToken.get_value())


def update_close_paren_stats(lTokens, iLine, iColumn, iToken, lParens):
    oToken = lTokens[iToken]
    if isinstance(oToken, parser.close_parenthesis):
        dParen = {}
        dParen['type'] = 'close'
        dParen['line'] = iLine
        dParen['column'] = iColumn
        dParen['begin_line'] = utils.does_token_start_line(iToken, lTokens)
        lParens.append(dParen)


def update_open_paren_stats(oToken, iLine, iColumn, lParens):
    if isinstance(oToken, parser.open_parenthesis):
        dParen = {}
        dParen['type'] = 'open'
        dParen['line'] = iLine
        dParen['column'] = iColumn
        lParens.append(dParen)


def set_last_line_number(oToi):
    iLine, lTokens = utils.get_toi_parameters(oToi)
    for iToken, oToken in enumerate(lTokens):

        iLine = utils.increment_line_number(iLine, oToken)

    oToi.iLastLine = iLine


def populate_toi_parameters(aToi, oFile):
    for oToi in aToi:
        oToi.iFirstLine, oToi.iFirstLineIndent = _get_first_line_info(oToi.iLine, oFile)
        oToi.iAssignColumn = oFile.get_column_of_token_index(oToi.get_start_index())
        oToi.iColumn = oToi.iAssignColumn
        oToi.dActualIndent = {}
        oToi.dActualIndent[oToi.iLine] = oToi.iFirstLineIndent
        oToi.lParens = []
        update_actual_indent(oToi)
        generate_paren_dicts(oToi)
        set_last_line_number(oToi)


def calculate_expected_indents(self, oToi):
    dExpectedIndent = {}
    if not self.align_paren and self.align_left:
        dExpectedIndent = _analyze_align_paren_false(oToi, self.indentSize)
    if self.align_paren and not self.align_left:
        dExpectedIndent = _analyze_align_paren_true(oToi, self.indentSize)
    if self.align_paren and self.align_left:
        dExpectedIndent = _analyze_align_paren_true_align_left_true(oToi, self.indentSize)
    return dExpectedIndent


def check_indents(self, dExpectedIndent, oToi):
    dIndex = get_mapping_of_carriage_returns(oToi)
    for iLine in range(oToi.iFirstLine, oToi.iLastLine + 1):
        if oToi.dActualIndent[iLine] == dExpectedIndent[iLine]:
            continue

        dAction = {}
        dAction['line'] = iLine
        dAction['column'] = dExpectedIndent[iLine]

        if oToi.dActualIndent[iLine] > 0:
            dAction['action'] = 'adjust'
        else:
            dAction['action'] = 'insert'

        sSolution = 'Adjust indent to column ' + str(dExpectedIndent[iLine])
        iToken = dIndex[iLine]
        oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution)
        oViolation.set_action(dAction)
        self.add_violation(oViolation)
