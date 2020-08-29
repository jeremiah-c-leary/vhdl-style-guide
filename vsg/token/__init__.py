

class Token():
    def __init__(self, sString):
        self.value = sString

    def get_value(self):
        return self.value

    def set_value(self, sString):
        self.value = sString

    def length(self):
        return len(self.value)


class CarriageReturn(Token):

    def __init__(self):
        Token.__init__(self, None)

class Comment(Token):

    def __init__(self):
        Token.__init__(self, None)

class Whitespace(Token):

    def __init__(self):
        Token.__init__(self, None)

class BlankLine(Token):

    def __init__(self):
        Token.__init__(self, None)

