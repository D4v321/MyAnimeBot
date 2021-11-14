import funcs

detect_inputs = ['ik heb een helikopter','ich bin ein helikopter','i am a helicopter']
detect_outputs =  [['ik heb een helikopter','nl'],[0,'de'],['i am a helicopter','en']]
ti_inputs = [['ik heb een helikopter','nl'],[0,'de'],['i am a helicopter','en']]
ti_outputs = [['i have a helicopter','nl'],[0,'de'],['i am a helicopter','en']]
to_inputs = [['i have a helicopter','nl'],['i have a helicopter','de'],['i am a helicopter','en']]
to_outputs = ['ik heb een helikopter',0, 'i am a helicopter']

import unittest

class UnitTest(unittest.TestCase):
    def test_detect_language(self):
        self.assertEqual(detect_language(input1), output1)

    def test_translate_input(self):
        self.assertEqual(translate_input(input2), output2)

    def test_translate_output(self):
        self.assertEqual(translate_output(input3), output3)
        
if __name__ == '__main__':
    for input1, output1, input2, output2, input3, output3 in zip(detect_inputs, detect_outputs, ti_inputs, ti_outputs, to_inputs, to_outputs):
        unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)
