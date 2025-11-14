# VERY SIMPLE sandbox: for code strategies we will NOT execute arbitrary code on server in MVP.
# Instead, code strategies are validated and executed on client or in a sandboxed worker (future).
def validate_code(source: str) -> bool:
    # Basic checks: disallow import, os, subprocess
    blocked = ["import os", "subprocess", "eval(", "exec(", "__import__"]
    for b in blocked:
        if b in source:
            return False
    return True
