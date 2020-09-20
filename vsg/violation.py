

class New():

  def __init__(self, iLine, oTokens):
      self.iLine = iLine
      self.oTokens = oTokens

  def get_tokens(self):
      return self.oTokens.get_tokens()

  def get_line_number(self):
      return self.iLine

  def set_tokens(self, lTokens):
      self.oTokens.set_tokens(lTokens)
