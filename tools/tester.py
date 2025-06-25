from typing import Callable, List, Tuple, TypeVar
from tools.my_logger import load_logger
logger = load_logger(DEBUG=True)

T = TypeVar('T')  # Input type
R = TypeVar('R')  # Output type

def run_test_cases(
    func: Callable[[T], R],
    test_cases: List[Tuple[T, R]],
    description: str = ""
) -> None:
    if description:
        logger.info(f"Running tests for: {description}")
    for i, (input_val, expected_output) in enumerate(test_cases, 1):
        logger.info(f"\nTesting {i}: {input_val}")
        actual_output = func(input_val)
        assert actual_output == expected_output, (
            f"Test {i} failed. Input: {input_val!r}, "
            f"Expected: {expected_output}, Got: {actual_output}"
        )
        logger.info(f"Test {i} passed.")
    logger.info("All tests passed.\n")