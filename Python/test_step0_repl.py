import unittest
import step0_repl


class Step0TestCase(unittest.TestCase):

    def test_basic_string(self):
        expected = 'abcABC123'
        observed = step0_repl.rep_mal('abcABC123')
        self.assertEqual(expected, observed)

    def test_string_with_spaces(self):
        expected = 'hello mal world'
        observed = step0_repl.rep_mal('hello mal world')
        self.assertEqual(expected, observed)

    def test_string_with_symbols(self):
        expected = '[]{}"\'* ;:()'
        observed = step0_repl.rep_mal('[]{}"\'* ;:()')
        self.assertEqual(expected, observed)

    def test_long_string(self):
        expected = 'hello world abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 (;:() []{}"\'* ;:() []{}"\'* ;:() []{}"\'*)'
        observed = step0_repl.rep_mal('hello world abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 (;:() []{}"\'* ;:() []{}"\'* ;:() []{}"\'*)')
        self.assertEqual(expected, observed)

    def test_non_aphanumeric(self):
        cases = [
            ('!', step0_repl.rep_mal('!')),
            ('&', step0_repl.rep_mal('&')),
            ('+', step0_repl.rep_mal('+')),
            (',', step0_repl.rep_mal(',')),
            ('-', step0_repl.rep_mal('-')),
            ('/', step0_repl.rep_mal('/')),
            ('<', step0_repl.rep_mal('<')),
            ('=', step0_repl.rep_mal('=')),
            ('>', step0_repl.rep_mal('>')),
            ('?', step0_repl.rep_mal('?')),
            ('@', step0_repl.rep_mal('@')),
            ('^', step0_repl.rep_mal('^')),
            ('_', step0_repl.rep_mal('_')),
            ('`', step0_repl.rep_mal('`')),
            ('~', step0_repl.rep_mal('~')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_non_aphanumeric_optional(self):
        cases = [
            ('#', step0_repl.rep_mal('#')),
            ('$', step0_repl.rep_mal('$')),
            ('%', step0_repl.rep_mal('%')),
            ('.', step0_repl.rep_mal('.')),
            ('|', step0_repl.rep_mal('|')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])
