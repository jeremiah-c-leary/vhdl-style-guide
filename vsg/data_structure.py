
from vsg import parser


def New(lAllObjects):
    return design_file(lAllObjects)


class design_file:

    def __init__(self, lAllObjects):
        self.lAllObjects = lAllObjects
        self.iCurrent = 0

    def advance_to_next_token(self):
        iTemp = self.iCurrent
        for iTemp, oToken in enumerate(self.lAllObjects[self.iCurrent::]):
            if type(oToken) == parser.item:
                self.iCurrent = self.iCurrent + iTemp
                return True
        return False

    def current_token_lower_value_is(self, sString):
        if self.get_current_token_lower_value() == sString:
            return True
        return False

    def get_current_index(self):
        return self.iCurrent

    def get_current_token_lower_value(self):
        return self.lAllObjects[self.iCurrent].lower_value

    def is_next_token(self, sString):
        self.advance_to_next_token()
        if self.lAllObjects[self.iCurrent].get_lower_value() == sString:
            return True
        return False

    def is_next_token_one_of(self, lString):
        self.advance_to_next_token()
        if self.lAllObjects[self.iCurrent].lower_value in lString:
            return True
        return False

    def replace_current_token_with(self, token):
        self.lAllObjects[self.iCurrent] = token(self.lAllObjects[self.iCurrent].get_value())
        self.iCurrent += 1

    def replace_next_token_with(self, token):
        self.advance_to_next_token()
        self.replace_current_token_with(token)

    def replace_next_token_with_if(self, sString, token):
        self.advance_to_next_token()
        if self.current_token_lower_value_is(sString):
            self.replace_current_token_with(token)
