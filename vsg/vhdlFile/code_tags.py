
from vsg import parser


class New():

  def __init__(self):
      self.code_tags = []
      self.next_line_code_tags = []
      self.bIgnoreNextCarriageReturn = False
      self.iLine = 0

  def clear(self):
      self.code_tags.clear()
      self.next_line_code_tags.clear()

  def remove(self, sCodeTag):
      self.code_tags.remove(sCodeTag)

  def add(self, sCodeTag):
      if sCodeTag not in self.code_tags:
          self.code_tags.append(sCodeTag)

  def get_tags(self):
      lReturn = []
      lReturn.extend(self.code_tags)
      lReturn.extend(self.next_line_code_tags)
      return lReturn

  def update(self, oToken):
      if isinstance(oToken, parser.comment):
          sValue = oToken.get_value()

          if sValue.startswith('-- vsg_on'):
              lValues = sValue.split()
              if len(lValues) == 2:
                  self.clear()
              else:
                 for sCodeTag in lValues[2:]:
                     self.remove(sCodeTag)
          elif sValue.startswith('-- vsg_off'):
              lValues = sValue.split()
              if len(lValues) == 2:
                  self.clear()
                  self.add('all')
              else:
                 for sCodeTag in lValues[2:]:
                     self.add(sCodeTag)
          elif sValue.startswith('-- vsg_disable_next_line'):
              lValues = sValue.split()
              for sCodeTag in lValues[2:]:
                 if sCodeTag not in self.next_line_code_tags:
                     self.next_line_code_tags.append(sCodeTag)
              self.bIgnoreNextCarriageReturn = True
      elif isinstance(oToken, parser.carriage_return):
          self.iLine += 1
          if self.bIgnoreNextCarriageReturn:
              self.bIgnoreNextCarriageReturn = False
          else:
              self.next_line_code_tags.clear()
