import unittest
import step1_read_print

deferred = True  # Run deferred tests?
optional = False  # Run optional tests?

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
            ('"\\"', step1_read_print.rep_mal('"\\"')),
            ('"\\\\\\\\\\\\\\\\\\"', step1_read_print.rep_mal('"\\\\\\\\\\\\\\\\\\"')),
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
            ('error: no input', step1_read_print.rep_mal('')),
            # ('error: unbalanced', step1_read_print.rep_mal('[1 2')),
            # ('error: unbalanced', step1_read_print.rep_mal('{"a" 2')),
            # ('error: unbalanced', step1_read_print.rep_mal('"abc')),
            ('"abc', step1_read_print.rep_mal('"abc')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])


"""

;;; These should throw some error with no return value
"abc
;/.*(EOF|end of input|unbalanced).*
"
;/.*(EOF|end of input|unbalanced).*
"\"
;/.*(EOF|end of input|unbalanced).*
"\\\\\\\\\\\\\\\\\\\"
;/.*(EOF|end of input|unbalanced).*
(1 "abc
;/.*(EOF|end of input|unbalanced).*
(1 "abc"
;/.*(EOF|end of input|unbalanced).*

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


;; Testing keywords
:kw
;=>:kw
(:kw1 :kw2 :kw3)
;=>(:kw1 :kw2 :kw3)

;; Testing read of vectors
[+ 1 2]
;=>[+ 1 2]
[]
;=>[]
[ ]
;=>[]
[[3 4]]
;=>[[3 4]]
[+ 1 [+ 2 3]]
;=>[+ 1 [+ 2 3]]
  [ +   1   [+   2 3   ]   ]  
;=>[+ 1 [+ 2 3]]
([])
;=>([])

;; Testing read of hash maps
{}
;=>{}
{ }
;=>{}
{"abc" 1}
;=>{"abc" 1}
{"a" {"b" 2}}
;=>{"a" {"b" 2}}
{"a" {"b" {"c" 3}}}
;=>{"a" {"b" {"c" 3}}}
{  "a"  {"b"   {  "cde"     3   }  }}
;=>{"a" {"b" {"cde" 3}}}
;;; The regexp sorcery here ensures that each key goes with the correct
;;; value and that each key appears only once.
{"a1" 1 "a2" 2 "a3" 3}
;/{"a([1-3])" \1 "a(?!\1)([1-3])" \2 "a(?!\1)(?!\2)([1-3])" \3}
{  :a  {:b   {  :cde     3   }  }}
;=>{:a {:b {:cde 3}}}
{"1" 1}
;=>{"1" 1}
({})
;=>({})

;; Testing read of comments
 ;; whole line comment (not an exception)
1 ; comment after expression
;=>1
1; comment after expression
;=>1

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

;; Non alphanumeric characters in strings
;;; \t is not specified enough to be tested
"\n"
;=>"\n"
"#"
;=>"#"
"$"
;=>"$"
"%"
;=>"%"
"."
;=>"."
"\\"
;=>"\\"
"|"
;=>"|"

;; Non alphanumeric characters in comments
1;!
;=>1
1;"
;=>1
1;#
;=>1
1;$
;=>1
1;%
;=>1
1;'
;=>1
1;\
;=>1
1;\\
;=>1
1;\\\
;=>1
1;`
;=>1
;;; Hopefully less problematic characters
1; &()*+,-./:;<=>?@[]^_{|}~
;=>1


"""
