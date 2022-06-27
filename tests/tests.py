#import sys
#sys.path.insert(0,"./python")
#print(sys.path)

import sound_segmentation

#ProcessSegments = sound_segmentation
#import ProcessSegments
def test_import():
    assert not type(sound_segmentation) is None

#def test_methods():
#    segments = sound_segmentation.process_data()
#    assert not type(segments) is None
