

class New():

  def __init__(self, iLine, oTokens, sSolution=None):
      self.iLine = iLine
      self.oTokens = oTokens
      self.sSolution = sSolution
      self.action = None
      self.remap = False
      self.fix_blank_lines = False

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

  def has_code_tag(self, sCodeTag):
      try:
          for oToken in self.oTokens.get_tokens():
              if oToken.has_code_tag(sCodeTag):
                  return True
          return False
#          return self.oTokens.get_tokens()[0].has_code_tag(sCodeTag)
      except IndexError:
          return False
      except AttributeError:
          return False

  def set_remap(self):
      self.remap = True

  def get_remap(self):
      return self.remap

  def fix_blanks(self):
      return self.fix_blank_lines

  def get_start_index(self):
      return self.oTokens.get_start_index()
