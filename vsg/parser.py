
###############################################################################
# Base object
###############################################################################


class item():

    def __init__(self, sString):
        self.value = sString

    def get_value(self):
        return self.value

    def set_value(self, sString):
        self.value = sString

    def length(self):
        return len(self.value)

###############################################################################
# Base VHDL type classes
###############################################################################


class none(item):

    def __init__(self):
        item.__init__(self, None)


class keyword(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class identifier(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class comma(item):

    def __init__(self):
        item.__init__(self, ',')


class semicolon(item):

    def __init__(self):
        item.__init__(self, ';')


class whitespace(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class comment(item):

    def __init__(self, sString):
        item.__init__(self, sString)


###############################################################################
# Context objects
###############################################################################


class context_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class context_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)


class context_is_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class context_end_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class context_end_context_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class context_end_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)


class context_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)


###############################################################################
# Library objects
###############################################################################


class library_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class library_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)

class library_comma(comma):

    def __init__(self):
        comma.__init__(self)

class library_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)

###############################################################################
# Use objects
###############################################################################


class use_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class use_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)

class use_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)

