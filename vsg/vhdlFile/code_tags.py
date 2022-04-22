
from vsg import parser


class New():

    def __init__(self):
        self.code_tags = []
        self.next_line_code_tags = []
        self.bIgnoreNextCarriageReturn = False

    def clear(self):
        self.code_tags.clear()
        self.next_line_code_tags.clear()

    def clear_next_line_code_tags(self):
        self.next_line_code_tags.clear()

    def remove(self, sCodeTag):
        self.code_tags.remove(sCodeTag)

    def add(self, sCodeTag):
        if sCodeTag not in self.code_tags:
            self.code_tags.append(sCodeTag)

    def get_tags(self):
        lReturn = []
        lReturn.extend(self.code_tags)
        lReturn.extend(self.next_line_code_tags)
        return lReturn

    def update(self, oToken):

        if isinstance(oToken, parser.carriage_return):
            if self.bIgnoreNextCarriageReturn:
                self.bIgnoreNextCarriageReturn = False
            else:
                self.next_line_code_tags.clear()
            return None

        if on_code_tag_detected(oToken):
            remove_code_tags(self, oToken)
            return False
        elif off_code_tag_detected(oToken):
            add_code_tags(self, oToken)
            return True
        elif next_line_code_tag_detected(oToken):
            add_next_line_code_tags(self, oToken)
            self.bIgnoreNextCarriageReturn = True


def on_code_tag_detected(oToken):
    if not isinstance(oToken, parser.comment):
        return False
    if token_starts_with(oToken, '-- vsg_on'):
        return True
    return False


def off_code_tag_detected(oToken):
    if not isinstance(oToken, parser.comment):
        return False
    if token_starts_with(oToken, '-- vsg_off'):
        return True
    return False


def next_line_code_tag_detected(oToken):
    if not isinstance(oToken, parser.comment):
        return False
    if token_starts_with(oToken, '-- vsg_disable_next_line'):
        return True
    return False


def token_starts_with(oToken, sString):
    if oToken.get_value().startswith(sString):
        return True
    return False


def remove_code_tags(self, oToken):
    sValue = remove_code_tag_comment(oToken)
    lValues = sValue.split()
    if bare_code_tag(lValues):
        self.clear()
    else:
       for sCodeTag in lValues[2:]:
           self.remove(sCodeTag)


def add_code_tags(self, oToken):
    sValue = remove_code_tag_comment(oToken)
    lValues = sValue.split()
    if bare_code_tag(lValues):
        self.clear()
        self.add('all')
    else:
       for sCodeTag in lValues[2:]:
           self.add(sCodeTag)


def remove_code_tag_comment(oToken):
    lString = oToken.get_value().split(':')
    return lString[0]


def add_next_line_code_tags(self, oToken):
    sValue = remove_code_tag_comment(oToken)
    lValues = sValue.split()
    for sCodeTag in lValues[2:]:
       if sCodeTag not in self.next_line_code_tags:
           self.next_line_code_tags.append(sCodeTag)


def bare_code_tag(lValues):
    if len(lValues) == 2:
        return True
    return False


def token_has_vsg_on_code_tag(oToken):
    return on_code_tag_detected(oToken)


def token_has_vsg_off_code_tag(oToken):
    return off_code_tag_detected(oToken)


def token_has_next_line_code_tag(oToken):
    return next_line_code_tag_detected(oToken)
