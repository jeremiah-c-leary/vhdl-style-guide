# -*- coding: utf-8 -*-

from vsg import config, exceptions, parser, token, tokens
from vsg.token import (
    adding_operator,
    aggregate,
    choices,
    direction,
    exponent,
    logical_operator,
    miscellaneous_operator,
    multiplying_operator,
    predefined_attribute,
    relational_operator,
    resolution_indication,
    sign,
    todo,
    type_mark,
    unary_logical_operator,
)
from vsg.token.ieee.std_logic_1164 import function, types
from vsg.token_map import process_tokens
from vsg.vhdlFile import code_tags, extract, utils
from vsg.vhdlFile.classify import (
    blank,
    comment,
    design_file,
    pragma,
    preprocessor,
    whitespace,
)
from vsg.vhdlFile.indent.set_token_indent import set_token_indent


class command_line_args:
    """This is used as an input into the version command."""

    def __init__(self, version=False):
        self.version = version
        self.style = "indent_only"
        self.configuration = []
        self.debug = False
        self.fix_only = False
        self.stdin = False
        self.force_fix = False
        self.fix = False


default_cla = command_line_args()

default_conf = config.New(default_cla)


class vhdlFile:
    """
    Holds contents of a VHDL file.
    When a vhdlFile object is created, the contents of the file must be passed to it.
    A line object is created for each line read in.
    Then the line object attributes are updated.

    Parameters:

       filecontent: (list)

    Returns:

       fileobject
    """

    def __init__(self, filecontent, commandLineArguments=default_cla, sFilename=None, eError=None, configuration=default_conf):
        self.filecontent = filecontent
        self.hasArchitecture = False
        self.hasEntity = False
        self.lAllObjects = []
        self.filename = sFilename
        self.dIndentMap = None
        self.lOpenPragmas = ["--vhdl_comp_off"]
        self.lClosePragmas = ["--vhdl_comp_on"]
        self.dVars = {}
        self.dVars["pragma"] = False
        self.eError = eError
        self.stdin = commandLineArguments.stdin
        self.configuration = configuration
        self.commandLineArguments = commandLineArguments
        #        p = cProfile.Profile()
        #        p.runcall(self._processFile)
        #        p.print_stats()
        self._processFile()

    def _processFile(self):
        oOptions = options()
        self.lAllObjects = []
        for sLine in self.filecontent:
            self.dVars["line"] = sLine
            lTokens = tokens.create(sLine.rstrip("\n").rstrip("\r"))
            lObjects = []
            for sToken in lTokens:
                lObjects.append(parser.item(sToken))

            blank.classify(lObjects, oOptions)
            whitespace.classify(lTokens, lObjects)
            comment.classify(lTokens, lObjects, oOptions)
            preprocessor.classify(lTokens, lObjects)
            pragma.classify(lObjects, self.lOpenPragmas, self.lClosePragmas, self.dVars, self.configuration)

            self.lAllObjects.extend(lObjects)
            self.lAllObjects.append(parser.carriage_return())

        try:
            self.lAllObjects[0].set_filename(self.filename)
        except IndexError:
            pass

        try:
            design_file.tokenize(self.lAllObjects)
        except exceptions.ClassifyError as e:
            if self.commandLineArguments.force_fix and self.commandLineArguments.fix:
                print(e.message)
                print("")
                print("INFO:  The --force_fix option was enabled.")
                print("       Proceeding to analyze and apply fixes.")
                print("")
            else:
                raise e

        post_token_assignments(self.lAllObjects)
        #        self.lAllObjects = combine_use_clause_selected_name(self.lAllObjects)

        set_token_hierarchy_value(self.lAllObjects)
        set_todo_tokens(self.lAllObjects)
        set_aggregate_tokens(self.lAllObjects)
        set_code_tags(self.lAllObjects)
        self.oTokenMap = process_tokens(self.lAllObjects)

    def update(self, lUpdates, bUpdateMap):
        if len(lUpdates) == 0:
            return
        for oUpdate in lUpdates[::-1]:
            iStart = oUpdate.oTokens.iStartIndex
            lTokens = oUpdate.get_tokens()
            iEnd = oUpdate.oTokens.iEndIndex
            lMyTokens = remove_beginning_of_file_tokens(lTokens)
            self.lAllObjects[iStart:iEnd] = lMyTokens
        if bUpdateMap:
            self.oTokenMap = process_tokens(self.lAllObjects)

    def get_token_map(self):
        return self.oTokenMap

    def update_token_map(self):
        self.oTokenMap = process_tokens(self.lAllObjects)

    def set_indent_map(self, dIndentMap):
        self.dIndentMap = dIndentMap
        set_token_indent(self.dIndentMap, self.lAllObjects)

    def get_indent_map(self):
        return self.dIndentMap

    def get_object_lines(self):
        lReturn = []
        lReturn.append("")
        for lLine in split_on_carriage_return(self.lAllObjects):
            lReturn.append(lLine)
        return lReturn

    def get_lines(self):
        lReturn = []
        lReturn.append("")
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

    def get_line_preceding_line(self, iLine, iNumLines=1):
        return extract.get_line_preceding_line(iLine, self.lAllObjects, iNumLines, self.oTokenMap)

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

    def get_tokens_bounded_by(
        self,
        oLeft,
        oRight,
        include_trailing_whitespace=False,
        bExcludeLastToken=False,
        bIncludeTillEndOfLine=False,
        bIncludeTillBeginningOfLine=False,
    ):
        return extract.get_tokens_bounded_by(
            oLeft,
            oRight,
            self.lAllObjects,
            self.oTokenMap,
            include_trailing_whitespace=include_trailing_whitespace,
            bExcludeLastToken=bExcludeLastToken,
            bIncludeTillEndOfLine=bIncludeTillEndOfLine,
            bIncludeTillBeginningOfLine=bIncludeTillBeginningOfLine,
        )

    def get_tokens_bounded_by_token_when_between_tokens(self, oLeft, oRight, oStart, oEnd, include_trailing_whitespace=False):
        return extract.get_tokens_bounded_by_token_when_between_tokens(
            oLeft,
            oRight,
            oStart,
            oEnd,
            self.lAllObjects,
            self.oTokenMap,
            include_trailing_whitespace,
        )

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
        return extract.get_tokens_between_tokens_inclusive_while_storing_value_from_token(
            left_token,
            right_token,
            value_token,
            self.lAllObjects,
            self.oTokenMap,
        )

    def get_tokens_between_non_whitespace_token_and_token(self, right_token):
        return extract.get_tokens_between_non_whitespace_token_and_token(right_token, self.lAllObjects, self.oTokenMap)

    def get_tokens_from_line(self, iLineNumber):
        return extract.get_tokens_from_line(iLineNumber, self.lAllObjects, self.oTokenMap)

    def get_consecutive_lines_starting_with_token(self, search_token, min_num_lines=2):
        return extract.get_consecutive_lines_starting_with_token(search_token, min_num_lines, self.lAllObjects, self.oTokenMap)

    def get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(self, search_token, stop_token):
        return extract.get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(
            search_token,
            stop_token,
            self.lAllObjects,
            self.oTokenMap,
        )

    def get_tokens_where_line_starts_with_token_until_ending_token_is_found(self, start_token, stop_token):
        return extract.get_tokens_where_line_starts_with_token_until_ending_token_is_found(start_token, stop_token, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_before_it(self, oToken, iTokens):
        return extract.get_token_and_n_tokens_before_it(oToken, iTokens, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_before_it_in_between_tokens(self, lTokens, iTokens, oStart, oEnd):
        return extract.get_token_and_n_tokens_before_it_in_between_tokens(lTokens, iTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_before_it_in_between_tokens_unless_token_is_found(self, lTokens, iTokens, oStart, oEnd, oStop):
        return extract.get_token_and_n_tokens_before_it_in_between_tokens_unless_token_is_found(
            lTokens,
            iTokens,
            oStart,
            oEnd,
            oStop,
            self.lAllObjects,
            self.oTokenMap,
        )

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

    def get_blank_lines_above_line_starting_with_use_clause(self, lTokens):
        return extract.get_blank_lines_above_line_starting_with_use_clause(lTokens, self.lAllObjects, self.oTokenMap)

    def get_blank_lines_above_line_starting_with_token_when_between_tokens(self, lTokens, lBetweenTokens):
        return extract.get_blank_lines_above_line_starting_with_token_when_between_tokens(lTokens, lBetweenTokens, self.lAllObjects, self.oTokenMap)

    def get_association_elements_between_tokens(self, oStart, oEnd):
        return extract.get_association_elements_between_tokens(oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_interface_elements_between_tokens(self, oStart, oEnd, include_end_of_line_comments=False):
        return extract.get_interface_elements_between_tokens(oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_lines_with_length_that_exceed_column(self, iColumn):
        return extract.get_lines_with_length_that_exceed_column(iColumn, self.lAllObjects, self.oTokenMap)

    def get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(
        self,
        lStartTokens,
        lEndTokens,
        bIncludeStartToken=False,
        bIncludeEndToken=True,
        bEarliestDetect=False,
    ):
        return extract.get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(
            lStartTokens,
            lEndTokens,
            self.lAllObjects,
            self.oTokenMap,
            bIncludeStartToken,
            bIncludeEndToken,
            bEarliestDetect,
        )

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

    def get_subprogram_body(self):
        return extract.get_subprogram_body(self.lAllObjects, self.oTokenMap)

    def get_function_subprogram_body(self):
        return extract.get_function_subprogram_body(self.lAllObjects, self.oTokenMap)

    def get_procedure_subprogram_body(self):
        return extract.get_procedure_subprogram_body(self.lAllObjects, self.oTokenMap)

    def get_tokens_from_non_whitespace_token_until_tokens(self, lTokens):
        return extract.get_tokens_from_non_whitespace_token_until_tokens(lTokens, self.lAllObjects, self.oTokenMap)


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


def replace_token(iToken, lTokens, new_token, **kwargs):
    lTokens[iToken] = lTokens[iToken].convert_to(new_token)

    # Update  attributes of new token with values specified in kwargs
    for key, value in kwargs.items():
        setattr(lTokens[iToken], key, value)


def replace_token_if_adjacent_tokens_in_list(iToken, lTokens, token_list, token_in_list, token_not_in_list):
    """Replace token at ``lTokens[iToken]`` with token ``token_in_list`` if the previous and optionally the next token matches any of the tokens in ``token_list``,
    otherwise replace it with ``token_not_in_list``.

    If an element in ``token_list`` is a token type, a match is obtained if that token precede the target token.

    If an element in ``token_list`` is a tuple (prev_token, next_token), a match is obtained if both the
    previous and following tokens are of the types specified in the tuple.
    """
    for token in token_list:
        if isinstance(token, tuple):
            match = utils.are_previous_consecutive_token_types_ignoring_whitespace(
                [token[0]],
                iToken - 1,
                lTokens,
            ) and utils.are_next_consecutive_token_types_ignoring_whitespace([token[1]], iToken + 1, lTokens)
        else:
            match = utils.are_previous_consecutive_token_types_ignoring_whitespace([token], iToken - 1, lTokens)
        if match:
            replace_token(iToken, lTokens, token_in_list)
            return
    replace_token(iToken, lTokens, token_not_in_list)


def post_token_assignments(lTokens):
    oCodeTags = code_tags.New()
    iParenId = 0
    lParenId = []
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, resolution_indication.resolution_function_name) or isinstance(oToken, type_mark.name) or isinstance(oToken, todo.name):
            sLowerValue = oToken.get_lower_value()
            ### IEEE values
            # Would be nice if types included a tuple of all defined types to be used below.
            if sLowerValue in ("std_logic_vector", "std_ulogic_vector", "std_ulogic", "std_logic", "integer", "natural", "signed", "unsigned"):
                replace_token(iToken, lTokens, getattr(types, sLowerValue))

        elif isinstance(oToken, type_mark.attribute):
            sValue = oToken.get_value()
            if oToken.get_lower_value() in predefined_attribute.values:
                lTokens[iToken] = predefined_attribute.keyword(sValue)

        elif isinstance(oToken, parser.todo):
            sValue = oToken.get_value()
            sLowerValue = oToken.get_lower_value()
            if sValue == "&":
                replace_token(iToken, lTokens, adding_operator.concat())

            elif sValue == "+":
                replace_token_if_adjacent_tokens_in_list(
                    iToken,
                    lTokens,
                    (parser.open_parenthesis, parser.keyword, parser.assignment, parser.comma, choices.bar),
                    sign.plus(),
                    adding_operator.plus(),
                )

            elif sValue == "-":
                replace_token_if_adjacent_tokens_in_list(
                    iToken,
                    lTokens,
                    (parser.open_parenthesis, parser.keyword, parser.assignment, parser.comma, choices.bar),
                    sign.minus(),
                    adding_operator.minus(),
                )

            elif sValue == "(":
                iParenId += 1
                lParenId.append(iParenId)
                replace_token(iToken, lTokens, parser.open_parenthesis(), iId=iParenId)

            elif sValue == ")":
                replace_token(iToken, lTokens, parser.close_parenthesis(), iId=lParenId.pop())

            elif sValue == ",":
                replace_token(iToken, lTokens, parser.comma())

            elif sLowerValue == "to":
                replace_token(iToken, lTokens, direction.to(sValue))

            elif sLowerValue == "downto":
                replace_token(iToken, lTokens, direction.downto(sValue))

            elif sLowerValue == "and":
                replace_token_if_adjacent_tokens_in_list(
                    iToken,
                    lTokens,
                    (parser.open_parenthesis, parser.assignment, parser.comma, logical_operator.logical_operator, (parser.keyword, parser.open_parenthesis)),
                    unary_logical_operator.and_operator(sValue),
                    logical_operator.and_operator(sValue),
                )

            elif sLowerValue == "or":
                replace_token_if_adjacent_tokens_in_list(
                    iToken,
                    lTokens,
                    (parser.open_parenthesis, parser.assignment, parser.comma, logical_operator.logical_operator, (parser.keyword, parser.open_parenthesis)),
                    unary_logical_operator.or_operator(sValue),
                    logical_operator.or_operator(sValue),
                )

            elif sLowerValue == "nand":
                replace_token_if_adjacent_tokens_in_list(
                    iToken,
                    lTokens,
                    (parser.open_parenthesis, parser.assignment, parser.comma, logical_operator.logical_operator, (parser.keyword, parser.open_parenthesis)),
                    unary_logical_operator.nand_operator(sValue),
                    logical_operator.nand_operator(sValue),
                )

            elif sLowerValue == "nor":
                replace_token_if_adjacent_tokens_in_list(
                    iToken,
                    lTokens,
                    (parser.open_parenthesis, parser.assignment, parser.comma, logical_operator.logical_operator, (parser.keyword, parser.open_parenthesis)),
                    unary_logical_operator.nor_operator(sValue),
                    logical_operator.nor_operator(sValue),
                )

            elif sLowerValue == "xor":
                replace_token_if_adjacent_tokens_in_list(
                    iToken,
                    lTokens,
                    (parser.open_parenthesis, parser.assignment, parser.comma, logical_operator.logical_operator, (parser.keyword, parser.open_parenthesis)),
                    unary_logical_operator.xor_operator(sValue),
                    logical_operator.xor_operator(sValue),
                )

            elif sLowerValue == "xnor":
                replace_token_if_adjacent_tokens_in_list(
                    iToken,
                    lTokens,
                    (parser.open_parenthesis, parser.assignment, parser.comma, logical_operator.logical_operator, (parser.keyword, parser.open_parenthesis)),
                    unary_logical_operator.xnor_operator(sValue),
                    logical_operator.xnor_operator(sValue),
                )

            elif sLowerValue == "**":
                replace_token(iToken, lTokens, miscellaneous_operator.double_star(sValue))

            elif sLowerValue == "abs":
                replace_token(iToken, lTokens, miscellaneous_operator.abs_operator(sValue))

            elif sLowerValue == "not":
                replace_token(iToken, lTokens, miscellaneous_operator.not_operator(sValue))

            elif sLowerValue == "*":
                replace_token(iToken, lTokens, multiplying_operator.star(sValue))

            elif sLowerValue == "/":
                replace_token(iToken, lTokens, multiplying_operator.slash(sValue))

            elif sLowerValue == "mod":
                replace_token(iToken, lTokens, multiplying_operator.mod_operator(sValue))

            elif sLowerValue == "rem":
                replace_token(iToken, lTokens, multiplying_operator.rem_operator(sValue))

            elif sValue == "=":
                replace_token(iToken, lTokens, relational_operator.equal(sValue))

            elif sValue == "'":
                replace_token(iToken, lTokens, parser.tic(sValue))
                utils.classify_predefined_types(lTokens, iToken + 1)

            elif sLowerValue == "event":
                replace_token(iToken, lTokens, parser.event_keyword(sValue))

            ### IEEE values
            elif sLowerValue in ("rising_edge", "falling_edge"):
                replace_token(iToken, lTokens, getattr(function, sLowerValue))

            elif sLowerValue in ("std_logic_vector", "std_ulogic_vector", "std_ulogic"):
                replace_token(iToken, lTokens, getattr(types, sLowerValue))

            elif len(sValue) == 3 and sValue.startswith("'") and sValue.endswith("'"):
                replace_token(iToken, lTokens, parser.character_literal(sValue))
        else:
            sValue = oToken.get_value()
            if sValue == "+":
                replace_token_if_adjacent_tokens_in_list(
                    iToken,
                    lTokens,
                    (parser.open_parenthesis, exponent.e_keyword, parser.keyword),
                    sign.plus(),
                    adding_operator.plus(),
                )
            elif sValue == "-":
                replace_token_if_adjacent_tokens_in_list(
                    iToken,
                    lTokens,
                    (parser.open_parenthesis, exponent.e_keyword, parser.keyword),
                    sign.minus(),
                    adding_operator.minus(),
                )
            elif sValue == "*":
                replace_token(iToken, lTokens, multiplying_operator.star(sValue))
            elif sValue == "/":
                replace_token(iToken, lTokens, multiplying_operator.slash(sValue))
            elif sValue == "**":
                replace_token(iToken, lTokens, miscellaneous_operator.double_star(sValue))
            elif sValue == "(":
                iParenId += 1
                lParenId.append(iParenId)
                oToken.iId = iParenId
            elif sValue == ")":
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
        #        if isinstance(oToken, parser.open_parenthesis):
        if type(oToken) == parser.open_parenthesis:
            lOpenParens.append(iToken)
        #        if isinstance(oToken, parser.close_parenthesis):
        if type(oToken) == parser.close_parenthesis:
            iIndex = lOpenParens.pop()
            if isinstance(lTokens[iIndex], token.aggregate.open_parenthesis):
                replace_token(iToken, lTokens, token.aggregate.close_parenthesis(), iId=oToken.iId)
        #        if isinstance(oToken, token.element_association.assignment):
        if len(lOpenParens) > 0 and (isinstance(oToken, token.element_association.assignment) or type(oToken) == parser.comma):
            replace_token(lOpenParens[-1], lTokens, token.aggregate.open_parenthesis(), iId=lTokens[lOpenParens[-1]].iId)


def set_todo_tokens(lTokens):
    lOpenParens = []
    for iToken, oToken in enumerate(lTokens):
        check_for_name(oToken, iToken, lTokens)
        check_for_open_parenthesis(oToken, iToken, lTokens, lOpenParens)
        check_for_close_parenthesis(oToken, iToken, lTokens, lOpenParens)


def check_for_name(oToken, iToken, lTokens):
    if type(oToken) == parser.todo:
        if utils.are_next_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken + 1, lTokens):
            lTokens[iToken] = oToken.convert_to(todo.name)


def check_for_open_parenthesis(oToken, iToken, lTokens, lOpenParens):
    if type(oToken) == parser.open_parenthesis:
        if (
            utils.are_previous_consecutive_token_types_ignoring_whitespace([todo.name], iToken - 1, lTokens)
            or utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.type], iToken - 1, lTokens)
            or utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.function], iToken - 1, lTokens)
        ):
            lTokens[iToken] = oToken.convert_to(todo.open_parenthesis)
            lOpenParens.append(oToken)


def check_for_close_parenthesis(oToken, iToken, lTokens, lOpenParens):
    if type(oToken) == parser.close_parenthesis:
        try:
            if oToken.iId == lOpenParens[-1].iId:
                lOpenParens.pop()
                lTokens[iToken] = oToken.convert_to(todo.close_parenthesis)
        except IndexError:
            pass


# def combine_use_clause_selected_name(lTokens):
#    lReturn = []
#    for iToken, oToken in enumerate(lTokens):
#        if isinstance(oToken, token.use_clause.selected_name):
#            if isinstance(lReturn[-1], token.use_clause.selected_name):
#                lReturn[-1].value = lReturn[-1].value + oToken.value
#                continue
#        lReturn.append(oToken)
#    return lReturn


def remove_beginning_of_file_tokens(lTokens):
    lReturn = []
    for oToken in lTokens:
        if not isinstance(oToken, parser.beginning_of_file):
            lReturn.append(oToken)
    return lReturn


class options:
    def __init__(self):
        self.bInsideDelimitedComment = False

    def set_inside_delimited_comment(self):
        self.bInsideDelimitedComment = True

    def clear_inside_delimited_comment(self):
        self.bInsideDelimitedComment = False

    def inside_delimited_comment(self):
        return self.bInsideDelimitedComment
