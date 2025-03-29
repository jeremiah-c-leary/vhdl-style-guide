# -*- coding: utf-8 -*-
from vsg import parser
from vsg.vhdlFile.classify import utils


def New(lAllObjects):
    return design_file(lAllObjects)


class design_file:
    def __init__(self, lAllObjects):
        self.lAllObjects = lAllObjects
        self.iEndIndex = len(lAllObjects) - 1
        self.sFilename = ""
        self.iCurrent = 0
        self.iSeek = 0

    def advance_seek_index_to_current_index(self):
        if self.iSeek < self.iCurrent:
            self.iSeek = self.iCurrent

    def advance_to_next_token(self):
        for iIndex, oToken in enumerate(self.lAllObjects[self.iCurrent : :]):
            if type(oToken) == parser.item:
                self.iCurrent = self.iCurrent + iIndex
                return True
        return False

    def advance_to_next_seek_token(self):
        for iIndex, oToken in enumerate(self.lAllObjects[self.iSeek : :]):
            if type(oToken) == parser.item:
                if self.iSeek > self.iEndIndex:
                    self.iSeek = self.iEndIndex
                else:
                    self.iSeek = self.iSeek + iIndex
                return True
        return False

    def align_seek_index(self):
        self.iSeek = self.iCurrent

    def are_next_consecutive_tokens(self, lTokens):
        self.align_seek_index()
        myIndex = self.iSeek
        for sToken in lTokens:
            self.seek_to_next_token()
            if sToken is not None:
                if not self.seek_token_lower_value_is(sToken):
                    self.iSeek = myIndex
                    return False
            self.increment_seek_index()
        return True

    def at_end_of_file(self):
        return self.iCurrent == self.iEndIndex

    def current_token_lower_value_is(self, sString):
        return self.get_current_token_lower_value() == sString

    def does_seek_token_match_regex(self, oRegex):
        if oRegex.fullmatch(self.get_seek_token_lower_value()) is not None:
            return True
        return False

    def does_string_exist_before_string(self, sFirst, sSecond):
        for oToken in self.lAllObjects[self.iCurrent : :]:
            if oToken.lower_value == sSecond:
                return False
            if oToken.lower_value == sFirst:
                return True

    def does_string_exist_before_matching_close_parenthesis(self, sString, myParen=0):
        iParen = myParen
        for oToken in self.lAllObjects[self.iSeek : :]:
            if iParen == 0 and oToken.lower_value == sString:
                return True
            if oToken.lower_value == "(":
                iParen += 1
            elif oToken.lower_value == ")":
                iParen -= 1
            if iParen == -1:
                return False
        return False

    def does_string_exist_before_string_honoring_parenthesis_hierarchy(self, sFirst, sSecond):
        iParen = 0
        for oToken in self.lAllObjects[self.iSeek : :]:
            if oToken.lower_value == sSecond:
                return False
            if oToken.lower_value == "(":
                iParen += 1
            elif oToken.lower_value == ")":
                iParen -= 1
            if iParen == 0 and oToken.lower_value == sFirst:
                return True
        return False

    def does_string_exist_before_seek_index_honoring_parenthesis_hierarchy(self, sString):
        iParen = 0
        for iIndex in range(self.get_current_index(), self.get_seek_index()):
            if self.lAllObjects[iIndex].lower_value == "(":
                iParen += 1
            elif self.lAllObjects[iIndex].lower_value == ")":
                iParen -= 1
            if iParen == 0 and self.lAllObjects[iIndex].lower_value == sString:
                return True
        return False

    def does_string_exist_in_next_n_tokens(self, sString, iNumTokens):
        self.iSeek = self.iCurrent
        for x in range(0, iNumTokens):
            self.seek_to_next_token()
            if self.seek_token_lower_value_is(sString):
                return True
            self.increment_seek_index()
        return False

    def get_current_index(self):
        return self.iCurrent

    def get_current_token_lower_value(self):
        return self.lAllObjects[self.iCurrent].lower_value

    def get_current_token_value(self):
        return self.lAllObjects[self.iCurrent].get_value()

    def get_next_token_value(self):
        return self.lAllObjects[self.iCurrent + 1].get_value()

    def get_seek_index(self):
        return self.iSeek

    def get_seek_token_lower_value(self):
        return self.lAllObjects[self.iSeek].lower_value

    def increment_current_index(self):
        self.iCurrent += 1

    def increment_seek_index(self):
        if self.iSeek < self.iEndIndex:
            self.iSeek += 1
        else:
            self.iSeek = self.iEndIndex

    def is_next_seek_token(self, sString):
        self.advance_to_next_seek_token()
        return self.seek_token_lower_value_is(sString)

    def is_next_seek_token_one_of(self, lString):
        self.advance_to_next_seek_token()
        return self.get_seek_token_lower_value() in lString

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
            utils.print_error_message(sToken, token, self)

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

    def replace_tokens_from_current_to_seek_with(self, token):
        while self.get_current_index() < self.get_seek_index():
            self.replace_next_token_with(token)
            self.advance_to_next_token()

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

    def advance_seek_over_parenthesis(self):
        if not self.seek_token_lower_value_is("("):
            return False

        iParen = 0
        for iToken, oToken in enumerate(self.lAllObjects[self.iSeek : :]):
            if oToken.lower_value == "(":
                iParen += 1
            elif oToken.lower_value == ")":
                iParen -= 1
            if iParen == 0:
                self.iSeek += iToken
                return True
        return False

    def debug_print(self, iNumTokens):
        sOutput = ""
        for oToken in self.lAllObjects[self.iCurrent : self.iCurrent + iNumTokens]:
            sOutput += oToken.get_value()
        print(f">>Current[{sOutput}]<<")

    def debug_seek_print(self, iNumTokens):
        sOutput = ""
        for oToken in self.lAllObjects[self.iSeek : self.iSeek + iNumTokens]:
            sOutput += oToken.get_value()
        print(f">>Seek[{sOutput}]<<")
