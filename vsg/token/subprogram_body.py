from vsg import parser


class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class begin_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class designator(parser.designator):

    def __init__(self, sString):
        parser.designator.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
