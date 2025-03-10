"""Eight Sleep constants."""

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass

DOMAIN = "eight_sleep"


class NameMapEntity:
    """Represent a mapping between API values and sensor entity attributes.

    Maps internal Eight Sleep API values to Home Assistant sensor entities
    with appropriate names, units, and classifications.
    """

    def __init__(
        self,
        name: str,
        measurement: str | None = None,
        device_class: SensorDeviceClass | None = None,
        state_class: SensorStateClass | None = SensorStateClass.MEASUREMENT,
    ) -> None:
        """Initialize a name map entity.

        Args:
            name: Display name of the entity
            measurement: Unit of measurement
            device_class: Sensor device class
            state_class: Sensor state class, defaults to measurement

        """
        self.name = name
        self.measurement = measurement
        self.device_class = device_class
        self.state_class = state_class

    def __str__(self) -> str:
        """Return the display name of the entity."""
        return self.name


NAME_MAP = {
    "current_sleep_quality_score": NameMapEntity("Sleep Quality Score", "%"),
    "current_sleep_fitness_score": NameMapEntity("Sleep Fitness Score", "%"),
    "current_sleep_routine_score": NameMapEntity("Sleep Routine Score", "%"),
    "current_heart_rate": NameMapEntity("Heart Rate", "bpm"),
    "current_hrv": NameMapEntity("HRV", "ms"),
    "current_breath_rate": NameMapEntity("Breath Rate", "/min"),
    "time_slept": NameMapEntity("Time Slept", "s", SensorDeviceClass.DURATION),
    "presence_start": NameMapEntity(
        "Presence Start", device_class=SensorDeviceClass.TIMESTAMP, state_class=None
    ),
    "presence_end": NameMapEntity(
        "Presence End", device_class=SensorDeviceClass.TIMESTAMP, state_class=None
    ),
    "next_alarm": NameMapEntity(
        "Next Alarm", device_class=SensorDeviceClass.TIMESTAMP, state_class=None
    ),
    "target_heating_temp": NameMapEntity(
        "Target Temperature",
        "°C",
        SensorDeviceClass.TEMPERATURE,
        SensorStateClass.MEASUREMENT,
    ),
}

SERVICE_HEAT_SET = "heat_set"
SERVICE_HEAT_INCREMENT = "heat_increment"
SERVICE_SIDE_OFF = "side_off"
SERVICE_SIDE_ON = "side_on"
SERVICE_ALARM_SNOOZE = "alarm_snooze"
SERVICE_ALARM_STOP = "alarm_stop"
SERVICE_ALARM_DISMISS = "alarm_dismiss"
SERVICE_AWAY_MODE_START = "away_mode_start"
SERVICE_AWAY_MODE_STOP = "away_mode_stop"

ATTR_TARGET = "target"
ATTR_DURATION = "duration"
ATTR_SERVICE_SLEEP_STAGE = "sleep_stage"
