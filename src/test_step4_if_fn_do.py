import unittest
import step4_if_fn_do

deferred = True  # Run deferred tests?

class Step4TestCase(unittest.TestCase):

    def test_if_form(self):
        cases = [
            ('7', step4_if_fn_do.rep_mal('(if true 7 8)')),
            ('8', step4_if_fn_do.rep_mal('(if false 7 8)')),
            ('false', step4_if_fn_do.rep_mal('(if false 7 false)')),
            ('8', step4_if_fn_do.rep_mal('(if true (+ 1 7) (+ 1 8))')),
            ('9', step4_if_fn_do.rep_mal('(if false (+ 1 7) (+ 1 8))')),
            ('8', step4_if_fn_do.rep_mal('(if nil 7 8)')),
            ('7', step4_if_fn_do.rep_mal('(if 0 7 8)')),
            ('7', step4_if_fn_do.rep_mal('(if (list) 7 8)')),
            ('7', step4_if_fn_do.rep_mal('(if (list 1 2 3) 7 8)')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_1_way_if(self):
        cases = [
            ('nil', step4_if_fn_do.rep_mal('(if false (+ 1 7))')),
            ('nil', step4_if_fn_do.rep_mal('(if nil 8)')),
            ('7', step4_if_fn_do.rep_mal('(if nil 8 7)')),
            ('8', step4_if_fn_do.rep_mal('(if true (+ 1 7))')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_fn_form(self):
        cases = [
            ('3', step4_if_fn_do.rep_mal('(+ 1 2)')),
            ('7', step4_if_fn_do.rep_mal('((fn* (a b) (+ b a)) 3 4)')),
            ('4', step4_if_fn_do.rep_mal('((fn* () 4))')),
            ('()', step4_if_fn_do.rep_mal('((fn* () ()))')),
            ('8', step4_if_fn_do.rep_mal('((fn* (f x) (f x)) (fn* (a) (+ 1 a)) 7)')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_closures(self):
        cases = [
            ('12', step4_if_fn_do.rep_mal('(((fn* (a) (fn* (b) (+ a b))) 5) 7)')),
            ('#<function>', step4_if_fn_do.rep_mal('(def! gen-plus5 (fn* () (fn* (b) (+ 5 b))))')),
            ('#<function>', step4_if_fn_do.rep_mal('(def! plus5 (gen-plus5))')),
            ('12', step4_if_fn_do.rep_mal('(plus5 7)')),
            ('#<function>', step4_if_fn_do.rep_mal('(def! gen-plusX (fn* (x) (fn* (b) (+ x b))))')),
            ('#<function>', step4_if_fn_do.rep_mal('(def! plus7 (gen-plusX 7))')),
            ('15', step4_if_fn_do.rep_mal('(plus7 8)')),
            ('0', step4_if_fn_do.rep_mal('(let* [b 0 f (fn* [] b)] (let* [b 1] (f)))')),
            ('0', step4_if_fn_do.rep_mal('((let* [b 0] (fn* [] b)))')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_conditionals(self):
        cases = [
            ('false', step4_if_fn_do.rep_mal('(= 2 1)')),
            ('true', step4_if_fn_do.rep_mal('(= 1 1)')),
            ('false', step4_if_fn_do.rep_mal('(= 1 2)')),
            ('false', step4_if_fn_do.rep_mal('(= 1 (+ 1 1))')),
            ('true', step4_if_fn_do.rep_mal('(= 2 (+ 1 1))')),

            ('true', step4_if_fn_do.rep_mal('(> 2 1)')),
            ('false', step4_if_fn_do.rep_mal('(> 1 1)')),
            ('false', step4_if_fn_do.rep_mal('(> 1 2)')),

            ('true', step4_if_fn_do.rep_mal('(>= 2 1)')),
            ('true', step4_if_fn_do.rep_mal('(>= 1 1)')),
            ('false', step4_if_fn_do.rep_mal('(>= 1 2)')),

            ('false', step4_if_fn_do.rep_mal('(< 2 1)')),
            ('false', step4_if_fn_do.rep_mal('(< 1 1)')),
            ('true', step4_if_fn_do.rep_mal('(< 1 2)')),

            ('false', step4_if_fn_do.rep_mal('(<= 2 1)')),
            ('true', step4_if_fn_do.rep_mal('(<= 1 1)')),
            ('true', step4_if_fn_do.rep_mal('(<= 1 2)')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_recursive_sumdown(self):
        cases = [
            ('#<function>', step4_if_fn_do.rep_mal('(def! sumdown (fn* (N) (if (> N 0) (+ N (sumdown  (- N 1))) 0)))')),
            ('1', step4_if_fn_do.rep_mal('(sumdown 1)')),
            ('3', step4_if_fn_do.rep_mal('(sumdown 2)')),
            ('21', step4_if_fn_do.rep_mal('(sumdown 6)')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_recursive_fibonacci(self):
        cases = [
            ('#<function>', step4_if_fn_do.rep_mal('(def! fib (fn* (N) (if (= N 0) 1 (if (= N 1) 1 (+ (fib (- N 1)) (fib (- N 2)))))))')),
            ('1', step4_if_fn_do.rep_mal('(fib 1)')),
            ('2', step4_if_fn_do.rep_mal('(fib 2)')),
            ('5', step4_if_fn_do.rep_mal('(fib 4)')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_recursive_fn_env(self):
        cases = [
            ('3', step4_if_fn_do.rep_mal('(let* (f (fn* () x) x 3) (f))')),
            ('nil', step4_if_fn_do.rep_mal('(let* (cst (fn* (n) (if (= n 0) nil (cst (- n 1))))) (cst 1))')),
            ('0', step4_if_fn_do.rep_mal('(let* (f (fn* (n) (if (= n 0) 0 (g (- n 1)))) g (fn* (n) (f n))) (f 2))')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_list_fn(self):
        cases = [
            ('()', step4_if_fn_do.rep_mal('(list)')),
            ('true', step4_if_fn_do.rep_mal('(list? (list))')),
            ('false', step4_if_fn_do.rep_mal('(list? nil)')),
            ('true', step4_if_fn_do.rep_mal('(empty? (list))')),
            ('false', step4_if_fn_do.rep_mal('(empty? (list 1))')),
            ('(1 2 3)', step4_if_fn_do.rep_mal('(list 1 2 3)')),
            ('3', step4_if_fn_do.rep_mal('(count (list 1 2 3))')),
            ('0', step4_if_fn_do.rep_mal('(count (list))')),
            ('0', step4_if_fn_do.rep_mal('(count nil)')),
            ('78', step4_if_fn_do.rep_mal('(if (> (count (list 1 2 3)) 3) 89 78)')),
            ('89', step4_if_fn_do.rep_mal('(if (>= (count (list 1 2 3)) 3) 89 78)')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_equality_nil_bool(self):
        cases = [
            ('true', step4_if_fn_do.rep_mal('(= 1 1)')),
            ('true', step4_if_fn_do.rep_mal('(= 0 0)')),
            ('false', step4_if_fn_do.rep_mal('(= 1 0)')),

            ('true', step4_if_fn_do.rep_mal('(= nil nil)')),
            ('false', step4_if_fn_do.rep_mal('(= nil false)')),
            ('false', step4_if_fn_do.rep_mal('(= nil true)')),
            ('false', step4_if_fn_do.rep_mal('(= nil 0)')),
            ('false', step4_if_fn_do.rep_mal('(= nil 1)')),
            ('false', step4_if_fn_do.rep_mal('(= nil "")')),
            ('false', step4_if_fn_do.rep_mal('(= nil ())')),
            ('false', step4_if_fn_do.rep_mal('(= nil [])')),
            ('false', step4_if_fn_do.rep_mal('(= nil {})')),

            ('false', step4_if_fn_do.rep_mal('(= false nil)')),
            ('true', step4_if_fn_do.rep_mal('(= false false)')),
            ('false', step4_if_fn_do.rep_mal('(= false true)')),
            ('false', step4_if_fn_do.rep_mal('(= false 0)')),
            ('false', step4_if_fn_do.rep_mal('(= false 1)')),
            ('false', step4_if_fn_do.rep_mal('(= false "")')),
            ('false', step4_if_fn_do.rep_mal('(= false ())')),
            ('false', step4_if_fn_do.rep_mal('(= false [])')),
            ('false', step4_if_fn_do.rep_mal('(= false {})')),

            ('false', step4_if_fn_do.rep_mal('(= true nil)')),
            ('false', step4_if_fn_do.rep_mal('(= true false)')),
            ('true', step4_if_fn_do.rep_mal('(= true true)')),
            ('false', step4_if_fn_do.rep_mal('(= true 0)')),
            ('false', step4_if_fn_do.rep_mal('(= true 1)')),
            ('false', step4_if_fn_do.rep_mal('(= true "")')),
            ('false', step4_if_fn_do.rep_mal('(= true ())')),
            ('false', step4_if_fn_do.rep_mal('(= true [])')),
            ('false', step4_if_fn_do.rep_mal('(= true {})')),

            ('true', step4_if_fn_do.rep_mal('(= (list) (list))')),
            ('true', step4_if_fn_do.rep_mal('(= (list) ())')),
            ('true', step4_if_fn_do.rep_mal('(= (list 1 2) (list 1 2))')),
            ('false', step4_if_fn_do.rep_mal('(= (list 1) (list))')),
            ('false', step4_if_fn_do.rep_mal('(= (list) (list 1))')),
            ('false', step4_if_fn_do.rep_mal('(= 0 (list))')),
            ('false', step4_if_fn_do.rep_mal('(= (list) 0)')),
            ('false', step4_if_fn_do.rep_mal('(= (list nil) (list))')),
            ('false', step4_if_fn_do.rep_mal('(= (list) nil)')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_do_form(self):
        cases = [
            ('nil', step4_if_fn_do.rep_mal('(do (prn 101))')),
            ('7', step4_if_fn_do.rep_mal('(do (prn 102) 7)')),
            ('3', step4_if_fn_do.rep_mal('(do (prn 101) (prn 102) (+ 1 2))')),
            ('14', step4_if_fn_do.rep_mal('(do (def! a 6) 7 (+ a 8))')),
            ('6', step4_if_fn_do.rep_mal('a')),
            ('#<function>', step4_if_fn_do.rep_mal('(def! DO (fn* (a) 7))')),
            ('7', step4_if_fn_do.rep_mal('(DO 3)')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    @unittest.skipUnless(deferred, "deferred")
    def test_if_string(self):
        expected = '7'
        observed = step4_if_fn_do.rep_mal('(if "" 7 8)')
        self.assertEqual(expected, observed)

    @unittest.skipUnless(deferred, "deferred")
    def test_string_equality(self):
        cases = [
            ('true', step4_if_fn_do.rep_mal('(= "" "")')),
            ('true', step4_if_fn_do.rep_mal('(= "abc" "abc")')),
            ('false', step4_if_fn_do.rep_mal('(= "abc" "")')),
            ('false', step4_if_fn_do.rep_mal('(= "" "abc")')),
            ('false', step4_if_fn_do.rep_mal('(= "abc" "def")')),
            ('false', step4_if_fn_do.rep_mal('(= "abc" "ABC")')),
            ('false', step4_if_fn_do.rep_mal('(= (list) "")')),
            ('false', step4_if_fn_do.rep_mal('(= "" (list))')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    @unittest.skipUnless(deferred, "deferred")
    def test_mal_defined_not(self):
        cases = [
            ('true', step4_if_fn_do.rep_mal('(not false)')),
            ('true', step4_if_fn_do.rep_mal('(not nil)')),
            ('false', step4_if_fn_do.rep_mal('(not true)')),
            ('false', step4_if_fn_do.rep_mal('(not "a")')),
            ('false', step4_if_fn_do.rep_mal('(not 0)')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    @unittest.skipUnless(deferred, "deferred")
    def test_var_length_args(self):
        cases = [
            ('3', step4_if_fn_do.rep_mal('((fn* (& more) (count more)) 1 2 3)')),
            ('true', step4_if_fn_do.rep_mal('((fn* (& more) (list? more)) 1 2 3)')),
            ('1', step4_if_fn_do.rep_mal('((fn* (& more) (count more)) 1)')),
            
            # ('0', step4_if_fn_do.rep_mal('((fn* (& more) (count more)))')),
            # ('true', step4_if_fn_do.rep_mal('((fn* (& more) (list? more)))')),

            ('2', step4_if_fn_do.rep_mal('((fn* (a & more) (count more)) 1 2 3)')),
            
            # ('0', step4_if_fn_do.rep_mal('((fn* (a & more) (count more)) 1)')),
            # ('true', step4_if_fn_do.rep_mal('((fn* (a & more) (list? more)) 1)')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    """
    ;; -----------------------------------------------------

    ;; Testing string quoting

    ""
    ;=>""

    "abc"
    ;=>"abc"

    "abc  def"
    ;=>"abc  def"

    "\""
    ;=>"\""

    "abc\ndef\nghi"
    ;=>"abc\ndef\nghi"

    "abc\\def\\ghi"
    ;=>"abc\\def\\ghi"

    "\\n"
    ;=>"\\n"

    ;; Testing pr-str

    (pr-str)
    ;=>""

    (pr-str "")
    ;=>"\"\""

    (pr-str "abc")
    ;=>"\"abc\""

    (pr-str "abc  def" "ghi jkl")
    ;=>"\"abc  def\" \"ghi jkl\""

    (pr-str "\"")
    ;=>"\"\\\"\""

    (pr-str (list 1 2 "abc" "\"") "def")
    ;=>"(1 2 \"abc\" \"\\\"\") \"def\""

    (pr-str "abc\ndef\nghi")
    ;=>"\"abc\\ndef\\nghi\""

    (pr-str "abc\\def\\ghi")
    ;=>"\"abc\\\\def\\\\ghi\""

    (pr-str (list))
    ;=>"()"

    ;; Testing str

    (str)
    ;=>""

    (str "")
    ;=>""

    (str "abc")
    ;=>"abc"

    (str "\"")
    ;=>"\""

    (str 1 "abc" 3)
    ;=>"1abc3"

    (str "abc  def" "ghi jkl")
    ;=>"abc  defghi jkl"

    (str "abc\ndef\nghi")
    ;=>"abc\ndef\nghi"

    (str "abc\\def\\ghi")
    ;=>"abc\\def\\ghi"

    (str (list 1 2 "abc" "\"") "def")
    ;=>"(1 2 abc \")def"

    (str (list))
    ;=>"()"

    ;; Testing prn
    (prn)
    ;/
    ;=>nil

    (prn "")
    ;/""
    ;=>nil

    (prn "abc")
    ;/"abc"
    ;=>nil

    (prn "abc  def" "ghi jkl")
    ;/"abc  def" "ghi jkl"

    (prn "\"")
    ;/"\\""
    ;=>nil

    (prn "abc\ndef\nghi")
    ;/"abc\\ndef\\nghi"
    ;=>nil

    (prn "abc\\def\\ghi")
    ;/"abc\\\\def\\\\ghi"
    nil

    (prn (list 1 2 "abc" "\"") "def")
    ;/\(1 2 "abc" "\\""\) "def"
    ;=>nil


    ;; Testing println
    (println)
    ;/
    ;=>nil

    (println "")
    ;/
    ;=>nil

    (println "abc")
    ;/abc
    ;=>nil

    (println "abc  def" "ghi jkl")
    ;/abc  def ghi jkl

    (println "\"")
    ;/"
    ;=>nil

    (println "abc\ndef\nghi")
    ;/abc
    ;/def
    ;/ghi
    ;=>nil

    (println "abc\\def\\ghi")
    ;/abc\\def\\ghi
    ;=>nil

    (println (list 1 2 "abc" "\"") "def")
    ;/\(1 2 abc "\) def
    ;=>nil


    ;; Testing keywords
    (= :abc :abc)
    ;=>true
    (= :abc :def)
    ;=>false
    (= :abc ":abc")
    ;=>false
    (= (list :abc) (list :abc))
    ;=>true

    ;; Testing vector truthiness
    (if [] 7 8)
    ;=>7

    ;; Testing vector printing
    (pr-str [1 2 "abc" "\""] "def")
    ;=>"[1 2 \"abc\" \"\\\"\"] \"def\""

    (pr-str [])
    ;=>"[]"

    (str [1 2 "abc" "\""] "def")
    ;=>"[1 2 abc \"]def"

    (str [])
    ;=>"[]"


    ;; Testing vector functions
    (count [1 2 3])
    ;=>3
    (empty? [1 2 3])
    ;=>false
    (empty? [])
    ;=>true
    (list? [4 5 6])
    ;=>false

    ;; Testing vector equality
    (= [] (list))
    ;=>true
    (= [7 8] [7 8])
    ;=>true
    (= [:abc] [:abc])
    ;=>true
    (= (list 1 2) [1 2])
    ;=>true
    (= (list 1) [])
    ;=>false
    (= [] [1])
    ;=>false
    (= 0 [])
    ;=>false
    (= [] 0)
    ;=>false
    (= [] "")
    ;=>false
    (= "" [])
    ;=>false

    ;; Testing vector parameter lists
    ( (fn* [] 4) )
    ;=>4
    ( (fn* [f x] (f x)) (fn* [a] (+ 1 a)) 7)
    ;=>8

    ;; Nested vector/list equality
    (= [(list)] (list []))
    ;=>true
    (= [1 2 (list 3 4 [5 6])] (list 1 2 [3 4 (list 5 6)]))
    ;=>true
    """
