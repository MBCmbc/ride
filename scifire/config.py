DEFAULT_NUM_FFS = 3
DEFAULT_NUM_IOTS = 6
DEFAULT_NUM_PRIORITIES = 3
DEFAULT_NUM_NET_FLOWS = DEFAULT_NUM_PRIORITIES

DEFAULT_NUM_TOPICS = 5
# TODO: make a list of different topics and probably assign them different priorities/utilities?
IOT_DEV_TOPIC = 'sensor_data'

DEFAULT_VIDEO_RATE_MBPS = 1.0
DEFAULT_VIDEO_PORT = 5000

FIRE_EXPERIMENT_DURATION = 15


# TODO: Move this to global config file once the environment variables have been moved elsewhere
def bandwidth_mbps_to_bps(bw):
    return bw * 1000000
