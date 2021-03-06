from polyskel import skeletonize

def test_skeletonize():

    polygon = [ # vertices from examples/misshapen
        (100, 50),
        (150, 150),
        (50,  100),
        (50,  250),
        (150, 250),
        (50,  350),
        (350, 350),
        (350, 100),
        (250, 150),
        (300, 50)
    ]

    skel = skeletonize(polygon)

    assert len(skel) > 0