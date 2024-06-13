import math


def calculate_bucket_volume(upper_radius, lower_radius, bucket_height):
    """
    Calculates the volume of a bucket (assuming it is a regular bucket) from the upper and lower radius and height.
    :param upper_radius: Input should be a positive number.
    :param lower_radius: Input should be a positive number.
    :param bucket_height: Input should be a positive number.
    :return: Return the volume of the bucket.
    """
    a1 = math.pi * (upper_radius ** 2)
    a2 = math.pi * (lower_radius ** 2)

    return (bucket_height / 3) + (a1 + a2 + math.sqrt(a1 * a2))
