# -*- coding: utf-8 -*-
from vsg import parser


def New(lAllObjects):
    return design_file(lAllObjects)


class design_file:
    def __init__(self, lAllObjects):
        self.lAllObjects = lAllObjects
        self.iCurrent = 0
        self.iSeek = 0

    def advance_to_next_token(self):
        for iIndex, oToken in enumerate(self.lAllObjects[self.iCurrent : :]):
            if type(oToken) == parser.item:
                self.iCurrent = self.iCurrent + iIndex
                return True
        return False

    def are_next_consecutive_tokens(self, lTokens):
        for sToken in lTokens:
            self.seek_to_next_token()
            if sToken is not None:
                if not self.seek_token_lower_value_is(sToken):
                    return False
        return True

    def current_token_lower_value_is(self, sString):
        return self.get_current_token_lower_value() == sString

    def does_string_exist_before_string(self, sFirst, sSecond):
        for oToken in self.lAllObjects[self.iCurrent : :]:
            if oToken.lower_value == sSecond:
                return False
            if oToken.lower_value == sFirst:
                return True

    def exists_in_next_n_tokens(self, sString, iNumTokens):
        for x in range(0, iNumTokens):
            self.seek_to_next_token()
            if self.seek_token_lower_value_is(sString):
                return True
        return False

    def get_current_index(self):
        return self.iCurrent

    def get_current_token_lower_value(self):
        return self.lAllObjects[self.iCurrent].lower_value

    def get_current_token_value(self):
        return self.lAllObjects[self.iCurrent].get_value()

    def get_next_token_value(self):
        return self.lAllObjects[self.iCurrent + 1].get_value()

    def get_seek_token_lower_value(self):
        return self.lAllObjects[self.iSeek].lower_value

    def increment_current_index(self):
        self.iCurrent += 1

    def is_next_token(self, sString):
        self.advance_to_next_token()
        return self.current_token_lower_value_is(sString)

    def is_next_token_one_of(self, lString):
        self.advance_to_next_token()
        return self.get_current_token_lower_value() in lString

    def remove_token_at_offset(self, iOffset):
        self.lAllObjects.pop(self.iCurrent + iOffset)

    def replace_current_token_with(self, token):
        self.lAllObjects[self.iCurrent] = token(self.get_current_token_value())
        self.increment_current_index()

    def replace_current_token_with_list_of_tokens(self, lTokens):
        self.lAllObjects.pop(self.get_current_index())
        self.lAllObjects[self.get_current_index() : self.get_current_index()] = lTokens

    def replace_next_token_required(self, sToken, token):
        if self.is_next_token(sToken):
            self.replace_current_token_with(token)
        else:
            print_error_message(sToken, token, oDesignFile)

    def replace_next_token_with(self, token):
        self.advance_to_next_token()
        self.replace_current_token_with(token)

    def replace_next_token_with_if(self, sString, token):
        self.advance_to_next_token()
        if self.current_token_lower_value_is(sString):
            self.replace_current_token_with(token)

    def replace_next_token_with_if_not(self, sString, token):
        self.advance_to_next_token()
        if not self.current_token_lower_value_is(sString):
            self.replace_current_token_with(token)

    def seek_to_next_token(self):
        # jcl - might need to watch out for going past the end of the lAllObjects list
        if self.iSeek < self.iCurrent:
            self.iSeek = self.iCurrent
        for iIndex, oToken in enumerate(self.lAllObjects[self.iSeek : :]):
            if type(oToken) == parser.item:
                self.iSeek = self.iSeek + iIndex
                return True
        return False

    def seek_token_lower_value_is(self, sString):
        return self.get_seek_token_lower_value() == sString
