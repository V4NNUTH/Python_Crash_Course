import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('ven','vannuth')
        self.assertEqual(formatted_name , 'Ven Vannuth')
        
if __name__ == '__main__':
    unittest.main()