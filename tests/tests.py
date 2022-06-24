#from src.math import add, subtract, multiply
def test_import():
    import ProcessSegments
    assert type(ProcessSegments) not None

def test_methods():
    import ProcessSegments
    segments = ProcessSegments.process_data()
    assert type(segments) not None
