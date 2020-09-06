
from vsg import parser


class access_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


 # jcl - remove the objects below when new parser is done
class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class subtype_indication(parser.subtype_indication):

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)
