
from vsg import parser


class miscellaneous_operator(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class double_star(miscellaneous_operator):

    def __init__(self, sString='**'):
        miscellaneous_operator.__init__(self, '**')


class abs_operator(miscellaneous_operator):

    def __init__(self, sString):
        miscellaneous_operator.__init__(self, sString)


class not_operator(miscellaneous_operator):

    def __init__(self, sString):
        miscellaneous_operator.__init__(self, sString)
