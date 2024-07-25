# tests/test_analysis.py

from src.analysis import run_analysis

def test_run_analysis():
    results = run_analysis()

    # Check if results is not None
    assert results is not None, "run_analysis() returned None"

    # Check if 'mean' key is in results and its value is greater than 0
    assert 'mean' in results, "Expected 'mean' key in results"
    assert results['mean'] > 0, f"Expected 'mean' value > 0, got {results['mean']}"

    # Additional assertions as needed for other metrics like median, mode, etc.
    assert 'median' in results, "Expected 'median' key in results"
    assert 'mode' in results, "Expected 'mode' key in results"
