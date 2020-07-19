
class item():

    def __init__(self, sString):
        self.value = sString

    def get_value(self):
        return self.value

    def set_value(self, sString):
        self.value = sString

    def length(self):
        return len(self.value)


class whitespace(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class comment(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class context(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class context_keyword(context):

    def __init__(self, sString):
        context.__init__(self, sString)

class context_identifier(context):

    def __init__(self, sString):
        context.__init__(self, sString)

class context_is_keyword(context):

    def __init__(self, sString):
        context.__init__(self, sString)

class context_end_keyword(context):

    def __init__(self, sString):
        context.__init__(self, sString)

class context_end_context_keyword(context):

    def __init__(self, sString):
        context.__init__(self, sString)

class context_end_identifier(context):

    def __init__(self, sString):
        context.__init__(self, sString)

class context_colon(context):

    def __init__(self, sString):
        context.__init__(self, sString)
