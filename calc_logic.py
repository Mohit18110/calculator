def evaluate_expression(expr):
    try:
        # Safer eval with no built-in functions
        result = eval(expr, {"__builtins__": None}, {})
        return result
    except Exception:
        return "Error"
