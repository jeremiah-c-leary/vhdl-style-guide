
from vsg import parser


class LabelName(parser.label):

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class LabelColon(parser.label_colon):

    def __init__(self):
        parser.label_colon.__init__(self)


class CaseKeyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class Expression(parser.expression):

    def __init__(self, sString):
        parser.expression.__init__(self, sString)


class GenerateKeyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class EndKeyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class EndGenerateKeyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class EndGenerateLabel(parser.label):

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class Semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)
