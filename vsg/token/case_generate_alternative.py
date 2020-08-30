
from vsg import parser


class AlternativeLabelName(parser.label):

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class AlternativeLabelColon(parser.label_colon):

    def __init__(self):
        parser.label_colon.__init__(self)


class WhenKeyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class Choices(parser.choices):

    def __init__(self, sString):
        parser.choices.__init__(self, sString)


class Assignment(parser.assignment):

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)
