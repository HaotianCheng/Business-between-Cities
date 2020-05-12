import unittest
import core


class MyTest(unittest.TestCase):
    def test(self):
        apple = core.Cargo('Apple',1,2,3)
        self.assertEqual(apple.getName(),'Apple')
        self.assertEqual(apple.getPrice(),1)
        self.assertEqual(apple.getNum(),3)
        apple.setNum(5)
        self.assertEqual(apple.getNum(),5)

if __name__ == "__main__":
    unittest.main()
