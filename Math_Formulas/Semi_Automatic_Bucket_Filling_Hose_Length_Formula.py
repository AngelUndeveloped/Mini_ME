def calculate_hose_length(bin_height,
                          wall_height,
                          wall_to_bin_edge_distance,
                          wall_thickness,
                          bin_top_radius):
    """
    Calculates the length of the hose used to transport the water from the bin to the bucket. All inputs must be the
    same unit size.
    :param bin_height: height of the bin.
    :param wall_height: height of the wall.
    :param wall_to_bin_edge_distance: distance from the wall to the edge of the bin.
    :param wall_thickness: thickness of the wall.
    :param bin_top_radius: radius of the top of the bin.

    :return: total length of the hose required to transport the water from the bin.

    """
    return (wall_height * 2) + wall_thickness + wall_to_bin_edge_distance + bin_top_radius + (bin_height * 2)
