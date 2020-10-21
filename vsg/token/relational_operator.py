
from vsg import parser


class relational_operator(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class equal(relational_operator):

    def __init__(self, sString='='):
        relational_operator.__init__(self, '=')


class not_equal(relational_operator):

    def __init__(self, sString='/='):
        relational_operator.__init__(self, '/=')


class less_than(relational_operator):

    def __init__(self, sString='<'):
        relational_operator.__init__(self, '<')


class less_than_or_equal(relational_operator):

    def __init__(self, sString='<='):
        relational_operator.__init__(self, '<=')


class greater_than(relational_operator):

    def __init__(self, sString='>'):
        relational_operator.__init__(self, '>')


class greater_than_or_equal(relational_operator):

    def __init__(self, sString='>='):
        relational_operator.__init__(self, '>=')


class question_equal(relational_operator):

    def __init__(self, sString='?='):
        relational_operator.__init__(self, '?=')


class question_not_equal(relational_operator):

    def __init__(self, sString='?/='):
        relational_operator.__init__(self, '?/=')


class question_less_than(relational_operator):

    def __init__(self, sString='?<'):
        relational_operator.__init__(self, '?<')


class question_less_than_or_equal(relational_operator):

    def __init__(self, sString='?<='):
        relational_operator.__init__(self, '?<=')


class question_greater_than(relational_operator):

    def __init__(self, sString='?>'):
        relational_operator.__init__(self, '?>')


class question_greater_than_or_equal(relational_operator):

    def __init__(self, sString='?>='):
        relational_operator.__init__(self, '?>=')

