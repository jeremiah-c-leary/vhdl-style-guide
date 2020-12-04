
from vsg import parser
from vsg import token

from vsg import tokens

from vsg.token import adding_operator
from vsg.token import direction
from vsg.token import logical_operator
from vsg.token import miscellaneous_operator
from vsg.token import multiplying_operator
from vsg.token import relational_operator
from vsg.token import sign
from vsg.token.ieee.std_logic_1164 import types
from vsg.token.ieee.std_logic_1164 import function

from vsg.vhdlFile import extract
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import blank
from vsg.vhdlFile.classify import comment
from vsg.vhdlFile.classify import design_file
from vsg.vhdlFile.classify import whitespace

from vsg.vhdlFile.indent.set_token_indent import set_token_indent

from vsg.token_map import process_tokens


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
    def __init__(self, filecontent):
        self.filecontent = filecontent
        self.hasArchitecture = False
        self.hasEntity = False
        self.lAllObjects = []
        self._processFile()
        self.filename = None

    def _processFile(self):

        self.lAllObjects = []

        for sLine in self.filecontent:
            lTokens = tokens.create(sLine.replace('\t', '  ').rstrip())
            lObjects = []
            for sToken in lTokens:
                lObjects.append(parser.item(sToken))

            blank.classify(lObjects)
            whitespace.classify(lTokens, lObjects)
            comment.classify(lTokens, lObjects)

            self.lAllObjects.extend(lObjects)
            self.lAllObjects.append(parser.carriage_return())

        design_file.tokenize(self.lAllObjects)
        post_token_assignments(self.lAllObjects)

        self.set_token_indent()
        set_token_hierarchy_value(self.lAllObjects)
        self.oTokenMap = process_tokens(self.lAllObjects)
#        lIndex = self.oTokenMap.get_token_indexes(token.library_clause.keyword)
#        print(lIndex)
#        for iIndex in lIndex:
#            print(self.oTokenMap.get_line_number_of_index(iIndex))
#        exit()

    def update(self, lUpdates):
        if len(lUpdates) == 0:
            return
        bUpdateMap = True
        for oUpdate in lUpdates[::-1]:
            iStart = oUpdate.oTokens.iStartIndex
            lTokens = oUpdate.get_tokens()
            iEnd = oUpdate.oTokens.iEndIndex
            iDelta = iEnd - iStart
            if iDelta != len(lTokens):
                bUpdateMap = True
            elif oUpdate.get_remap():
                bUpdateMap = True
            self.lAllObjects[iStart:iEnd] = lTokens
        if bUpdateMap:
            self.oTokenMap = process_tokens(self.lAllObjects)

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

    def fix_blank_lines(self):
        self.lAllObjects = utils.fix_blank_lines(self.lAllObjects)

    def set_token_indent(self):
        set_token_indent(self.lAllObjects)

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

    def get_n_token_after_tokens(self, iToken, lTokens):
        return extract.get_n_token_after_tokens(iToken, lTokens, self.lAllObjects, self.oTokenMap)

    def get_n_tokens_after_token(self, iN, lTokens):
        return extract.get_m_tokens_before_and_n_tokens_after_token(0, iN, lTokens, self.lAllObjects, self.oTokenMap)

    def get_m_tokens_before_and_n_tokens_after_token(self, iM, iN, lTokens):
        return extract.get_m_tokens_before_and_n_tokens_after_token(iM, iN, lTokens, self.lAllObjects, self.oTokenMap)

    def get_n_token_after_tokens_between_tokens(self, iToken, lTokens, oStart, oEnd):
        return extract.get_n_token_after_tokens_between_tokens(iToken, lTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_tokens_matching_in_range_bounded_by_tokens(self, lTokens, oStart, oEnd):
        return extract.get_tokens_matching_in_range_bounded_by_tokens(lTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_tokens_bounded_by(self, oLeft, oRight, include_trailing_whitespace=False, bExcludeLastToken=False, bIncludeTillEndOfLine=False):
        return extract.get_tokens_bounded_by(oLeft, oRight, self.lAllObjects, self.oTokenMap, include_trailing_whitespace=include_trailing_whitespace, bExcludeLastToken=bExcludeLastToken, bIncludeTillEndOfLine=bIncludeTillEndOfLine)

    def get_tokens_bounded_by_token_when_between_tokens(self, oLeft, oRight, oStart, oEnd, include_trailing_whitespace=False):
        return extract.get_tokens_bounded_by_token_when_between_tokens(oLeft, oRight, oStart, oEnd, self.lAllObjects, self.oTokenMap, include_trailing_whitespace)

    def get_tokens_bounded_by_tokens_if_token_is_between_them(self, oLeft, oRight, oToken):
        return extract.get_tokens_bounded_by_tokens_if_token_is_between_them(oLeft, oRight, oToken, self.lAllObjects, self.oTokenMap)

    def get_tokens_at_beginning_of_line_matching(self, lTokens):
        return extract.get_tokens_at_beginning_of_line_matching(lTokens, self.lAllObjects, self.oTokenMap)

    def get_tokens_at_beginning_of_line_matching_between_tokens(self, lTokens, oStart, oEnd, bInclusive=False):
        return extract.get_tokens_at_beginning_of_line_matching_between_tokens(lTokens, oStart, oEnd, bInclusive, self.lAllObjects, self.oTokenMap)

    def get_column_of_token_index(self, iToken):
        return extract.get_column_of_token_index(iToken, self.lAllObjects, self.oTokenMap)

    def get_line_above_line_starting_with_token(self, lTokens):
        return extract.get_line_above_line_starting_with_token(lTokens, self.lAllObjects, self.oTokenMap)

    def get_line_above_line_starting_with_token_with_hierarchy(self, lTokens, lHierarchy):
        return extract.get_line_above_line_starting_with_token_with_hierarchy(lTokens, self.lAllObjects, lHierarchy, self.oTokenMap)

    def get_line_below_line_ending_with_token(self, lTokens):
        return extract.get_line_below_line_ending_with_token(lTokens, self.lAllObjects, self.oTokenMap)

    def get_line_below_line_ending_with_token_with_hierarchy(self, lTokens, lHierarchy):
        return extract.get_line_below_line_ending_with_token_with_hierarchy(lTokens, self.lAllObjects, lHierarchy, self.oTokenMap)

    def get_if_statement_conditions(self):
        return extract.get_if_statement_conditions(self.lAllObjects, self.oTokenMap)

    def get_n_tokens_before_and_after_tokens(self, iToken, lTokens):
        return extract.get_n_tokens_before_and_after_tokens(iToken, lTokens, self.lAllObjects, self.oTokenMap)

    def get_sequence_of_tokens_not_matching(self, lTokens):
        return extract.get_sequence_of_tokens_not_matching(lTokens, self.lAllObjects, self.oTokenMap)

    def get_tokens_between_tokens_inclusive_while_storing_value_from_token(self, left_token, right_token, value_token):
        return extract.get_tokens_between_tokens_inclusive_while_storing_value_from_token(left_token, right_token, value_token, self.lAllObjects, self.oTokenMap)

    def get_tokens_from_line(self, iLineNumber):
        return extract.get_tokens_from_line(iLineNumber, self.lAllObjects, self.oTokenMap)

    def get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(self, search_token, stop_token):
        return extract.get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(search_token, stop_token, self.lAllObjects, self.oTokenMap)

    def get_tokens_where_line_starts_with_token_until_ending_token_is_found(self, start_token, stop_token):
        return extract.get_tokens_where_line_starts_with_token_until_ending_token_is_found(start_token, stop_token, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_before_it(self, oToken, iTokens):
        return extract.get_token_and_n_tokens_before_it(oToken, iTokens, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_before_it_in_between_tokens(self, lTokens, iTokens, oStart, oEnd):
        return extract.get_token_and_n_tokens_before_it_in_between_tokens(lTokens, iTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_after_it(self, lTokens, iTokens):
        return extract.get_token_and_n_tokens_after_it(lTokens, iTokens, self.lAllObjects, self.oTokenMap)

    def get_token_and_n_tokens_after_it_when_between_tokens(self, lTokens, iTokens, oStart, oEnd):
        return extract.get_token_and_n_tokens_after_it_when_between_tokens(lTokens, iTokens, oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_blank_lines_below_line_ending_with_token(self, lTokens):
        return extract.get_blank_lines_below_line_ending_with_token(lTokens, self.lAllObjects, self.oTokenMap)

    def get_blank_lines_above_line_starting_with_token(self, lTokens):
        return extract.get_blank_lines_above_line_starting_with_token(lTokens, self.lAllObjects, self.oTokenMap)

    def get_association_elements_between_tokens(self, oStart, oEnd):
        return extract.get_association_elements_between_tokens(oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_interface_elements_between_tokens(self, oStart, oEnd, include_end_of_line_comments=False):
        return extract.get_interface_elements_between_tokens(oStart, oEnd, self.lAllObjects, self.oTokenMap)

    def get_lines_with_length_that_exceed_column(self, iColumn):
        return extract.get_lines_with_length_that_exceed_column(iColumn, self.lAllObjects, self.oTokenMap)

    def get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(self, lStartTokens, lEndTokens):
        return extract.get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(lStartTokens, lEndTokens, self.lAllObjects, self.oTokenMap)

    def get_tokens_between_indexes(self, iStartIndex, iEndIndex):
        return extract.get_tokens_between_indexes(iStartIndex, iEndIndex, self.lAllObjects)


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
    lCodeTags = []
    for iToken, oToken in enumerate(lTokens):
        oToken.set_code_tags(lCodeTags)
        if isinstance(oToken, parser.todo):
            sValue = oToken.get_value()
            if sValue == '&':
                lTokens[iToken] = adding_operator.concat()
                continue
            if sValue  == '+':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.keyword], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                else:
                    lTokens[iToken] = adding_operator.plus()
                continue
            if sValue  == '-':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.keyword], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.assignment], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                else:
                    lTokens[iToken] = adding_operator.minus()
                continue
            if sValue == '(':
                lTokens[iToken] = parser.open_parenthesis()
                continue
            if sValue == ')':
                lTokens[iToken] = parser.close_parenthesis()
                continue
            if sValue == ',':
                lTokens[iToken] = parser.comma()
                continue
            if sValue.lower() == 'to':
                lTokens[iToken] = token.direction.to(sValue)
                continue
            if sValue.lower() == 'downto':
                lTokens[iToken] = token.direction.downto(sValue)
                continue
            if sValue.lower() == 'and':
                lTokens[iToken] = token.logical_operator.and_operator(sValue)
                continue
            if sValue.lower() == 'or':
                lTokens[iToken] = token.logical_operator.or_operator(sValue)
                continue
            if sValue.lower() == 'nand':
                lTokens[iToken] = token.logical_operator.nand_operator(sValue)
                continue
            if sValue.lower() == 'nor':
                lTokens[iToken] = token.logical_operator.nor_operator(sValue)
                continue
            if sValue.lower() == 'xor':
                lTokens[iToken] = token.logical_operator.xor_operator(sValue)
                continue
            if sValue.lower() == 'xnor':
                lTokens[iToken] = token.logical_operator.xnor_operator(sValue)
                continue
            if sValue.lower() == '**':
                lTokens[iToken] = token.miscellaneous_operator.double_star(sValue)
                continue
            if sValue.lower() == 'abs':
                lTokens[iToken] = token.miscellaneous_operator.abs_operator(sValue)
                continue
            if sValue.lower() == 'not':
                lTokens[iToken] = token.miscellaneous_operator.not_operator(sValue)
                continue

            if sValue.lower() == '*':
                lTokens[iToken] = token.multiplying_operator.star(sValue)
                continue
            if sValue.lower() == '/':
                lTokens[iToken] = token.multiplying_operator.slash(sValue)
                continue
            if sValue.lower() == 'mod':
                lTokens[iToken] = token.multiplying_operator.mod_operator(sValue)
                continue
            if sValue.lower() == 'rem':
                lTokens[iToken] = token.multiplying_operator.rem_operator(sValue)
                continue

            if sValue == '=':
                lTokens[iToken] = token.relational_operator.equal(sValue)
                continue



            if sValue == "'":
                lTokens[iToken] = parser.tic(sValue)
                continue
            if sValue.lower() == 'event':
                lTokens[iToken] = parser.event_keyword(sValue)
                continue

            ### IEEE values
            if sValue.lower() == 'rising_edge':
                lTokens[iToken] = token.ieee.std_logic_1164.function.rising_edge(sValue)
                continue
            if sValue.lower() == 'falling_edge':
                lTokens[iToken] = token.ieee.std_logic_1164.function.falling_edge(sValue)
                continue

            if sValue.lower() == 'std_logic_vector':
                lTokens[iToken] = token.ieee.std_logic_1164.types.std_logic_vector(sValue)

            if sValue.lower() == 'std_ulogic_vector':
                lTokens[iToken] = token.ieee.std_logic_1164.types.std_ulogic_vector(sValue)

            if sValue.lower() == 'std_ulogic':
                lTokens[iToken] = token.ieee.std_logic_1164.types.std_ulogic(sValue)

            if len(sValue) == 3 and sValue.startswith("'") and sValue.endswith("'"):
                lTokens[iToken] = parser.character_literal(sValue)
                continue
        else:
            update_code_tags(oToken, lCodeTags)
            sValue = oToken.get_value()
            if sValue  == '+':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.keyword], iToken - 1, lTokens):
                    lTokens[iToken] = sign.plus()
                else:
                    lTokens[iToken] = adding_operator.plus()
                continue
            if sValue  == '-':
                if utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                elif utils.are_previous_consecutive_token_types_ignoring_whitespace([parser.keyword], iToken - 1, lTokens):
                    lTokens[iToken] = sign.minus()
                else:
                    lTokens[iToken] = adding_operator.minus()
                continue

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

def update_code_tags(oToken, lCodeTags):
    if isinstance(oToken, parser.comment):
        sValue = oToken.get_value()

        if sValue.startswith('-- vsg_on'):
          lValues = sValue.split()
          if len(lValues) == 2:
              lCodeTags.clear()
          else:
             for sCodeTag in lValues[2:]:
                 lCodeTags.remove(sCodeTag)
        elif sValue.startswith('-- vsg_off'):
          lValues = sValue.split()
          if len(lValues) == 2:
              lCodeTags.clear()
              lCodeTags.append('all')
          else:
             for sCodeTag in lValues[2:]:
                 try:
                     lCodeTags.append(sCodeTag)
                 except ValueError:
                     pass
