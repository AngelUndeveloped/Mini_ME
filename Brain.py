# I first want to calculate the volume of a bucket
from Math_Formulas.Bucket_Formula import calculate_bucket_volume
from Math_Formulas.Semi_Automatic_Bucket_Filling_Essentials import calculate_required_flow, \
    calculate_liter_flow_per_hour_from_seconds
from Math_Formulas.Semi_Automatic_Bucket_Filling_Hose_Length_Formula import calculate_hose_length
from Math_Formulas.Convert_Between_Units import cm3_to_liters

# Set bucket dimensions
upper_radius = 29  # cm, inner radius of bucket
lower_radius = 21  # cm, inner radius of bucket
bucket_height = 27  # cm
bucket_volume = cm3_to_liters(calculate_bucket_volume(upper_radius, lower_radius, bucket_height))
print("The bucket volume is: ", bucket_volume, "liters")

# Calculate the total hose length needed to transport the water to the bucket in the bathroom.
bin_height = 60  # cm
wall_height = 140  # cm
wall_to_bin_edge_distance = 160  # cm
wall_thickness = 20  # cm
bin_top_radius = 25  # cm

hose_length = calculate_hose_length(bin_height,
                                    wall_height,
                                    wall_to_bin_edge_distance,
                                    wall_thickness,
                                    bin_top_radius)

print("The total length of the hose should be about:", hose_length, "cm.")

# How fast do you want to fill the bucket?
desired_fill_time = 20  # seconds
required_flow = calculate_required_flow(bucket_volume, desired_fill_time)
print("The pump must have a flow rate of: ", required_flow, " liters/second in order to fill the bucket in ",
      desired_fill_time, " seconds.")

print("Commercial water pumps work in liters/hour, so the converted value would be: ",
      calculate_liter_flow_per_hour_from_seconds(required_flow))

"""
Conclusion: I would need a water pump capable of moving more than 1,070 liters per hour or 17.8 Liters per minute.
Using a lower end water pump the time to fill the bucket is far too long.
Using a higher end water pump the cost is more than desired.
The simplest solution is to just get the water from the bin by hand.

If the bucket was further, then that might entail a further look.
"""