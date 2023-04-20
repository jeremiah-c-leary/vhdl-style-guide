
from vsg import parser
from vsg import token

from vsg import tokens

from vsg.token import adding_operator
from vsg.token import aggregate
from vsg.token import direction
from vsg.token import exponent
from vsg.token import logical_operator
from vsg.token import miscellaneous_operator
from vsg.token import multiplying_operator
from vsg.token import relational_operator
from vsg.token import resolution_indication
from vsg.token import sign
from vsg.token import subtype_indication
from vsg.token import type_mark
from vsg.token import unary_logical_operator
from vsg.token import choices

from vsg.token.ieee.std_logic_1164 import types
from vsg.token.ieee.std_logic_1164 import function

from vsg.vhdlFile import extract
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import blank
from vsg.vhdlFile.classify import comment
from vsg.vhdlFile.classify import design_file
from vsg.vhdlFile.classify import whitespace
from vsg.vhdlFile.classify import preprocessor
from vsg.vhdlFile.classify import pragma

from vsg.vhdlFile.indent.set_token_indent import set_token_indent

from vsg.token_map import process_tokens

from vsg.vhdlFile import code_tags


class vhdlFile():
    '''
    Holds contents of a VHDL file.
    When a vhdlFile object is created, the contents of the file must be passed to it.
    A line object is created for each line read in.
    Then the line object attributes are updated.

    Parameters:

       filecontent: (list)

    Returns:

       fileobject
    '''
    def __init__(self, filecontent, sFilename=None, eError=None):
        self.filecontent = filecontent
        self.hasArchitecture = False
        self.hasEntity = False
        self.lAllObjects = []
        self.filename = sFilename
        self.dIndentMap = None
        self.lOpenPragmas = ['--vhdl_comp_off']
        self.lClosePragmas = ['--vhdl_comp_on']
        self.dVars = {}
        self.dVars['pragma'] = False
        self.eError = eError
        self._processFile()

    def _processFile(self):

        oOptions = options()
        self.lAllObjects = []
        for sLine in self.filecontent:
            lTokens = tokens.create(sLine.rstrip('\n').rstrip('\r'))
            lObjects = []
            for sToken in lTokens:
                lObjects.append(parser.item(sToken))

            blank.classify(lObjects, oOptions)
            whitespace.classify(lTokens, lObjects)
            comment.classify(lTokens, lObjects, oOptions)
            preprocessor.classify(lTokens, lObjects)
            pragma.classify(lTokens, lObjects, self.lOpenPragmas, self.lClosePragmas, self.dVars)

            self.lAllObjects.extend(lObjects)
            self.lAllObjects.append(parser.carriage_return())

        try:
            self.lAllObjects[0].set_filename(self.filename)
        except IndexError:
            pass

        design_file.tokenize(self.lAllObjects)
        post_token_assignments(self.lAllObjects)
        self.lAllObjects = combine_use_clause_selected_name(self.lAllObjects)

        set_token_hierarchy_value(self.lAllObjects)
        set_aggregate_tokens(self.lAllObjects)
        set_code_tags(self.lAllObjects)
        self.oTokenMap = process_tokens(self.lAllObjects)

    def update(self, lUpdates):

        if len(lUpdates) == 0:
            return
        bUpdateMap = True
        for oUpdate in lUpdates[::-1]:
            iStart = oUpdate.oTokens.iStartIndex
            lTokens = oUpdate.get_tokens()
            iEnd = oUpdate.oTokens.iEndIndex
            lMyTokens = remove_beginning_of_file_tokens(lTokens)
            self.lAllObjects[iStart:iEnd] = lMyTokens
        if bUpdateMap:
            self.oTokenMap = process_tokens(self.lAllObjects)

    def update_token_map(self):
        self.oTokenMap = process_tokens(self.lAllObjects)

    def set_indent_map(self, dIndentMap):
        self.dIndentMap = dIndentMap
        set_token_indent(self.dIndentMap, self.lAllObjects)

    def get_indent_map(self):
        return self.dIndentMap

    def get_object_lines(self):
        lReturn = []
        lReturn.append('')
        for lLine in split_on_carriage_return(self.lAllObjects):
            lReturn.append(lLine)
        return lReturn

    def get_lines(self):
        lReturn = []
        lReturn.append('')
        for lLine in split_on_carriage_return(self.lAllObjects):
            lReturn.append(utils.convert_token_list_to_string(lLine))
        return lReturn

    def get_line_count(self):
        return utils.count_carriage_returns(self.lAllObjects)

    def get_line_count_between_tokens(self, oStart, oEnd):
        return extract.get_line_count_between_tokens(oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def fix_blank_lines(self):
        self.lAllObjects = utils.fix_blank_lines(self.lAllObjects)

    def fix_trailing_whitespace(self):
        self.lAllObjects = utils.fix_trailing_whitespace(self.lAllObjects)

    def set_token_indent(self):
        set_token_indent(self.dIndentMap, self.lAllObjects)

    def get_line_preceeding_line(self, iLine, iNumLines=1):
        return extract.get_line_preceeding_line(iLine, self.lAllObjects, iNumLines, self.oTokenMap)

    def get_line_succeeding_line(self, iLine, iNumLines=1):
        return extract.get_line_succeeding_line(iLine, self.lAllObjects, iNumLines, self.oTokenMap)

    def get_all_tokens(self):
        return extract.get_all_tokens(self.lAllObjects)

    def get_sequence_of_tokens_matching(self, lTokens, bIgnoreIfLineStart=False):
        return extract.get_sequence_of_tokens_matching(lTokens, self.lAllObjects, self.oTokenMap, bIgnoreIfLineStart)

    def get_sequence_of_tokens_matching_bounded_by_tokens(self, lTokens, oStart, oEnd):
        return extract.get_sequence_of_tokens_matching_bounded_by_tokens(lTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_tokens_matching(self, lTokens):
        return extract.get_tokens_matching(lTokens, self.lAllObjects, self.oTokenMap)

    def get_tokens_matching_not_at_beginning_or_ending_of_line(self, lTokens):
        return extract.get_tokens_matching_not_at_beginning_or_ending_of_line(lTokens, self.lAllObjects, self.oTokenMap)

    def get_n_token_after_tokens(self, iToken, lTokens):
        return extract.get_n_token_after_tokens(iToken, lTokens, self.lAllObjects, self.oTokenMap)

    def get_n_tokens_before_token(self, iN, lTokens):
        return extract.get_m_tokens_before_and_n_tokens_after_token(iN, 0, lTokens, self.lAllObjects, self.oTokenMap)

    def get_n_tokens_after_token(self, iN, lTokens):
        return extract.get_m_tokens_before_and_n_tokens_after_token(0, iN, lTokens, self.lAllObjects, self.oTokenMap)

    def get_m_tokens_before_and_n_tokens_after_token(self, iM, iN, lTokens):
        return extract.get_m_tokens_before_and_n_tokens_after_token(iM, iN, lTokens, self.lAllObjects, self.oTokenMap)

    def get_n_token_after_tokens_between_tokens(self, iToken, lTokens, oStart, oEnd):
        return extract.get_n_token_after_tokens_between_tokens(iToken, lTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_tokens_matching_in_range_bounded_by_tokens(self, lTokens, oStart, oEnd):
        return extract.get_tokens_matching_in_range_bounded_by_tokens(lTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_tokens_bounded_by(self, oLeft, oRight, include_trailing_whitespace=False, bExcludeLastToken=False, bIncludeTillEndOfLine=False, bIncludeTillBeginningOfLine=False):
        return extract.get_tokens_bounded_by(oLeft, oRight, self.lAllObjects, self.oTokenMap, include_trailing_whitespace=include_trailing_whitespace, bExcludeLastToken=bExcludeLastToken, bIncludeTillEndOfLine=bIncludeTillEndOfLine, bIncludeTillBeginningOfLine=bIncludeTillBeginningOfLine)

    def get_tokens_bounded_by_token_when_between_tokens(self, oLeft, oRight, oStart, oEnd, include_trailing_whitespace=False):
        return extract.get_tokens_bounded_by_token_when_between_tokens(oLeft, oRight, oStart, oEnd, self.lAllObjects, self.oTokenMap, include_trailing_whitespace)

    def get_tokens_bounded_by_tokens_if_token_is_between_them(self, oLeft, oRight, oToken):
        return extract.get_tokens_bounded_by_tokens_if_token_is_between_them(oLeft, oRight, oToken, self.lAllObjects, self.oTokenMap)

    def get_tokens_bounded_by_unless_between(self, oLeft, oRight, lUnless):
        return extract.get_tokens_bounded_by_unless_between(oLeft, oRight, lUnless, self.lAllObjects, self.oTokenMap)

    def get_tokens_at_beginning_of_line_matching(self, lTokens):
        return extract.get_tokens_at_beginning_of_line_matching(lTokens, self.lAllObjects, self.oTokenMap)

    def get_tokens_at_beginning_of_line_matching_unless_between_tokens(self, lTokens, lUnless):
        return extract.get_tokens_at_beginning_of_line_matching_unless_between_tokens(lTokens, lUnless, self.lAllObjects, self.oTokenMap)

    def get_tokens_at_beginning_of_line_matching_between_tokens(self, lTokens, oStart, oEnd, bInclusive=False):
        return extract.get_tokens_at_beginning_of_line_matching_between_tokens(lTokens, oStart, oEnd, bInclusive, self.lAllObjects, self.oTokenMap)

    def get_column_of_token_index(self, iToken):
        return extract.get_column_of_token_index(iToken, self.lAllObjects, self.oTokenMap)

    def get_line_above_line_starting_with_token(self, lTokens, bIncludeComments):
        return extract.get_line_above_line_starting_with_token(lTokens, self.lAllObjects, self.oTokenMap, bIncludeComments)

    def get_line_above_line_starting_with_token_with_hierarchy(self, lTokens, lHierarchy, bIncludeComments):
        return extract.get_line_above_line_starting_with_token_with_hierarchy(lTokens, self.lAllObjects, lHierarchy, self.oTokenMap, bIncludeComments)

    def get_line_below_line_ending_with_token(self, lTokens):
        return extract.get_line_below_line_ending_with_token(lTokens, self.lAllObjects, self.oTokenMap)

    def get_line_below_line_ending_with_several_possible_tokens(self, lTokens):
        return extract.get_line_below_line_ending_with_several_possible_tokens(lTokens, self.lAllObjects, self.oTokenMap)

    def get_line_below_line_ending_with_token_with_hierarchy(self, lTokens, lHierarchy):
        return extract.get_line_below_line_ending_with_token_with_hierarchy(lTokens, self.lAllObjects, lHierarchy, self.oTokenMap)

    def get_line_which_includes_tokens(self, lTokens):
        return extract.get_line_which_includes_tokens(lTokens, self.lAllObjects, self.oTokenMap)

    def get_if_statement_conditions(self, fRemoveWhitespace=True):
        return extract.get_if_statement_conditions(self.lAllObjects, self.oTokenMap, fRemoveWhitespace)

    def get_n_tokens_before_and_after_tokens(self, iToken, lTokens):
        return extract.get_n_tokens_before_and_after_tokens(iToken, lTokens, self.lAllObjects, self.oTokenMap)

    def get_n_tokens_before_and_after_tokens_bounded_by_tokens(self, iToken, lTokens, lBetween):
        return extract.get_n_tokens_before_and_after_tokens_bounded_by_tokens(iToken, lTokens, lBetween, self.lAllObjects, self.oTokenMap)

    def get_sequence_of_tokens_not_matching(self, lTokens):
        return extract.get_sequence_of_tokens_not_matching(lTokens, self.lAllObjects, self.oTokenMap)

    def get_tokens_between_tokens_inclusive_while_storing_value_from_token(self, left_token, right_token, value_token):
        return extract.get_tokens_between_tokens_inclusive_while_storing_value_from_token(left_token, right_token, value_token, self.lAllObjects, self.oTokenMap)

    def get_tokens_between_non_whitespace_token_and_token(self, right_token):
        return extract.get_tokens_between_non_whitespace_token_and_token(right_token, self.lAllObjects, self.oTokenMap)

    def get_tokens_from_line(self, iLineNumber):
        return extract.get_tokens_from_line(iLineNumber, self.lAllObjects, self.oTokenMap)

    def get_consecutive_lines_starting_with_token(self, search_token, min_num_lines=2):
        return extract.get_consecutive_lines_starting_with_token(search_token, min_num_lines, self.lAllObjects, self.oTokenMap)

    def get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(self, search_token, stop_token):
        return extract.get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(search_token, stop_token, self.lAllObjects, self.oTokenMap)

    def get_tokens_where_line_starts_with_token_until_ending_token_is_found(self, start_token, stop_token):
        return extract.get_tokens_where_line_starts_with_token_until_ending_token_is_found(start_token, stop_token, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_before_it(self, oToken, iTokens):
        return extract.get_token_and_n_tokens_before_it(oToken, iTokens, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_before_it_in_between_tokens(self, lTokens, iTokens, oStart, oEnd):
        return extract.get_token_and_n_tokens_before_it_in_between_tokens(lTokens, iTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_before_it_in_between_tokens_unless_token_is_found(self, lTokens, iTokens, oStart, oEnd, oStop):
        return extract.get_token_and_n_tokens_before_it_in_between_tokens_unless_token_is_found(lTokens, iTokens, oStart, oEnd, oStop, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_after_it(self, lTokens, iTokens):
        return extract.get_token_and_n_tokens_after_it(lTokens, iTokens, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_after_it_when_between_tokens(self, lTokens, iTokens, oStart, oEnd):
        return extract.get_token_and_n_tokens_after_it_when_between_tokens(lTokens, iTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_blank_lines_below_line_ending_with_token(self, lTokens, lHierarhcy=None):
        return extract.get_blank_lines_below_line_ending_with_token(lTokens, lHierarhcy, self.lAllObjects, self.oTokenMap)

    def get_blank_lines_below_line_ending_with_several_possible_tokens(self, lTokens):
        return extract.get_blank_lines_below_line_ending_with_several_possible_tokens(lTokens, self.lAllObjects, self.oTokenMap)

    def get_blank_lines_above_line_starting_with_token(self, lTokens):
        return extract.get_blank_lines_above_line_starting_with_token(lTokens, self.lAllObjects, self.oTokenMap)

    def get_blank_lines_above_line_starting_with_token_when_between_tokens(self, lTokens, lBetweenTokens):
        return extract.get_blank_lines_above_line_starting_with_token_when_between_tokens(lTokens, lBetweenTokens, self.lAllObjects, self.oTokenMap)

    def get_association_elements_between_tokens(self, oStart, oEnd):
        return extract.get_association_elements_between_tokens(oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_interface_elements_between_tokens(self, oStart, oEnd, include_end_of_line_comments=False):
        return extract.get_interface_elements_between_tokens(oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_lines_with_length_that_exceed_column(self, iColumn):
        return extract.get_lines_with_length_that_exceed_column(iColumn, self.lAllObjects, self.oTokenMap)

    def get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(self, lStartTokens, lEndTokens, bIncludeStartToken=False, bIncludeEndToken=True, bEarliestDetect=False):
        return extract.get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(lStartTokens, lEndTokens, self.lAllObjects, self.oTokenMap, bIncludeStartToken, bIncludeEndToken, bEarliestDetect)

    def get_tokens_between_indexes(self, iStartIndex, iEndIndex):
        return extract.get_tokens_between_indexes(iStartIndex, iEndIndex, self.lAllObjects)

    def get_tokens_from_beginning_of_line_containing_token_to_the_next_non_whitespace_token_to_the_right(self, token):
        return extract.get_tokens_from_beginning_of_line_containing_token_to_the_next_non_whitespace_token_to_the_right(token, self.lAllObjects, self.oTokenMap)

    def get_indent_of_line_at_index(self, iIndex):
        for iToken in range(iIndex, 0, -1):
            oToken = self.lAllObjects[iToken]
            if oToken.get_indent() is not None:
                return oToken.get_indent()
        return 0

    def get_tokens_in_declarative_parts(self):
        return extract.get_tokens_in_declarative_parts(self.lAllObjects, self.oTokenMap)


def split_on_carriage_return(lObjects):
    lReturn = []
    lMyObjects = []
    iLine = 1
    for oObject in lObjects:
        if isinstance(oObject, parser.carriage_return):
            lReturn.append(lMyObjects)
            iLine += 1
            lMyObjects = []
        else:
            lMyObjects.append(oObject)
    if len(lMyObjects) > 0:
        lReturn.append(lMyObjects)
    return lReturn


def post_token_assignments(lTokens):
    oCodeTags = code_tags.New()
    iParenId = 0
    lParenId = []
    for iToken, oToken in enumerate(lTokens):

        if isinstance(oToken, subtype_indication.type_mark) or isinstance(oToken, resolution_indication.resolution_function_name) or isinstance(oToken, type_mark.name):
            sValue = oToken.get_value()
            ### IEEE values
            if sValue.lower() == 'std_logic_vector':
                lTokens[iToken] = types.std_logic_vector(sValue)

            elif sValue.lower() == 'std_ulogic_vector':
                lTokens[iToken] = types.std_ulogic_vector(sValue)

            elif sValue.lower() == 'std_ulogic':
                lTokens[iToken] = types.std_ulogic(sValue)

            elif sValue.lower() == 'std_logic':
                lTokens[iToken] = types.std_logic(sValue)

            elif sValue.lower() == 'integer':
                lTokens[iToken] = types.integer(sValue)

            elif sValue.lower() == 'signed':
                lTokens[iToken] = types.signed(sValue)

        elif isinstance(oToken, parser.todo):
            sValue = oToken.get_value()
            if sValue == '&':
                lTokens[iToken] = adding_operator.concat()

            elif sValue  == '+':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.keyword], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.comma], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([choices.bar], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                else:
                    lTokens[iToken] = adding_operator.plus()

            elif sValue  == '-':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.keyword], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.comma], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([choices.bar], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                else:
                    lTokens[iToken] = adding_operator.minus()

            elif sValue == '(':
                lTokens[iToken] = parser.open_parenthesis()
                iParenId += 1
                lParenId.append(iParenId)
                lTokens[iToken].iId = iParenId

            elif sValue == ')':
                lTokens[iToken] = parser.close_parenthesis()
                lTokens[iToken].iId = lParenId.pop()

            elif sValue == ',':
                lTokens[iToken] = parser.comma()

            elif sValue.lower() == 'to':
                lTokens[iToken] = direction.to(sValue)

            elif sValue.lower() == 'downto':
                lTokens[iToken] = direction.downto(sValue)

            elif sValue.lower() == 'and':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.and_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.and_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.comma], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.and_operator(sValue)
                else:
                    lTokens[iToken] = logical_operator.and_operator(sValue)

            elif sValue.lower() == 'or':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.or_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.or_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.comma], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.or_operator(sValue)
                else:
                    lTokens[iToken] = logical_operator.or_operator(sValue)

            elif sValue.lower() == 'nand':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.nand_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.nand_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.comma], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.nand_operator(sValue)
                else:
                    lTokens[iToken] = logical_operator.nand_operator(sValue)

            elif sValue.lower() == 'nor':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.nor_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.nor_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.comma], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.nor_operator(sValue)
                else:
                    lTokens[iToken] = logical_operator.nor_operator(sValue)

            elif sValue.lower() == 'xor':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.xor_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.xor_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.comma], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.xor_operator(sValue)
                else:
                    lTokens[iToken] = logical_operator.xor_operator(sValue)

            elif sValue.lower() == 'xnor':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.xnor_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.xnor_operator(sValue)
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.comma], iToken - 1, lTokens):
                    lTokens[iToken] = unary_logical_operator.xnor_operator(sValue)
                else:
                    lTokens[iToken] = logical_operator.xnor_operator(sValue)

            elif sValue.lower() == '**':
                lTokens[iToken] = miscellaneous_operator.double_star(sValue)

            elif sValue.lower() == 'abs':
                lTokens[iToken] = miscellaneous_operator.abs_operator(sValue)

            elif sValue.lower() == 'not':
                lTokens[iToken] = miscellaneous_operator.not_operator(sValue)

            elif sValue.lower() == '*':
                lTokens[iToken] = multiplying_operator.star(sValue)

            elif sValue.lower() == '/':
                lTokens[iToken] = multiplying_operator.slash(sValue)

            elif sValue.lower() == 'mod':
                lTokens[iToken] = multiplying_operator.mod_operator(sValue)

            elif sValue.lower() == 'rem':
                lTokens[iToken] = multiplying_operator.rem_operator(sValue)

            elif sValue == '=':
                lTokens[iToken] = relational_operator.equal(sValue)

            elif sValue == "'":
                lTokens[iToken] = parser.tic(sValue)
                utils.classify_predefined_types(lTokens, iToken + 1)

            elif sValue.lower() == 'event':
                lTokens[iToken] = parser.event_keyword(sValue)

            ### IEEE values
            elif sValue.lower() == 'rising_edge':
                lTokens[iToken] = function.rising_edge(sValue)

            elif sValue.lower() == 'falling_edge':
                lTokens[iToken] = function.falling_edge(sValue)

            elif sValue.lower() == 'std_logic_vector':
                lTokens[iToken] = types.std_logic_vector(sValue)

            elif sValue.lower() == 'std_ulogic_vector':
                lTokens[iToken] = types.std_ulogic_vector(sValue)

            elif sValue.lower() == 'std_ulogic':
                lTokens[iToken] = types.std_ulogic(sValue)

            elif len(sValue) == 3 and sValue.startswith("'") and sValue.endswith("'"):
                lTokens[iToken] = parser.character_literal(sValue)
        else:
            sValue = oToken.get_value()
            if sValue  == '+':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([exponent.e_keyword], iToken - 1, lTokens):
                    pass
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.keyword], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                else:
                    lTokens[iToken] = adding_operator.plus()
            elif sValue  == '-':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([exponent.e_keyword], iToken - 1, lTokens):
                    pass
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.keyword], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                else:
                    lTokens[iToken] = adding_operator.minus()
            elif sValue.lower() == '*':
                lTokens[iToken] = multiplying_operator.star(sValue)
            elif sValue.lower() == '/':
                lTokens[iToken] = multiplying_operator.slash(sValue)
            elif sValue.lower() == '**':
                lTokens[iToken] = miscellaneous_operator.double_star(sValue)
            elif sValue == '(':
                iParenId += 1
                lParenId.append(iParenId)
                oToken.iId = iParenId
            elif sValue == ')':
                oToken.iId = lParenId.pop()


def set_token_hierarchy_value(lTokens):
    iIfHierarchy = 0
    for oToken in lTokens:
        if isinstance(oToken, token.if_statement.if_keyword):
            oToken.set_hierarchy(iIfHierarchy)
            iIfHierarchy += 1
        if isinstance(oToken, token.if_statement.elsif_keyword):
            oToken.set_hierarchy(iIfHierarchy - 1)
        if isinstance(oToken, token.if_statement.else_keyword):
            oToken.set_hierarchy(iIfHierarchy - 1)
        if isinstance(oToken, token.if_statement.semicolon):
            iIfHierarchy -= 1
            oToken.set_hierarchy(iIfHierarchy)


def set_code_tags(lTokens):
    oCodeTags = code_tags.New()
    for oToken in lTokens:
        if code_tags.token_has_vsg_on_code_tag(oToken):
            oToken.set_code_tags(oCodeTags.get_tags())
            oCodeTags.update(oToken)
        elif code_tags.token_has_vsg_off_code_tag(oToken):
            oCodeTags.update(oToken)
            oToken.set_code_tags(oCodeTags.get_tags())
        elif code_tags.token_has_next_line_code_tag(oToken):
            oCodeTags.update(oToken)
            oToken.set_code_tags(oCodeTags.get_tags())
        else:
            oToken.set_code_tags(oCodeTags.get_tags())
            oCodeTags.update(oToken)


def set_aggregate_tokens(lTokens):
    lOpenParens = []
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, parser.open_parenthesis):
            lOpenParens.append(iToken)
        if isinstance(oToken, parser.close_parenthesis):
            iIndex = lOpenParens.pop()
            if isinstance(lTokens[iIndex], token.aggregate.open_parenthesis):
                lTokens[iToken] = token.aggregate.close_parenthesis()
        if isinstance(oToken, token.element_association.assignment):
            lTokens[lOpenParens[-1]] = token.aggregate.open_parenthesis()


def combine_use_clause_selected_name(lTokens):
    lReturn = []
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, token.use_clause.selected_name):
            if isinstance(lReturn[-1], token.use_clause.selected_name):
                lReturn[-1].value = lReturn[-1].value + oToken.value
                continue
        lReturn.append(oToken)
    return lReturn


def remove_beginning_of_file_tokens(lTokens):
    lReturn = []
    for oToken in lTokens:
        if not isinstance(oToken, parser.beginning_of_file):
            lReturn.append(oToken)
    return lReturn


class options():

    def __init__(self):
        self.bInsideDelimitedComment = False

    def set_inside_delimited_comment(self):
        self.bInsideDelimitedComment = True

    def clear_inside_delimited_comment(self):
        self.bInsideDelimitedComment = False

    def inside_delimited_comment(self):
        return self.bInsideDelimitedComment
