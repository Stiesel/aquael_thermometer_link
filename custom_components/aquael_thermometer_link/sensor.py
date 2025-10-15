import logging
import requests
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator
)
from datetime import timedelta

_LOGGER = logging.getLogger(__name__)

def get_data(ip_address):
    try:
        resp = requests.get(f"http://{ip_address}/readADC", timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as err:
        _LOGGER.error("Error fetching aquarium sensor data: %s", err)
        return {}

async def async_setup_entry(hass, entry, async_add_entities):
    ip_address = entry.data["ip_address"]
    name = entry.data["name"]
    description = entry.data.get("description", "")
    scan_interval = entry.data["scan_interval"]

    async def async_update_data():
        return await hass.async_add_executor_job(get_data, ip_address)

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"Aquael Thermometer Link ({name})",
        update_method=async_update_data,
        update_interval=timedelta(seconds=scan_interval)
    )
    await coordinator.async_config_entry_first_refresh()
    async_add_entities([
        AquariumWassertemperaturSensor(coordinator, name, description),
        AquariumLufttemperaturSensor(coordinator, name, description)
    ])

class AquariumWassertemperaturSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, name, description):
        super().__init__(coordinator)
        self._attr_name = f"{name} Wassertemperatur"
        self._attr_native_unit_of_measurement = TEMP_CELSIUS
        self._attr_extra_state_attributes = {"description": description}

    @property
    def state(self):
        return self.coordinator.data.get("Data")

class AquariumLufttemperaturSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, name, description):
        super().__init__(coordinator)
        self._attr_name = f"{name} Lufttemperatur"
        self._attr_native_unit_of_measurement = TEMP_CELSIUS
        self._attr_extra_state_attributes = {"description": description}

    @property
    def state(self):
        return self.coordinator.data.get("Data2")
