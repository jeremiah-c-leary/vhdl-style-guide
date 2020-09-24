

class New():

  def __init__(self, iLine, oTokens, sSolution=None):
      self.iLine = iLine
      self.oTokens = oTokens
      self.sSolution = sSolution
      self.action = None

  def get_tokens(self):
      return self.oTokens.get_tokens()

  def get_line_number(self):
      return self.iLine

  def set_tokens(self, lTokens):
      self.oTokens.set_tokens(lTokens)

  def set_solution(self, sSolution):
      self.solution = sSolution

  def get_solution(self):
      return self.sSolution

  def set_action(self, sAction):
      self.action = sAction

  def get_action(self):
      return self.action

  def get_token_value(self):
      return self.oTokens.get_token_value()
