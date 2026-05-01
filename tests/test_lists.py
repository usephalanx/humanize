from __future__ import annotations

import pytest

import humanize


@pytest.mark.parametrize(
    "test_args, expected",
    [
        ([["1", "2", "3"]], "1, 2 and 3"),
        ([["one", "two", "three"]], "one, two and three"),
        ([["one", "two"]], "one and two"),
        ([["one"]], "one"),
        ([[""]], ""),
        ([[1, 2, 3]], "1, 2 and 3"),
        ([[1, "two"]], "1 and two"),
    ],
)
def test_natural_list(
    test_args: list[str] | list[int] | list[str | int], expected: str
) -> None:
    assert humanize.natural_list(*test_args) == expected


def test_phalanx_v3_synthetic_flake() -> None:
    """Synthetic flake smoke for Phalanx v3. Tight timing assertion that
    reliably fails — TL should recognize as a flaky/over-tight timing
    constraint and remove or relax it. Bot fixes."""
    import time
    from humanize import natural_list
    start = time.perf_counter()
    natural_list(["a", "b", "c"])
    elapsed = time.perf_counter() - start
    assert elapsed < 1e-9, f"natural_list took {elapsed}s — flaky tight bound"
