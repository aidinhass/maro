# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from maro.utils import convert_dottable


# Set size default/ add enable/disable
proxy = convert_dottable({
    "fault_tolerant": False,
    "delay_for_slow_joiner": 3,
    "redis": {
        "host": "localhost",
        "port": 6379,
        "max_retries": 5,
        "base_retry_interval": 0.1
    }
    "dynamic_peer": {
        "enable": False,
        "peers_update_frequency": 10,
        "alive_peers": 1.0,    # 1.0 - 0.1 available peers percentage (at least one alive peer)
        "message_cache_for_exited_peer": True,
        "cache_size": 1024,  # May remove
        "max_wait_time_for_rejoin": 300 # second
    }
})

driver = convert_dottable({
    "zmq": {
        "protocol": "tcp",
        "send_timeout": -1,
        "receive_timeout": -1
    }
})
