
from vsg import parser
from vsg import rule
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils

oInsertTokens = token.for_generate_statement.end_generate_label
oAnchorTokens = token.for_generate_statement.semicolon
oLeftTokens = token.for_generate_statement.end_keyword
oRightTokens = token.for_generate_statement.semicolon
oValueTokens = token.for_generate_statement.generate_label


class rule_011(rule.Rule):
    '''
    Checks for the existence of a token and will insert it if it does not exist.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    insert_token : token object
       token to insert if it does not exist.

    anchor_token : token object
       token to check if insert_token exists to the right of

       token to pull the value from
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'generate', '011')
        self.solution = 'Add generate label'
        self.phase = 1
        self.insert_token = oInsertTokens
        self.anchor_token = oAnchorTokens
        self.left_token = oLeftTokens
        self.right_token = oRightTokens
        self.value_token = oValueTokens

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(token.architecture_body.begin_keyword, token.architecture_body.end_keyword)

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            lLabels = []
            for iToken, oToken in enumerate(lTokens):
               iLine = utils.increment_line_number(iLine, oToken)

               if manage_labels(oToken, lLabels):
                   continue

               if isinstance(oToken, token.for_generate_statement.end_generate_keyword):
                   if not utils.are_next_consecutive_token_types_ignoring_whitespace([token.for_generate_statement.end_generate_label], iToken + 1, lTokens):
                       oNewToi = oToi.extract_tokens(iToken, iToken)
                       dAction = {}
                       dAction['label'] = token.for_generate_statement.end_generate_label(lLabels[-1].get_value())
                       sSolution = 'Add label ' + lLabels[-1].get_value()
                       oViolation = violation.New(oNewToi.get_line_number(), oNewToi, sSolution)
                       oViolation.set_action(dAction)
                       self.add_violation(oViolation)
                   continue

               if isinstance(oToken, token.if_generate_statement.end_generate_keyword):
                   if not utils.are_next_consecutive_token_types_ignoring_whitespace([token.if_generate_statement.end_generate_label], iToken + 1, lTokens):
                       oNewToi = oToi.extract_tokens(iToken, iToken)
                       dAction = {}
                       dAction['label'] = token.if_generate_statement.end_generate_label(lLabels[-1].get_value())
                       sSolution = 'Add label ' + lLabels[-1].get_value()
                       oViolation = violation.New(oNewToi.get_line_number(), oNewToi, sSolution)
                       oViolation.set_action(dAction)
                       self.add_violation(oViolation)
                   continue

               if isinstance(oToken, token.case_generate_statement.end_generate_keyword):
                   if not utils.are_next_consecutive_token_types_ignoring_whitespace([token.case_generate_statement.end_generate_label], iToken + 1, lTokens):
                       oNewToi = oToi.extract_tokens(iToken, iToken)
                       dAction = {}
                       dAction['label'] = token.case_generate_statement.end_generate_label(lLabels[-1].get_value())
                       sSolution = 'Add label ' + lLabels[-1].get_value()
                       oViolation = violation.New(oNewToi.get_line_number(), oNewToi, sSolution)
                       oViolation.set_action(dAction)
                       self.add_violation(oViolation)
                   continue

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lTokens.append(parser.whitespace(' '))
        lTokens.append(dAction['label'])
        oViolation.set_tokens(lTokens)


def manage_labels(oToken, lLabels):

    if isinstance(oToken, token.for_generate_statement.generate_label):
        lLabels.append(oToken)
        return True

    if isinstance(oToken, token.if_generate_statement.generate_label):
        lLabels.append(oToken)
        return True

    if isinstance(oToken, token.case_generate_statement.generate_label):
        lLabels.append(oToken)
        return True

    if isinstance(oToken, token.for_generate_statement.semicolon):
        lLabels.pop()
        return True

    if isinstance(oToken, token.if_generate_statement.semicolon):
        lLabels.pop()
        return True

    if isinstance(oToken, token.case_generate_statement.semicolon):
        lLabels.pop()
        return True

    return False
