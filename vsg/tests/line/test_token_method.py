
import unittest

from vsg import line

class testTokenMethod(unittest.TestCase):

    def test_single_spaces(self):
        oLine = line.line('contents of line')
        self.assertTrue(oLine)
        self.assertEqual('contents of line', oLine.line)

        lTokens = []
        lTokens.append('contents')
        lTokens.append(' ')
        lTokens.append('of')
        lTokens.append(' ')
        lTokens.append('line')

        self.assertEqual(lTokens, oLine.tokens)

    def test_multiple_spaces(self):
        oLine = line.line('   contents   of     line')
        self.assertTrue(oLine)
        self.assertEqual('   contents   of     line', oLine.line)

        lTokens = []
        lTokens.append('   ')
        lTokens.append('contents')
        lTokens.append('   ')
        lTokens.append('of')
        lTokens.append('     ')
        lTokens.append('line')

        self.assertEqual(lTokens, oLine.tokens)

    def test_comment_at_end_of_line_without_spaces_around_dashes(self):
        oLine = line.line('contents of line--This is a comment')
        self.assertTrue(oLine)
        self.assertEqual('contents of line--This is a comment', oLine.line)

        lTokens = []
        lTokens.append('contents')
        lTokens.append(' ')
        lTokens.append('of')
        lTokens.append(' ')
        lTokens.append('line')
        lTokens.append('--This is a comment')

        self.assertEqual(lTokens, oLine.tokens)

    def test_comment_at_end_of_line_with_spaces_around_dashes(self):
        oLine = line.line('contents of line --  This is a comment')
        self.assertTrue(oLine)
        self.assertEqual('contents of line --  This is a comment', oLine.line)

        lTokens = []
        lTokens.append('contents')
        lTokens.append(' ')
        lTokens.append('of')
        lTokens.append(' ')
        lTokens.append('line')
        lTokens.append(' ')
        lTokens.append('--  This is a comment')

        self.assertEqual(lTokens, oLine.tokens)

    def test_comment_at_end_of_line_with_spaces_at_the_end_of_line(self):
        oLine = line.line('contents of line --  This is a comment  ')
        self.assertTrue(oLine)
        self.assertEqual('contents of line --  This is a comment  ', oLine.line)

        lTokens = []
        lTokens.append('contents')
        lTokens.append(' ')
        lTokens.append('of')
        lTokens.append(' ')
        lTokens.append('line')
        lTokens.append(' ')
        lTokens.append('--  This is a comment  ')

        self.assertEqual(lTokens, oLine.tokens)

    def test_comment_only_line_with_spaces_before_the_comment(self):
        oLine = line.line(' -- This is a comment  ')
        self.assertTrue(oLine)
        self.assertEqual(' -- This is a comment  ', oLine.line)

        lTokens = []
        lTokens.append(' ')
        lTokens.append('-- This is a comment  ')

        self.assertEqual(lTokens, oLine.tokens)

    def test_comment_only_line_without_spaces_before_the_comment(self):
        oLine = line.line('-- This is a comment  ')
        self.assertTrue(oLine)
        self.assertEqual('-- This is a comment  ', oLine.line)

        lTokens = []
        lTokens.append('-- This is a comment  ')

        self.assertEqual(lTokens, oLine.tokens)

