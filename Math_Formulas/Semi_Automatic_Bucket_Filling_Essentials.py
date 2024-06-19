def calculate_required_flow(goal_volume, desired_time):
    """
    Calculates the flow rate required to fill a bucket in a given time.
    :param goal_volume:
    :param desired_time:
    :return:
    """
    flow_rate = goal_volume / desired_time
    return flow_rate


def calculate_liter_flow_per_hour_from_seconds(input_flow_rate):
    """
    Converts the input flow rate from liters per second to liters per hour
    :param input_flow_rate: input flow rate in liters/second
    :return: output_flow_rate: outplut flow rate in liters/hours
    """
    output_flow_rate = input_flow_rate * 3600
    return output_flow_rate
