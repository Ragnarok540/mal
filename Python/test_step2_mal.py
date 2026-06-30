import unittest
import step2_eval

deferred = True  # Run deferred tests?

class Step2TestCase(unittest.TestCase):

    def test_eval_arithmetic_operations(self):
        cases = [
            ('3', step2_eval.rep_mal('(+ 1 2)')),
            ('11', step2_eval.rep_mal('(+ 5 (* 2 3))')),
            ('8', step2_eval.rep_mal('(- (+ 5 (* 2 3)) 3)')),
            ('2', step2_eval.rep_mal('(/ (- (+ 5 (* 2 3)) 3) 4)')),
            ('1010', step2_eval.rep_mal('(/ (- (+ 515 (* 87 311)) 302) 27)')),
            ('-18', step2_eval.rep_mal('(* -3 6)')),
            ('-994', step2_eval.rep_mal('(/ (- (+ 515 (* -87 311)) 296) 27)')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    def test_eval_error(self):
        expected = 'error: symbol "abc" not found'
        observed = step2_eval.rep_mal('(abc 1 2 3)')
        self.assertEqual(expected, observed)

    def test_empty_list(self):
        expected = '()'
        observed = step2_eval.rep_mal('()')
        self.assertEqual(expected, observed)

    @unittest.skipUnless(deferred, "deferred")
    def test_nil_inside_vector(self):
        expected = '[nil]'
        observed = step2_eval.rep_mal('[nil]')
        self.assertEqual(expected, observed)

    @unittest.skipUnless(deferred, "deferred")
    def test_eval_within_collections(self):
        cases = [
            ('[1 2 3]', step2_eval.rep_mal('[1 2 (+ 1 2)]')),
            ('{"a" 15}', step2_eval.rep_mal('{"a" (+ 7 8)}')),
            ('{:a 15}', step2_eval.rep_mal('{:a (+ 7 8)}')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])

    @unittest.skipUnless(deferred, "deferred")
    def test_eval_empty_collections(self):
        cases = [
            ('[]', step2_eval.rep_mal('[]')),
            ('{}', step2_eval.rep_mal('{}')),
        ]
        for cas in cases:
            self.assertEqual(cas[0], cas[1])
