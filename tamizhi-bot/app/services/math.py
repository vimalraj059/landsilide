from __future__ import annotations

import math
import re
from typing import Optional


def solve_expression(expr: str) -> Optional[float]:
    """Safely evaluate basic math expressions (digits, + - * / ^ parentheses).
    Returns None if unsafe or invalid.
    """
    if not re.fullmatch(r"[\d\s+\-*/().^]+", expr):
        return None
    safe_expr = expr.replace("^", "**")
    try:
        value = eval(safe_expr, {"__builtins__": {}}, {"sqrt": math.sqrt, "pi": math.pi, "e": math.e})
    except Exception:
        return None
    try:
        return float(value)
    except Exception:
        return None

