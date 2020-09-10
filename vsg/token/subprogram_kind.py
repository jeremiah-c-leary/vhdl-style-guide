from vsg import parser


class procedure_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class function_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
