import unittest
import sys
import os

# Dodajemy katalog główny do ścieżki
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculationfunctions import calculate_expression, simplify_to_polynomial

# Klasa z testami jednostkowymi sprawdzające działanie funkcji 
class TestCalculationFunctions(unittest.TestCase):

    # Sprawdzanie funkcji calculate_expression
    def test_calculate_expression(self):

        # Arrange
        expression = "2*x + 3*y - 4"
        vars = {'x': 1, 'y': 2}

        # Act
        result, latex_expression = calculate_expression(expression, vars)
        
        # Assert
        self.assertAlmostEqual(result, 4.0)
        self.assertEqual(latex_expression, '2 x + 3 y - 4')
        
        # Arrange
        expression_2 = "x**2 + y**2"
        vars_2 = {'x': 3, 'y': 4}

        # Act
        result_2, latex_expression_2 = calculate_expression(expression_2, vars_2)
        
        # Assert
        self.assertAlmostEqual(result_2, 25.0)
        self.assertEqual(latex_expression_2, 'x^{2} + y^{2}')
    
    # Sprawdzanie funkcji simplify_to_polynomial
    def test_simplify_to_polynomial(self):

        # Arrange
        expression = "2*x**2 + 3*x + 2 - 4*x**2 + x"
        
        # Act
        simplified_expression, latex_simplified_expression = simplify_to_polynomial(expression)
        
        # Assert
        self.assertEqual(simplified_expression, '-2*x**2 + 4*x + 2')
        self.assertEqual(latex_simplified_expression, '- 2 x^{2} + 4 x + 2')
        
        # Arrange
        expression_2 = "(x + 1)*(x - 1)"

        # Act
        simplified_expression_2, latex_simplified_expression_2 = simplify_to_polynomial(expression_2)
        
        # Assert
        self.assertEqual(simplified_expression_2, 'x**2 - 1')
        self.assertEqual(latex_simplified_expression_2, 'x^{2} - 1')

if __name__ == '__main__':
    unittest.main()
