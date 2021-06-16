

from vsg import parser
from vsg import rule
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rules import utils as rule_utils


class align_tokens_in_region_between_tokens_unless_between_tokens(rule.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object list
       List of tokens to align

    left_token : token object
       The first token that defines the region

    right_token : token object
       The second token that defines the region

    lUnless : token object pairs list
       A list of pairs of tokens in which to exclude alignment
    '''

    def __init__(self, name, identifier, lTokens, left_token, right_token, lUnless):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 5
        self.lTokens = lTokens
        self.left_token = left_token
        self.right_token = right_token
        self.lUnless = lUnless
        ## attributes below are configurable by the user

        self.compact_alignment = True
        self.configuration.append('compact_alignment')

        self.blank_line_ends_group = True
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = True
        self.configuration.append('comment_line_ends_group')

        self.if_control_statements_ends_group = False
        self.configuration.append('if_control_statements_ends_group')
        self.case_control_statements_ends_group = False
        self.configuration.append('case_control_statements_ends_group')
        self.loop_control_statements_ends_group = False
        self.configuration.append('loop_control_statements_ends_group')

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.left_token, self.right_token)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            iColumn = 0
            bTokenFound = False
            iToken = -1
            bSkip = False
            oEndSkipToken = None
            dAnalysis = {}

            for iIndex in range(0, len(lTokens)):
               iToken += 1
               oToken = lTokens[iIndex]

               bSkip, oEndSkipToken = check_for_exclusions(oToken, bSkip, oEndSkipToken, self.lUnless)

               if not bTokenFound and not bSkip:
                   for oSearch in self.lTokens:
                       if isinstance(oToken, oSearch):
                           bTokenFound = True
                           dAnalysis[iLine] = {}
                           dAnalysis[iLine]['token_column'] = iColumn
                           dAnalysis[iLine]['token_index'] = iToken
                           dAnalysis[iLine]['line_number'] = iLine
                           dAnalysis[iLine]['token_value'] = oToken.get_value()
                           if isinstance(lTokens[iIndex -1], parser.whitespace):
                               dAnalysis[iLine]['left_column'] = iColumn - len(lTokens[iIndex - 1].get_value())
                           else:
                               dAnalysis[iLine]['left_column'] = iColumn
                           break

                   iColumn += len(oToken.get_value())

               if isinstance(oToken, parser.carriage_return):
                   iLine += 1
                   iColumn = 0
                   bTokenFound = False
                   iToken = -1
                   if self.comment_line_ends_group:
                       if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment], iIndex + 1, lTokens) or \
                          utils.are_next_consecutive_token_types([parser.comment], iIndex + 1, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}
                   if self.blank_line_ends_group:
                       if utils.are_next_consecutive_token_types([parser.blank_line], iIndex + 1, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}

                   if self.if_control_statements_ends_group:
                       if check_for_if_keywords(iIndex + 1, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}

                   if is_case_control_enabled(self.case_control_statements_ends_group):
                       if is_case_keyword(self.case_control_statements_ends_group, iIndex, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}

                   if self.loop_control_statements_ends_group:
                       if check_for_loop_keywords(iIndex + 1, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}



            add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)


            for iKey in list(dAnalysis.keys()):
                if dAnalysis[iKey]['adjust'] != 0:
                    oLineTokens = oFile.get_tokens_from_line(iKey)
                    sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                    oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                    oViolation.set_action(dAnalysis[iKey])
                    self.add_violation(oViolation)

            dAnalysis = {}

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        iTokenIndex = dAction['token_index']

        if isinstance(lTokens[iTokenIndex - 1], parser.whitespace):
            iLen = len(lTokens[iTokenIndex - 1].get_value())
            lTokens[iTokenIndex - 1].set_value(' '*(iLen + dAction['adjust']))
        else:
            rule_utils.insert_whitespace(lTokens, iTokenIndex, dAction['adjust'])
        oViolation.set_tokens(lTokens)


def add_adjustments_to_dAnalysis(dAnalysis, compact_alignment):
    iMaxLeftColumn = 0
    iMinLeftColumn = 9999999999999999
    iMaxTokenColumn = 0
    iMinTokenColumn = 9999999999999999

    for iKey in list(dAnalysis.keys()):
        iMaxLeftColumn = max(iMaxLeftColumn, dAnalysis[iKey]['left_column'])
        iMinLeftColumn = min(iMinLeftColumn, dAnalysis[iKey]['left_column'])
        iMaxTokenColumn = max(iMaxTokenColumn, dAnalysis[iKey]['token_column'])
        iMinTokenColumn = min(iMinTokenColumn, dAnalysis[iKey]['token_column'])

    if compact_alignment:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxLeftColumn - dAnalysis[iKey]['token_column'] + 1
    else:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxTokenColumn - dAnalysis[iKey]['token_column']


def check_for_exclusions(oToken, bSkip, oEndSkipToken, lUnless):
    if bSkip:
        if isinstance(oToken, oEndSkipToken):
            return False, None
    else:
        for lTokenPairs in lUnless:
            if isinstance(oToken, lTokenPairs[0]):
                return True, lTokenPairs[1]

    return bSkip, oEndSkipToken


def check_for_if_keywords(iToken, lTokens):
    iMyToken = iToken
    if isinstance(lTokens[iToken], parser.whitespace):
        iMyToken += 1

    if isinstance(lTokens[iMyToken], token.if_statement.if_label):
        return True

    if isinstance(lTokens[iMyToken], token.if_statement.if_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.if_statement.elsif_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.if_statement.else_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.if_statement.end_keyword):
        return True

    return False

def check_for_case_keywords(iToken, lTokens):
    iMyToken = iToken
    if isinstance(lTokens[iToken], parser.whitespace):
        iMyToken += 1

    if isinstance(lTokens[iMyToken], token.case_statement.case_label):
        return True

    if isinstance(lTokens[iMyToken], token.case_statement.case_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.case_statement.end_keyword):
        return True

    return False

def check_for_when_keywords(iToken, lTokens):
    iMyToken = iToken
    if isinstance(lTokens[iToken], parser.whitespace):
        iMyToken += 1

    if isinstance(lTokens[iMyToken], token.case_statement_alternative.when_keyword):
        return True

    return False

def check_for_loop_keywords(iToken, lTokens):
    iMyToken = iToken
    if isinstance(lTokens[iToken], parser.whitespace):
        iMyToken += 1

    if isinstance(lTokens[iMyToken], token.loop_statement.loop_label):
        return True

    if isinstance(lTokens[iMyToken], token.iteration_scheme.while_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.iteration_scheme.for_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.loop_statement.loop_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.loop_statement.end_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.loop_statement.end_loop_keyword):
        return True

    return False

def is_case_control_enabled(config):
    if config == 'break_on_case_or_end_case':
        return True
    return config

def is_case_keyword(config, iIndex, lTokens):
    if check_for_case_keywords(iIndex + 1, lTokens):
        return True
    if check_for_when_keywords(iIndex + 1, lTokens):
        if config != 'break_on_case_or_end_case':
           return True
    return False

