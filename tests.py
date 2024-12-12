import unittest

def multiply_numbers(a, b):
    return a * b

def reverse_list(input_list):
    return input_list[::-1]

def calculate_discount(price, discount_percentage):
    if price < 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Invalid input: Price must be positive and discount between 0 and 100")
    return price - (price * discount_percentage / 100)

class MathOperations:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

class TestFunctions(unittest.TestCase):
    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(3, 4), 12)
        self.assertEqual(multiply_numbers(5, 0), 0)
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(-2, -3), 6)

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list([]), [])
        self.assertEqual(reverse_list([1]), [1])

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(100, 10), 90)
        self.assertEqual(calculate_discount(100, 0), 100)
        self.assertEqual(calculate_discount(0, 10), 0)
        with self.assertRaises(ValueError):
            calculate_discount(-100, 10)
        with self.assertRaises(ValueError):
            calculate_discount(100, -10)
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)

class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.math_ops = MathOperations()

    def test_is_prime(self):
        self.assertTrue(self.math_ops.is_prime(2))
        self.assertTrue(self.math_ops.is_prime(17))
        self.assertFalse(self.math_ops.is_prime(4))
        self.assertFalse(self.math_ops.is_prime(15))
        self.assertFalse(self.math_ops.is_prime(0))
        self.assertFalse(self.math_ops.is_prime(1))
        self.assertFalse(self.math_ops.is_prime(-5))

    def test_factorial(self):
        self.assertEqual(self.math_ops.factorial(5), 120)
        self.assertEqual(self.math_ops.factorial(3), 6)
        self.assertEqual(self.math_ops.factorial(0), 1)
        with self.assertRaises(ValueError):
            self.math_ops.factorial(-1)

if __name__ == '__main__':
    unittest.main()