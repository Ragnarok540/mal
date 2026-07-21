import unittest
import step1_read_print

deferred = True  # Run deferred tests?
optional = True  # Run optional tests?

class Step1TestCase(unittest.TestCase):

    def test_read_numbers(self):
        cases = [
            ('1', step1_read_print.rep_mal('1')),
            ('7', step1_read_print.rep_mal('7')),
            ('7', step1_read_print.rep_mal('  7   ')),
            ('-123', step1_read_print.rep_mal('-123')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_read_symbols(self):
        cases = [
            ('+', step1_read_print.rep_mal('+')),
            ('abc', step1_read_print.rep_mal('abc')),
            ('abc', step1_read_print.rep_mal('   abc   ')),
            ('abc5', step1_read_print.rep_mal('abc5')),
            ('abc-def', step1_read_print.rep_mal('abc-def')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_dash(self):
        cases = [
            ('-', step1_read_print.rep_mal('-')),
            ('-abc', step1_read_print.rep_mal('-abc')),
            ('->>', step1_read_print.rep_mal('->>')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_lists(self):
        cases = [
            ('(+ 1 2)', step1_read_print.rep_mal('(+ 1 2)')),
            ('()', step1_read_print.rep_mal('()')),
            ('()', step1_read_print.rep_mal('( )')),
            ('(nil)', step1_read_print.rep_mal('(nil)')),
            ('((3 4))', step1_read_print.rep_mal('((3 4))')),
            ('(+ 1 (+ 2 3))', step1_read_print.rep_mal('(+ 1 (+ 2 3))')),
            ('(+ 1 (+ 2 3))', step1_read_print.rep_mal('  ( +   1   (+   2 3   )   )  ')),
            ('(* 1 2)', step1_read_print.rep_mal('(* 1 2)')),
            ('(** 1 2)', step1_read_print.rep_mal('(** 1 2)')),
            ('(* -3 6)', step1_read_print.rep_mal('(* -3 6)')),
            ('(() ())', step1_read_print.rep_mal('(()())')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_commas_as_whitespace(self):
        expected = '(1 2 3)'
        observed = step1_read_print.rep_mal('(1 2, 3,,,,),,')
        self.assertEqual(expected, observed)

    @unittest.skipUnless(deferred, "deferred")
    def test_nil_true_false(self):
        cases = [
            ('nil', step1_read_print.rep_mal('nil')),
            ('true', step1_read_print.rep_mal('true')),
            ('false', step1_read_print.rep_mal('false')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    @unittest.skipUnless(deferred, "deferred")
    def test_read_strings(self):
        cases = [
            ('"abc"', step1_read_print.rep_mal('"abc"')),
            ('"abc"', step1_read_print.rep_mal('   "abc"   ')),
            ('"abc (with parens)"', step1_read_print.rep_mal('"abc (with parens)"')),
            (r'''"abc\"def"''', step1_read_print.rep_mal(r'''"abc\"def"''')),
            ('""', step1_read_print.rep_mal('""')),
            (r'''"\\"''', step1_read_print.rep_mal(r'''"\\"''')),
            (r'''"\\\\\\\\\\\\\\\\\\"''', step1_read_print.rep_mal(r'''"\\\\\\\\\\\\\\\\\\"''')),
            ('"&"', step1_read_print.rep_mal('"&"')),
            ('"\'"', step1_read_print.rep_mal('"\'"')),
            ('"("', step1_read_print.rep_mal('"("')),
            ('")"', step1_read_print.rep_mal('")"')),
            ('"*"', step1_read_print.rep_mal('"*"')),
            ('"+"', step1_read_print.rep_mal('"+"')),
            ('","', step1_read_print.rep_mal('","')),
            ('"-"', step1_read_print.rep_mal('"-"')),
            ('"/"', step1_read_print.rep_mal('"/"')),
            ('":"', step1_read_print.rep_mal('":"')),
            ('";"', step1_read_print.rep_mal('";"')),
            ('"<"', step1_read_print.rep_mal('"<"')),
            ('"="', step1_read_print.rep_mal('"="')),
            ('">"', step1_read_print.rep_mal('">"')),
            ('"?"', step1_read_print.rep_mal('"?"')),
            ('"@"', step1_read_print.rep_mal('"@"')),
            ('"["', step1_read_print.rep_mal('"["')),
            ('"]"', step1_read_print.rep_mal('"]"')),
            ('"^"', step1_read_print.rep_mal('"^"')),
            ('"_"', step1_read_print.rep_mal('"_"')),
            ('"`"', step1_read_print.rep_mal('"`"')),
            ('"{"', step1_read_print.rep_mal('"{"')),
            ('"}"', step1_read_print.rep_mal('"}"')),
            ('"~"', step1_read_print.rep_mal('"~"')),
            ('"!"', step1_read_print.rep_mal('"!"')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    @unittest.skipUnless(deferred, "deferred")
    def test_reader_errors(self):
        cases = [
            ('error: unbalanced', step1_read_print.rep_mal('(')),
            ('error: unbalanced', step1_read_print.rep_mal('(1 2')),
            ('error: unbalanced', step1_read_print.rep_mal('[1 2')),
            ('error: unbalanced', step1_read_print.rep_mal('{"a" 2')),
            ('error: unbalanced', step1_read_print.rep_mal('"abc')),
            ('error: unbalanced', step1_read_print.rep_mal('"')),
            ('error: unbalanced', step1_read_print.rep_mal(r'''"\"''')),
            ('error: unbalanced', step1_read_print.rep_mal(r'''"\\\\\\\\\\\\\\\\\\\"''')),
            ('error: unbalanced', step1_read_print.rep_mal('(1 "abc')),
            ('error: unbalanced', step1_read_print.rep_mal('(1 "abc"')),
            ('error: no input', step1_read_print.rep_mal('')),  # custom test
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    """
    ;; deferred
    ;; Testing read of quoting
    '1
    ;=>(quote 1)
    '(1 2 3)
    ;=>(quote (1 2 3))
    `1
    ;=>(quasiquote 1)
    `(1 2 3)
    ;=>(quasiquote (1 2 3))
    `(a (b) c)
    ;=>(quasiquote (a (b) c))
    ~1
    ;=>(unquote 1)
    ~(1 2 3)
    ;=>(unquote (1 2 3))
    `(1 ~a 3)
    ;=>(quasiquote (1 (unquote a) 3))
    ~@(1 2 3)
    ;=>(splice-unquote (1 2 3))


    """

    @unittest.skipUnless(deferred, "deferred")
    def test_keywords(self):
        cases = [
            (':kw', step1_read_print.rep_mal(':kw')),
            ('(:kw1 :kw2 :kw3)', step1_read_print.rep_mal('(:kw1 :kw2 :kw3)')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    @unittest.skipUnless(deferred, "deferred")
    def test_read_of_vectors(self):
        cases = [
            ('[+ 1 2]', step1_read_print.rep_mal('[+ 1 2]')),
            ('[]', step1_read_print.rep_mal('[]')),
            ('[]', step1_read_print.rep_mal('[ ]')),
            ('[[3 4]]', step1_read_print.rep_mal('[[3 4]]')),
            ('[+ 1 [+ 2 3]]', step1_read_print.rep_mal('[+ 1 [+ 2 3]]')),
            ('[+ 1 [+ 2 3]]', step1_read_print.rep_mal('  [ +   1   [+   2 3   ]   ]  ')),
            ('([])', step1_read_print.rep_mal('([])')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    @unittest.skipUnless(deferred, "deferred")
    def test_read_of_hashmaps(self):
        cases = [
            ('{}', step1_read_print.rep_mal('{}')),
            ('{}', step1_read_print.rep_mal('{ }')),
            ('{"abc" 1}', step1_read_print.rep_mal('{"abc" 1}')),
            ('{"a" {"b" 2}}', step1_read_print.rep_mal('{"a" {"b" 2}}')),
            ('{"a" {"b" {"c" 3}}}', step1_read_print.rep_mal('{"a" {"b" {"c" 3}}}')),
            ('{"a" {"b" {"cde" 3}}}', step1_read_print.rep_mal(' {  "a"  {"b"   {  "cde"     3   }  }}   ')),
            ('{"a1" 1 "a2" 2 "a3" 3}', step1_read_print.rep_mal('{"a1" 1 "a2" 2 "a3" 3}')),
            ('{:a {:b {:cde 3}}}', step1_read_print.rep_mal('{  :a  {:b   {  :cde     3   }  }}')),
            ('{"1" 1}', step1_read_print.rep_mal('{"1" 1}')),
            ('({})', step1_read_print.rep_mal('({})')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    @unittest.skipUnless(deferred, "deferred")
    def test_read_of_comments(self):
        cases = [
            ('1', step1_read_print.rep_mal('1 ; comment after expression')),
            ('1', step1_read_print.rep_mal('1; comment after expression')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    """
    ;; deferred
    ;; Testing read of @/deref
    @a
    ;=>(deref a)

    ;; Colon character inside a symbol
    a:
    ;=>a:

    ;>>> soft=True
    ;>>> optional=True
    ;;
    ;; -------- Optional Functionality --------

    ;; Testing read of ^/metadata
    ^{"a" 1} [1 2 3]
    ;=>(with-meta [1 2 3] {"a" 1})
    ^2 [1 2 3]
    ;=>(with-meta [1 2 3] 2)

    
    """

    @unittest.skipUnless(optional, "optional")
    def test_non_alphanum_chars_strings(self):
        cases = [
            (r'"\n"', step1_read_print.rep_mal(r'"\n"')),
            ('"#"', step1_read_print.rep_mal('"#"')),
            ('"$"', step1_read_print.rep_mal('"$"')),
            ('"%"', step1_read_print.rep_mal('"%"')),
            ('"."', step1_read_print.rep_mal('"."')),
            (r'"\\"', step1_read_print.rep_mal(r'"\\"')),
            ('"|"', step1_read_print.rep_mal('"|"')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    @unittest.skipUnless(optional, "optional")
    def test_non_alphanum_chars_comments(self):
        cases = [
            ('1', step1_read_print.rep_mal('1;!')),
            ('1', step1_read_print.rep_mal('1;"')),
            ('1', step1_read_print.rep_mal('1;#')),
            ('1', step1_read_print.rep_mal('1;$')),
            ('1', step1_read_print.rep_mal('1;%')),
            ('1', step1_read_print.rep_mal("1;'")),
            ('1', step1_read_print.rep_mal('1;\\')),
            ('1', step1_read_print.rep_mal('1;\\\\')),
            ('1', step1_read_print.rep_mal('1;\\\\\\')),
            ('1', step1_read_print.rep_mal('1;`')),
            ('1', step1_read_print.rep_mal('1; &()*+,-./:;<=>?@[]^_{|}~')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])
