from typing import Callable, List, Tuple, TypeVar, Literal
from tools.my_logger import load_logger
logger = load_logger(DEBUG=True)

T = TypeVar('T')  # Input type
R = TypeVar('R')  # Output type

def run_test_cases(
    func: Callable[[T], R],
    test_cases: List[Tuple[T, R]],
    passing_condition: Literal['in', 'equal'] = 'equal',
    description: str = ""
) -> None:
    if description:
        logger.info(f"Running tests for: {description}")
    for i, (input_val, expected_output) in enumerate(test_cases, 1):
        logger.info(f"\nTesting {i}: {input_val}")
        actual_output = func(input_val)

        if passing_condition == 'equal': 
            assert actual_output == expected_output, (
                f"Test {i} failed. Input: {input_val!r}, "
                f"Expected: {expected_output}, Got: {actual_output}"
            )
        elif passing_condition == 'in':
            expected_str = " or ".join(str(opt) for opt in expected_output)
            assert actual_output in expected_output, (
                f"Test {i} failed.\n"
                f"  Input: {input_val!r} \n"
                f"  Expected: {expected_str} \n"
                f"  Got: {actual_output} \n"
            )

        logger.info(f"Test {i} passed.")
    logger.info("All tests passed.\n")