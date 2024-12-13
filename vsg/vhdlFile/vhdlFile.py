# -*- coding: utf-8 -*-

from vsg import config, exceptions, parser, token, tokens
from vsg.token import (
    adding_operator,
    aggregate,
    attribute_name,
    choices,
    direction,
    exponent,
    logical_operator,
    miscellaneous_operator,
    multiplying_operator,
    predefined_attribute,
    relational_operator,
    resolution_indication,
    shift_operator,
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

dIeeeTypeStringMap = {
    "std_logic_vector": types.std_logic_vector,
    "std_ulogic_vector": types.std_ulogic_vector,
    "std_ulogic": types.std_ulogic,
    "std_logic": types.std_logic,
    "integer": types.integer,
    "natural": types.natural,
    "signed": types.signed,
    "unsigned": types.unsigned,
}

dParserTodoStringMap = {
    "&": adding_operator.concat,
    ",": parser.comma,
    "to": direction.to,
    "downto": direction.downto,
    "**": miscellaneous_operator.double_star,
    "abs": miscellaneous_operator.abs_operator,
    "not": miscellaneous_operator.not_operator,
    "*": multiplying_operator.star,
    "/": multiplying_operator.slash,
    "mod": multiplying_operator.mod_operator,
    "rem": multiplying_operator.rem_operator,
    "=": relational_operator.equal,
    "event": parser.event_keyword,
    "rising_edge": function.rising_edge,
    "falling_edge": function.falling_edge,
    "sll": shift_operator.sll,
    "srl": shift_operator.srl,
    "sla": shift_operator.sla,
    "sra": shift_operator.sra,
    "rol": shift_operator.rol,
    "ror": shift_operator.ror,
}

dUnaryOrBinaryAdditionOperatorStringMap = {
    "+": {"unary": sign.plus, "binary": adding_operator.plus},
    "-": {"unary": sign.minus, "binary": adding_operator.minus},
}

dUnaryOrBinaryLogicalOperatorStringMap = {
    "and": {"unary": unary_logical_operator.and_operator, "binary": logical_operator.and_operator},
    "or": {"unary": unary_logical_operator.or_operator, "binary": logical_operator.or_operator},
    "nand": {"unary": unary_logical_operator.nand_operator, "binary": logical_operator.nand_operator},
    "nor": {"unary": unary_logical_operator.nor_operator, "binary": logical_operator.nor_operator},
    "xor": {"unary": unary_logical_operator.xor_operator, "binary": logical_operator.xor_operator},
    "xnor": {"unary": unary_logical_operator.xnor_operator, "binary": logical_operator.xnor_operator},
}


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

    def get_n_token_after_tokens_between_tokens_unless_between_tokens(self, iToken, lTokens, oStart, oEnd, lUnless):
        return extract.get_n_token_after_tokens_between_tokens_unless_between_tokens(iToken, lTokens, oStart, oEnd, lUnless, self.lAllObjects, self.oTokenMap)

    def get_tokens_matching_in_range_bounded_by_tokens(self, lTokens, oStart, oEnd):
        return extract.get_tokens_matching_in_range_bounded_by_tokens(lTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_tokens_matching_in_range_bounded_by_tokens_unless_between_tokens(self, lTokens, oStart, oEnd, lUnless):
        return extract.get_tokens_matching_in_range_bounded_by_tokens_unless_between_tokens(lTokens, oStart, oEnd, lUnless, self.lAllObjects, self.oTokenMap)

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

    def get_tokens_at_beginning_of_line_matching_between_tokens_unless_between_tokens(self, lTokens, oStart, oEnd, lUnless, bInclusive=False):
        return extract.get_tokens_at_beginning_of_line_matching_between_tokens_unless_between_tokens(
            lTokens,
            oStart,
            oEnd,
            lUnless,
            bInclusive,
            self.lAllObjects,
            self.oTokenMap,
        )

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

    def get_token_and_n_tokens_before_it_in_between_tokens_unless_between_tokens(self, lTokens, iTokens, oStart, oEnd, lUnless):
        return extract.get_token_and_n_tokens_before_it_in_between_tokens_unless_between_tokens(
            lTokens,
            iTokens,
            oStart,
            oEnd,
            lUnless,
            self.lAllObjects,
            self.oTokenMap,
        )

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

    def get_token_and_n_tokens_after_it_when_between_tokens_unless_between_tokens(self, lTokens, iTokens, oStart, oEnd, lUnless):
        return extract.get_token_and_n_tokens_after_it_when_between_tokens_unless_between_tokens(
            lTokens,
            iTokens,
            oStart,
            oEnd,
            lUnless,
            self.lAllObjects,
            self.oTokenMap,
        )

    def get_blank_lines_below_line_ending_with_token(self, lTokens, lHierarchy=None):
        return extract.get_blank_lines_below_line_ending_with_token(lTokens, lHierarchy, self.lAllObjects, self.oTokenMap)

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


def post_token_assignments(lTokens):
    iParenId = 0
    lParenId = []
    for iToken, oToken in enumerate(lTokens):
        sValue = oToken.get_value()
        if isinstance(oToken, (resolution_indication.resolution_function_name, type_mark.name, attribute_name.name, todo.name)):
            sLowerValue = oToken.get_lower_value()
            ### IEEE values
            if sLowerValue in dIeeeTypeStringMap.keys():
                oTokenClass = dIeeeTypeStringMap[sLowerValue]
                lTokens[iToken] = oTokenClass(sValue)

        elif isinstance(oToken, attribute_name.attribute):
            if sValue.lower() in predefined_attribute.values:
                lTokens[iToken] = predefined_attribute.keyword(sValue)

        elif isinstance(oToken, parser.todo):
            sLowerValue = oToken.get_lower_value()
            if sLowerValue in dParserTodoStringMap.keys():
                oTokenClass = dParserTodoStringMap[sLowerValue]
                lTokens[iToken] = oTokenClass(sValue)

            elif sLowerValue in dUnaryOrBinaryAdditionOperatorStringMap.keys():
                dTokenTypes = dUnaryOrBinaryAdditionOperatorStringMap[sLowerValue]
                assign_token_of_addition_operator_that_can_be_either_unary_and_binary(iToken, lTokens, sValue, dTokenTypes)

            elif sLowerValue in dUnaryOrBinaryLogicalOperatorStringMap.keys():
                dTokenTypes = dUnaryOrBinaryLogicalOperatorStringMap[sLowerValue]
                assign_token_of_logical_operator_that_can_be_either_unary_and_binary(iToken, lTokens, sValue, dTokenTypes)

            elif sValue == "(":
                lTokens[iToken] = parser.open_parenthesis()
                iParenId += 1
                lParenId.append(iParenId)
                lTokens[iToken].iId = iParenId

            elif sValue == ")":
                lTokens[iToken] = parser.close_parenthesis()
                lTokens[iToken].iId = lParenId.pop()

            elif sValue == "'":
                lTokens[iToken] = parser.tic(sValue)
                utils.classify_predefined_types(lTokens, iToken + 1)

            elif len(sValue) == 3 and sValue.startswith("'") and sValue.endswith("'"):
                lTokens[iToken] = parser.character_literal(sValue)
        else:
            if sValue == "+":
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([exponent.e_keyword], iToken - 1, lTokens):
                    pass
                else:
                    lTokens[iToken] = adding_operator.plus()
            elif sValue == "-":
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([exponent.e_keyword], iToken - 1, lTokens):
                    pass
                else:
                    lTokens[iToken] = adding_operator.minus()
            elif sValue == "*":
                lTokens[iToken] = multiplying_operator.star(sValue)
            elif sValue == "/":
                lTokens[iToken] = multiplying_operator.slash(sValue)
            elif sValue == "**":
                lTokens[iToken] = miscellaneous_operator.double_star(sValue)
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
        if type(oToken) == parser.open_parenthesis:
            lOpenParens.append(iToken)
        if type(oToken) == parser.close_parenthesis:
            iIndex = lOpenParens.pop()
            if isinstance(lTokens[iIndex], token.aggregate.open_parenthesis):
                iId = oToken.iId
                lTokens[iToken] = token.aggregate.close_parenthesis()
                lTokens[iToken].iId = iId
        if len(lOpenParens) > 0 and (isinstance(oToken, token.element_association.assignment) or type(oToken) == parser.comma):
            iId = lTokens[lOpenParens[-1]].iId
            lTokens[lOpenParens[-1]] = token.aggregate.open_parenthesis()
            lTokens[lOpenParens[-1]].iId = iId


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


def remove_beginning_of_file_tokens(lTokens):
    lReturn = []
    for oToken in lTokens:
        if not isinstance(oToken, parser.beginning_of_file):
            lReturn.append(oToken)
    return lReturn


def assign_token_of_addition_operator_that_can_be_either_unary_and_binary(iToken, lTokens, sValue, dTokenTypes):
    if (
        utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens)
        or utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.keyword], iToken - 1, lTokens)
        or utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens)
        or utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.comma], iToken - 1, lTokens)
        or utils.are_previous_consecutive_token_types_ignoring_whitespace([choices.bar], iToken - 1, lTokens)
    ):
        lTokens[iToken] = dTokenTypes["unary"](sValue)
    else:
        lTokens[iToken] = dTokenTypes["binary"](sValue)


def assign_token_of_logical_operator_that_can_be_either_unary_and_binary(iToken, lTokens, sValue, dTokenTypes):
    if (
        utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens)
        or utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens)
        or utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.comma], iToken - 1, lTokens)
        or utils.are_previous_consecutive_token_types_ignoring_whitespace([logical_operator.logical_operator], iToken - 1, lTokens)
        or (
            utils.are_previous_consecutive_token_types_ignoring_whitespace(
                [parser.keyword],
                iToken - 1,
                lTokens,
            )
            and utils.are_next_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken + 1, lTokens)
        )
    ):
        lTokens[iToken] = dTokenTypes["unary"](sValue)
    else:
        lTokens[iToken] = dTokenTypes["binary"](sValue)


class options:
    def __init__(self):
        self.bInsideDelimitedComment = False

    def set_inside_delimited_comment(self):
        self.bInsideDelimitedComment = True

    def clear_inside_delimited_comment(self):
        self.bInsideDelimitedComment = False

    def inside_delimited_comment(self):
        return self.bInsideDelimitedComment
