
from vsg import parser


class file_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class of_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

# jcl - need to delete the object below when old parsing method can be retired.


class type_mark(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
