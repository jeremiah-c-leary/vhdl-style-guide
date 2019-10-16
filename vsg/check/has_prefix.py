
def has_prefix(self, prefixes, words, iLineNumber):
    '''
    Checks if words in the list have allowed prefixes.

    Parameters:

      self: (rule object)

      prefixes: (list of allowed prefixes)

      words: (list of words to check)

      iLineNumber: (integer)
    '''
    for word in words:
        for prefix in prefixes:
            if word.lower().startswith(prefix.lower()):
                break
        else:
            self.add_violation(iLineNumber)
