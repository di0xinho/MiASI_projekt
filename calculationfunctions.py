from sympy import symbols, sympify, simplify, expand
from sympy.printing.latex import latex

# Funkcja przyjmuje dwa argumenty:
# Pierwszy - wyrażenie matematyczne, które jest pobierane z odpowiedniego wejścia tekstowego
# Drugi - słownik zmiennych z odpowiednio przypisanymi wartościami, np. {'x': 2, 'y':4}
# Na wyjściu zwracane jest wyrażenie matematyczne w postaci stringa wraz z wyrażeniem dla formatu LaTeXa w celu
# wygenerowania odpowiedniego wykresu w bibliotece matplotlib
def calculate_expression(raw_expression, vars):

    # Symbole do obliczeń matematycznych
    sym_vars = {k: symbols(k) for k in vars.keys()}
    
    # Parsowanie wejścia (wyrażenia matematycznego na wejściu)
    expression = sympify(raw_expression)
    
    # Zamiana zmiennych na wartości
    expression = expression.subs(sym_vars)
    print(expression)
    
    # Obliczanie wartości wyrażenia przez podstawienie wartości
    result = expression.evalf(subs = vars)
    
    # Generowanie wyrażenia w formacie LaTeX
    latex_expression = latex(expression)
    
    return result, latex_expression

# Funkcja upraszczająca wyrażenie matematyczne do postaci wielomianu
# Funkcja przyjmuje argument w postaci wyrażenia matematycznego
# Na wyjściu zwraca uproszczone wyrażenie w postaci wielomianu oraz jego reprezentację w formacie LaTeX
def simplify_to_polynomial(raw_expression):
    
    # Parsowanie wyrażenia
    expression = sympify(raw_expression)
    
    # Upraszczanie do wielomianu
    simplified_expression = simplify(expand(expression))
    
    # Generowanie wyrażenia w formacie LaTeX
    latex_expression = latex(simplified_expression)
    
    return str(simplified_expression), latex_expression
