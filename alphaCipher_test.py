 
from alphabetCipherClass import *
import unittest


class TestAlphabetCipher(unittest.TestCase):

    def test_cipherEncoding(self):
        alphaCipher = alphabetCipher()
        keyword = 'scones'
        inputMessage = 'meetmebythetree'
        encodedMsg = alphaCipher.encodeTheMessage(inputMessage,keyword)
        self.assertEqual(encodedMsg, 'egsgqwtahuiljgs', "Should be egsgqwtahuiljgs")
        
        keyword = 'seal'
        inputMessage = 'hilana'
        encodedMsg = alphaCipher.encodeTheMessage(inputMessage,keyword)
        self.assertEqual(encodedMsg, 'zmllfe', "Should be zmllfe")
        
        keyword = 'give'
        inputMessage = 'whateverafter'
        encodedMsg = alphaCipher.encodeTheMessage(inputMessage,keyword)
        self.assertEqual(encodedMsg, 'cpvxkdzvgnoix', "Should be cpvxkdzvgnoix")

    def test_cipherDecoding(self):
        keyword = 'scones'
        inputMessage = 'meetmebythetree'
        alphaCipher = alphabetCipher()
        decodedMsg = alphaCipher.decodeTheMessage('egsgqwtahuiljgs', keyword)
        self.assertEqual(decodedMsg, 'meetmebythetree', "Should be meetmebythetree")
        
        
if __name__ == '__main__':
    unittest.main()
