# conftest.py

import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "IvinPro_test: Marker for test cases related to Lifeeazy product.")
    config.addinivalue_line("markers", "Lifeeazy_test: Marker for test cases related to Ivin_Pro product.")