
#!/usr/bin/env python
from prometheus_client import CollectorRegistry, Gauge, write_to_textfile
from mh_z19b.sync import Sensor

TTY_DEVICE    = '/dev/ttyUSB0'
TTY_BAUDRATE  = 9600
EXPORTER_PATH = '/opt/node_exporter/custom_metrics'

sensor = Sensor(port=TTY_DEVICE, baudrate=TTY_BAUDRATE)

registry = CollectorRegistry()
gauge = Gauge('room_air_condition', 'Air condition measured by MH-Z19B', ['kind'], registry=registry)

result = sensor.read_metric()

gauge.labels('temperature_celsius').set(result.temperature)
gauge.labels('co2_ppm').set(result.co2)

write_to_textfile(EXPORTER_PATH + '/room_air_condition.prom', registry)
