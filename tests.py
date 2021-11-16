from funcs import detect_language, translate_input, translate_output


detect_inputs = ['ik heb een helikopter','ich bin ein helikopter','i am a helicopter']
detect_outputs =  [['ik heb een helikopter','nl'],[0,'de'],['i am a helicopter','en']]
ti_inputs = [['ik heb een helikopter','nl'],[0,'de'],['i am a helicopter','en']]
ti_outputs = [['i have a helicopter','nl'],[0,'de'],['i am a helicopter','en']]
to_inputs = [['i have a helicopter','nl'],['i have a helicopter','de'],['i am a helicopter','en']]
to_outputs = ['ik heb een helikopter',0, 'i am a helicopter']

USER_INPUT = [' ' , ' ' , ' ']
EXPECTED_OUTPUT = [' ' , ' ' , ' ']

import unittest

class UnitTest(unittest.TestCase):

    '''UNIT TESTS'''

    def test_detect_language(self):
	'''test detect_language function'''
        self.assertEqual(detect_language(input1), output1)
        
    def test_translate_input(self):
        '''test translate_input function'''
        self.assertEqual(translate_input(input2), output2)
        
    def test_translate_output(self):
        '''test translate_output function'''
        self.assertEqual(translate_output(input3), output3)

    def test_UNIT_TEST4(self):
        '''test user input interface'''
        self.assertEqual( USERINTERFACE( USER_INPUT ), EXPECTED_USER_INPUT) #2nd one should be same as 1st but unmodified or maybe modified in some way we want it to be 

    def test_UNIT_TEST5(self):
        '''test Chatbot'''
        self.assertEqual(  CHATBOT( USER_INPUT  ), EXPECTED_OUTPUT)

    '''INTEGRATION TESTS'''

    def test_integration1(self):
        '''test integration of language detection and subsequent translation if necessary'''
        self.assertEqual(translate_input(detect_language(input1)), output2)
    
    def test_integration2(self):
        '''test integration of UI, language detection/translation and Chatbot'''
        self.assertEqual( CHATBOT ( USERINTERFACE ( translate_input(detect_language( USER_INPUT )))), EXPECTED_CHATBOT_OUTPUT )
        
    def test_integration3(self):
        '''test integration of Chatbot, Translation if necessary and UI output'''
        self.assertEqual( USERINTERFACE (translate_output( CHATBOT ( USER_INPUT ), input3[1]), EXPECTED_OUTPUT) 
        #depending on the input language, the expected output should be unchanged, translated or 0
        #input3[1] corresponds to the oringinal input language, which will be required for the translation function input
   
if __name__ == '__main__':

    for input1, output1, input2, output2, input3, output3 in zip(detect_inputs, detect_outputs, ti_inputs, ti_outputs, to_inputs, to_outputs):

        unittest.main(argv=['first-arg-is-ignored'], verbosity=3, exit=False)
