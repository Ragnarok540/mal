import unittest
import step3_env

optional = True  # Run optional tests?

class Step3TestCase(unittest.TestCase):

    def test_repl_env(self):
        cases = [
            ('3', step3_env.rep_mal('(+ 1 2)')),
            ('2', step3_env.rep_mal('(/ (- (+ 5 (* 2 3)) 3) 4)')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_def(self):
        cases = [
            ('3', step3_env.rep_mal('(def! x 3)')),
            ('3', step3_env.rep_mal('x')),
            ('4', step3_env.rep_mal('(def! x 4)')),
            ('4', step3_env.rep_mal('x')),
            ('8', step3_env.rep_mal('(def! y (+ 1 7))')),
            ('8', step3_env.rep_mal('y')),
            ('12', step3_env.rep_mal('(+ x y)'))
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_case_sensitive_symbols(self):
        cases = [
            ('111', step3_env.rep_mal('(def! mynum 111)')),
            ('222', step3_env.rep_mal('(def! MYNUM 222)')),
            ('111', step3_env.rep_mal('mynum')),
            ('222', step3_env.rep_mal('MYNUM')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_env_lookup(self):
        cases = [
            ('error: symbol "abc" not found', step3_env.rep_mal('(abc 1 2 3)')),
            ('123', step3_env.rep_mal('(def! w 123)')),
            ('error: symbol "abc" not found', step3_env.rep_mal('(def! w (abc))')),
            ('123', step3_env.rep_mal('w')),
        ]

        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    """
;; Testing let*
(let* (z 9) z)
;=>9
(let* (x 9) x)
;=>9
x
;=>4
(let* (z (+ 2 3)) (+ 1 z))
;=>6
(let* (p (+ 2 3) q (+ 2 p)) (+ p q))
;=>12
(def! y (let* (z 7) z))
y
;=>7

;; Testing outer environment
(def! a 4)
;=>4
(let* (q 9) q)
;=>9
(let* (q 9) a)
;=>4
(let* (z 2) (let* (q 9) a))
;=>4

;>>> deferrable=True
;;
;; -------- Deferrable Functionality --------

;; Testing let* with vector bindings
(let* [z 9] z)
;=>9
(let* [p (+ 2 3) q (+ 2 p)] (+ p q))
;=>12

;; Testing vector evaluation
(let* (a 5 b 6) [3 4 a [b 7] 8])
;=>[3 4 5 [6 7] 8]

;>>> soft=True
;>>> optional=True
;;
;; -------- Optional Functionality --------

;; Check that last assignment takes priority
(let* (x 2 x 3) x)
;=>3

;; Check DEBUG-EVAL
(let* (DEBUG-EVAL false) (- 3 1))
;=>2
(let* (DEBUG-EVAL nil) (- 3 1))
;=>2
;;; Some implementations avoid a recursive EVAL when the first element
;;; is a symbol or when map(EVAL, list) encounters a number.
(let* (a 3 b 2 DEBUG-EVAL true) (- a b))
;/EVAL: \(- a b\).*\n1
;; Check the readably pretty-printing option
(let* (DEBUG-EVAL 1) "a")
;/EVAL: "a".*\n"a"
;; Usually false values
(let* (a 3 DEBUG-EVAL ()) a)
;/EVAL: a.*\n3
(let* (a 3 DEBUG-EVAL 0) a)
;/EVAL: a.*\n3
(let* (a 3 DEBUG-EVAL "") a)
;/EVAL: a.*\n3
    """
