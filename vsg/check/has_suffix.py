
def has_suffix(self, suffixes, words, iLineNumber):
    '''
    Checks if words in the list have allowed suffixes.

    Parameters:

      self: (rule object)

      suffixes: (list of allowed suffixes)

      words: (list of words to check)

      iLineNumber: (integer)
    '''
    for word in words:
        for suffix in suffixes:
            if word.endswith(suffix):
                break
        else:
            self.add_violation(iLineNumber)
