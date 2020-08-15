
from vsg import parser


class assert_label(label):

    def __init__(self, sString):
        label.__init__(self, sString)


class assert_label_colon(label_colon):

    def __init__(self):
        label_colon.__init__(self)


class assert_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)
