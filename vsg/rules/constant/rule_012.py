
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
            oLines = lines(oToi)
            oLines.set_first_line_indent(oToi.iFirstLineIndent)
#            print('-==-'*20)
            for x in oLines.lines:
                sString = ''
                for y in x.tokens:
                    sString += y.get_value()
#                print('='*80)
#                print(sString)
#                print(x.parens)
#                print(x.actual_indent)
#                print(x.number)
            calculate_expected_indents(self, oToi, oLines)
            check_indents(self, oToi, oLines)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
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


def analyze_align_left_true_align_paren_false(oToi, iIndentStep, oLines):
    iIndent = oLines.get_first_line_indent()
    iParens = 0
    for oLine in oLines.lines:
        if oLine.isFirst:
            oLines.set_first_line_expected_indent(iIndent)
        else:
            if rules_utils.token_list_begins_with_close_paren(oLine.tokens):
                oLine.set_expected_indent(iIndent + iParens * iIndentStep - iIndentStep)
            else:
                oLine.set_expected_indent(iIndent + iParens * iIndentStep)
    
        iParens += oLine.get_delta_parens()


def analyze_align_left_false_align_paren_true(oToi, iIndentStep, oLines):

    for oLine in oLines.lines:
        if oLine.isFirst:
            check_first_line(oLine, oLines, oToi)
        elif oLine.isLast:
            check_last_line(oLine, oLines)
        else:
            check_middle_line(oLine, oLines)

#    print('='*80)
#    print_expected_indents(oLines)


def print_expected_indents(oLines):
#    print('-'*80)
    for oLine in oLines.lines:
        print(f'[{oLine.number}][{oLine.iExpectedIndent}]')

def check_first_line(oLine, oLines, oToi):
    iIndent = oLines.get_first_line_indent()
    oLine.set_expected_indent(iIndent)

    iAdjust = oToi.iAssignColumn
#    print(f'iAdjust = {iAdjust}')
    oLines.update_parens(oLine, iAdjust)

    if oLines.no_parens():
        oLines.iNextIndent = iIndent
    else:
        oLines.iNextIndent = oLines.lParens[-1].iExpectedColumn
#        print(f'iNextIndent = {oLines.iNextIndent}')


def check_last_line(oLine, oLines):
    if oLine.starts_with_close_paren():
        oLine.set_expected_indent(oLines.iNextIndent - 1)
    else:
        oLine.set_expected_indent(oLines.iNextIndent)
    oLines.update_parens(oLine)


def check_middle_line(oLine, oLines):
    if oLines.no_parens():
        oLine.set_expected_indent(oLines.iNextIndent)
    elif oLine.starts_with_close_paren():
        oLine.set_expected_indent(oLines.iNextIndent - 1)
    else:
        oLine.set_expected_indent(oLines.iNextIndent)
    oLines.update_parens(oLine)
    oLines.iNextIndent = oLines.lParens[-1].iExpectedColumn


def debug_print_paren_list(lParens):
    sPrint = ''
    for oParen in lParens:
        sPrint += f'[{oParen.sType}|{oParen.iColumn}|{oParen.iExpectedColumn}|{oParen.iId}]'
    print(sPrint)

def print_line_num(iNum, sString):
    print(sString + '[' + str(iNum) + ']' + sString*80)


def analyze_align_paren_true(oToi, iIndentStep):
    iFirstLine = oToi.iFirstLine
    iLastLine = oToi.iLastLine
    lParens = oToi.lParens
    dActualIndent = oToi.dActualIndent
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


def set_expected_column(iLine, oToi, dTemp, iIndentStep, iTemp):
    if iLine == oToi.iFirstLine:
        iColumn = dTemp['column'] + iIndentStep - 1
    else:
        iColumn = dTemp['column'] + (iTemp - oToi.dActualIndent[iLine]) + iIndentStep - 1
    return iColumn



def _analyze_align_paren_true_align_left_true(oToi, iIndentStep):
    iFirstLine = oToi.iFirstLine
    iLastLine = oToi.iLastLine
    lParens = oToi.lParens
    dActualIndent = oToi.dActualIndent
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

        adjust_indent_left(iLine, oToi, dExpectedIndent, iParens, iIndentStep, lColumn)

#        print(f'{iLine} | {lColumn} | {dExpectedIndent}')

    return dExpectedIndent


def adjust_indent_left(iLine, oToi, dExpectedIndent, iParens, iIndentStep, lColumn):
    if iLine == oToi.iFirstLine or iParens == 1:
        dExpectedIndent[iLine + 1] = iParens * iIndentStep + oToi.dActualIndent[oToi.iFirstLine]
        lColumn[-1] = iParens * iIndentStep + oToi.dActualIndent[oToi.iFirstLine]


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
    for oToken in lTokens:

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


def calculate_expected_indents(self, oToi, oLines):
    dExpectedIndent = {}
    if not self.align_paren and self.align_left:
        dExpectedIndent = analyze_align_left_true_align_paren_false(oToi, self.indentSize, oLines)
    if self.align_paren and not self.align_left:
        dExpectedIndent = analyze_align_left_false_align_paren_true(oToi, self.indentSize, oLines)
    if self.align_paren and self.align_left:
        dExpectedIndent = _analyze_align_paren_true_align_left_true(oToi, self.indentSize)
    return dExpectedIndent


def check_indents(self, oToi, oLines):
    dIndex = get_mapping_of_carriage_returns(oToi)
    for oLine in oLines.lines:
        if oLine.actual_indent != oLine.iExpectedIndent:
            oViolation = create_violation(oToi, oLine)
            self.add_violation(oViolation)
            

def create_violation(oToi, oLine):
    iToken = oLine.token_index
    iLine = oLine.number
    lTokens = oToi.extract_tokens(iToken, iToken)
    sSolution = 'Adjust indent to column ' + str(oLine.iExpectedIndent)

    oViolation = violation.New(iLine, lTokens, sSolution)
    oViolation.set_action(create_action_dict(oLine))

    return oViolation


def create_action_dict(oLine):
    dAction = {}
    dAction['line'] = oLine.number
    dAction['column'] = oLine.iExpectedIndent

    if isinstance(oLine.tokens[0], parser.whitespace):
        dAction['action'] = 'adjust'
    else:
        dAction['action'] = 'insert'
    return dAction


class lines():

    def __init__(self, oToi):
        self.oToi = oToi
        self.convert_toi(oToi)
        self.update_paren_ids()
        self.lParens = []

    def convert_toi(self, oToi):
        self.lines = []
        iLine, lTokens = utils.get_toi_parameters(oToi)
        lLine = []
        bFirstLine = True
        iOffset = 0
        for iToken, oToken in enumerate(lTokens):
            lLine.append(oToken)
            if rules_utils.token_is_carriage_return(oToken):
                oLine = line(lLine, iLine, iToken - len(lLine) + 1, iOffset)
                oLine.isFirst = bFirstLine
                if iToken == len(lTokens):
                    oLine.isLast = True
                bFirstLine = False
                self.lines.append(oLine)
                iLine += 1
                iOffset = 0
                lLine = []

        oLine = line(lLine, iLine, iToken - len(lLine) + 1)
        oLine.isLast = True
        self.lines.append(oLine)

    def set_first_line_indent(self, iIndent):
        self.lines[0].actual_indent = iIndent

    def get_first_line_indent(self):
        return self.lines[0].actual_indent

    def set_first_line_expected_indent(self, iIndent):
        self.lines[0].set_expected_indent(iIndent)

    def update_paren_ids(self):
        iOpenId = 0
        lCloseParen = []
        for oLine in self.lines:
            for oParen in oLine.parens:
                if oParen.is_open():
                    oParen.iId = iOpenId
                    lCloseParen.append(iOpenId)
                    iOpenId += 1
                  
                if oParen.is_close():
                    oParen.iId = lCloseParen[-1]
                    lCloseParen.pop()

    def no_parens(self):
        if len(self.lParens) == 0:
            return True
        return False

    def update_parens(self, oLine, iAdjust=0):
       self.lParens = oLine.update_parens(self.lParens, iAdjust)


class line():

    def __init__(self, lLine, iLine, iToken, iIndent=0):
        self.number = iLine
        self.tokens = lLine
        self.parens = []
        self.detect_parenthesis(iIndent)
        self.set_actual_indent()
        self.token_index = iToken
        self.isFirst = False
        self.isLast = False
        self.iExpectedIndent = 0

    def detect_parenthesis(self, iIndent):
        iColumn = iIndent
        for oToken in self.tokens:
            iColumn += len(oToken.get_value())
            if rules_utils.token_is_open_paren(oToken):
                oParen = paren('open', iColumn)
                self.parens.append(oParen)
            if rules_utils.token_is_close_paren(oToken):
                oParen = paren('close', iColumn)
                self.parens.append(oParen)

    def set_actual_indent(self):
        oToken = self.tokens[0]
        self.actual_indent = 0
        if rules_utils.token_is_whitespace(oToken):
            self.actual_indent = len(oToken.get_value())

    def get_delta_parens(self):
        iReturn = 0
        for oParen in self.parens:
            if oParen.is_open():
                iReturn += 1
            else:
                iReturn -= 1
        return iReturn

    def set_expected_indent(self, iIndent):
        self.iExpectedIndent = iIndent

    def column_of_right_most_open_paren(self, iColumn, iParens=0):
        lParens = []
        for oToken in self.tokens:
            iColumn += len(oToken.get_value())
            if isinstance(oToken, parser.open_parenthesis):
                lParens.append(iColumn)
                iParens += 1
            if isinstance(oToken, parser.close_parenthesis):
                if len(lParens) > 0:
                    lParens.pop()
                    iParens -= 1
        if len(lParens) > 0:
            return lParens[-1]
        return None

    def starts_with_close_paren(self):
        return rules_utils.token_list_begins_with_close_paren(self.tokens)

    def update_column_list(self, lColumn, iAdjust=0):
        for oParen in self.parens:
            if oParen.is_open():
                iTemp = oParen.iColumn
                lColumn.append(iTemp - self.actual_indent + self.iExpectedIndent + 1)
            else:
                lColumn.pop()

    def update_parens(self, lParens, iAdjust=0):
#        print('-->update_parens')
        lReturn = []
        for oParen in self.parens:
#            print(f'{oParen.iColumn} + {iAdjust} - {self.actual_indent} + {self.iExpectedIndent}')
            oParen.iExpectedColumn = oParen.iColumn + iAdjust - self.actual_indent + self.iExpectedIndent
        lParens.extend(self.parens)
        for oParen in lParens:
            if oParen.is_open():
                lReturn.append(oParen)
            if oParen.is_close():
                lReturn.pop()
        return lReturn


class paren():

    def __init__(self, sType, iColumn, iId=None):
        self.sType = sType
        self.iColumn = iColumn
        self.iId = iId
        self.iExpectedColumn = iColumn

    def is_open(self):
        if self.sType == 'open':
            return True
        return False

    def is_close(self):
        if self.sType == 'close':
            return True
        return False


def debug_print_parens(oLines):
    print('--> debug_print_parens')
    for oLine in oLines.lines:
        sLine = f'[{oLine.number}][{oLine.iExpectedIndent}]'
        for oParen in oLine.parens:
            sLine += f'[{oParen.sType}|{oParen.iColumn}|{oParen.iId}]'
        print(sLine)
    print('<-- debug_print_parens')
