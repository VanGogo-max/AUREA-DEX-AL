import asyncio
from typing import Dict

# Strategy runner skeleton. Real engine will fetch prices, indicators and evaluate.

async def run_strategy_loop(strategy: Dict, on_signal):
    """
    strategy: dict structure (owner, spec, mode)
    on_signal: callback(signal_data)
    """
    # This is a placeholder loop. Real implementation uses websockets / price feeds.
    while strategy.get("enabled"):
        # compute indicators (TODO)
        # evaluate spec (visual AST -> conditions, or execute code in sandbox)
        # if condition -> await on_signal(...)
        await asyncio.sleep(5)
