
from vsg import parser


class multiplying_operator(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class star(multiplying_operator):

    def __init__(self, sString='*'):
        multiplying_operator.__init__(self, '*')


class slash(multiplying_operator):

    def __init__(self, sString='/'):
        multiplying_operator.__init__(self, '/')


class mod_operator(multiplying_operator):

    def __init__(self, sString):
        multiplying_operator.__init__(self, sString)


class rem_operator(multiplying_operator):

    def __init__(self, sString):
        multiplying_operator.__init__(self, sString)
