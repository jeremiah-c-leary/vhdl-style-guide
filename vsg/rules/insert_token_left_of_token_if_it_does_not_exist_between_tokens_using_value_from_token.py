# -*- coding: utf-8 -*-


from vsg import parser, violation
from vsg.rule_group import structure
from vsg.rules import utils as rules_utils
from vsg.rules.insert_token_next_to_token_if_it_does_not_exist_between_tokens_using_value_from_token import (
    insert_token_next_to_token_if_it_does_not_exist_between_tokens_using_value_from_token as Rule,
)
from vsg.vhdlFile import utils


class insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token(Rule):
    """
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

    value_token : token object
       token to pull the value from
    """

    def __init__(self, insert_token, anchor_token, left_token, right_token, value_token):
        Rule.__init__(self)
        self.insert_token = insert_token
        self.anchor_token = anchor_token
        self.left_token = left_token
        self.right_token = right_token
        self.value_token = value_token
        self.direction = "left"
