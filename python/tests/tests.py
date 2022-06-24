import sys
import ProcessSegments
def test_import():
    assert not type(ProcessSegments) is None

def test_methods():
    segments = ProcessSegments.process_data()
    assert not type(segments) is None
