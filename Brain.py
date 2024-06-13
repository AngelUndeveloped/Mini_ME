# I first want to calculate the volume of a bucket
from Math_Formulas.Bucket_Formula import calculate_bucket_volume

# Set bucket dimensions
upper_radius = 29  # cm, inner radius of bucket
lower_radius = 21  # cm, inner radius of bucket
bucket_height = 27  # cm
units = "cm"
bucket_volume = calculate_bucket_volume(upper_radius, lower_radius, bucket_height)
print("The bucket volume is: ", bucket_volume, units, "^2")
