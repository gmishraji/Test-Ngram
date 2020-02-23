from unittest import TestCase, mock
from ngram import _tuplifyString, generateNewText, generateNgram, getCleanText


class ModuleTests(TestCase):
    bigram = {('I', 'may'): ['I'],
              ('I', 'wish'): ['I', 'I'],
              ('may', 'I'): ['wish'],
              ('wish', 'I'): ['may', 'might']
              }

    def test__tuplifyString(self):
        self.assertEqual(_tuplifyString('I may'), ('I', 'may'))

    def test_getCleanText(self):
        with mock.patch('ngram.getCleanText', return_value='I wish I may I wish I might'):
            self.assertEqual(getCleanText('test_file.txt'), 'I wish I may I wish I might')

    def test_generateNgram(self):
        with mock.patch('ngram.getCleanText', return_value='I wish I may I wish I might'):
            self.assertEqual(generateNgram('test_file.txt'), self.bigram)

    def test_generateNewText(self):
        with self.assertRaises(KeyError): generateNewText({})
        self.assertGreater(len(generateNewText(self.bigram)), 0)
