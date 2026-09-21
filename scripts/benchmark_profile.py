"""Small deterministic benchmark for the offline profile validator."""

from __future__ import annotations

import json
import time

from scripts.validate_profile import validate


def main() -> int:
    iterations = 100
    started = time.perf_counter()
    failures = sum(bool(validate()) for _ in range(iterations))
    elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
    result = {
        "iterations": iterations,
        "successful": iterations - failures,
        "failures": failures,
        "elapsedMilliseconds": elapsed_ms,
    }
    print(json.dumps(result, sort_keys=True))
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
