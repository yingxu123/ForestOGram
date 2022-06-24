#from src.math import add, subtract, multiply
def test_import():
    import ProcessSegments
    assert not type(ProcessSegments) is None

def test_methods():
    import ProcessSegments
    segments = ProcessSegments.process_data()
    assert not type(segments) is None
