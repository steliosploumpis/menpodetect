from menpodetect.conversion import bounding_box


def pointgraph_from_rect(rect):
    r"""
    Convert an ffld2 detection to a menpo.shape.PointDirectedGraph.
    This enforces a particular point ordering.

    Parameters
    ----------
    rect : `tuple`
        The bounding box to convert. Result of calling an opencv detection.

    Returns
    -------
    bounding_box : `menpo.shape.PointDirectedGraph`
        A menpo PointDirectedGraph giving the bounding box.
    """
    return bounding_box((rect.y, rect.x),
                        (rect.y + rect.height, rect.x + rect.width))
