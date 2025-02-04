# -*- coding: utf-8 -*-
from vsg import parser


def New(lAllObjects):
    return design_file(lAllObjects)


class design_file:

    def __init__(self, lAllObjects):
        self.lAllObjects = lAllObjects
        self.iCurrent = 0

    def advance_to_next_token(self):
        for iIndex, oToken in enumerate(self.lAllObjects[self.iCurrent::]):
            if type(oToken) == parser.item:
                self.iCurrent = self.iCurrent + iIndex
                return True
        return False

    def assign_next_token_required(self, sToken, token):
        if self.is_next_token(sToken):
            self.replace_current_token_with(token)
        else:
            print_error_message(sToken, token, oDesignFile)

    def current_token_lower_value_is(self, sString):
        return self.get_current_token_lower_value() == sString

    def get_current_index(self):
        return self.iCurrent

    def get_current_token_lower_value(self):
        return self.lAllObjects[self.iCurrent].lower_value

    def get_current_token_value(self):
        return self.lAllObjects[self.iCurrent].get_value()

    def increment_current_index(self):
        self.iCurrent += 1

    def is_next_token(self, sString):
        self.advance_to_next_token()
        return self.current_token_lower_value_is(sString)

    def is_next_token_one_of(self, lString):
        self.advance_to_next_token()
        return self.get_current_token_lower_value() in lString

    def replace_current_token_with(self, token):
        self.lAllObjects[self.iCurrent] = token(self.get_current_token_value())
        self.increment_current_index()

    def replace_next_token_with(self, token):
        self.advance_to_next_token()
        self.replace_current_token_with(token)

    def replace_next_token_with_if(self, sString, token):
        self.advance_to_next_token()
        if self.current_token_lower_value_is(sString):
            self.replace_current_token_with(token)
