import logging
from datetime import timedelta
import aiohttp
import async_timeout
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import UnitOfTemperature
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    CoordinatorEntity,
)

_LOGGER = logging.getLogger(__name__)

# ============================================================
# 1. SETUP FUNKTION
# ============================================================
async def async_setup_entry(hass, entry, async_add_entities):
    """Richtet die Sensorplattform für ein konfiguriertes Gerät ein."""
    ip = entry.data["ip_address"]
    name = entry.data["name"]
    description = entry.data.get("description", "")
    scan_interval = entry.data.get("scan_interval", 600)

    coordinator = AquaelDataUpdateCoordinator(hass, ip, name, scan_interval)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([
        AquariumWassertemperaturSensor(coordinator, name, description),
        AquariumLufttemperaturSensor(coordinator, name, description),
    ])

# ============================================================
# 2. KOORDINATOR – Daten regelmäßig vom Gerät holen
# ============================================================
class AquaelDataUpdateCoordinator(DataUpdateCoordinator):
    """Koordiniert die Kommunikation mit dem Thermometer."""

    def __init__(self, hass, ip, name, interval):
        super().__init__(
            hass,
            _LOGGER,
            name=f"Aquael Thermometer ({name})",
            update_interval=timedelta(seconds=interval),
        )
        self.ip = ip

    async def _async_update_data(self):
        url = f"http://{self.ip}/readADC"
        try:
            async with async_timeout.timeout(10):
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as resp:
                        data = await resp.json(content_type=None)
                        _LOGGER.debug("Empfangene Daten von %s: %s", self.ip, data)
                        return data
        except Exception as err:
            _LOGGER.error("Fehler beim Abrufen der Daten von %s: %s", self.ip, err)
            return {}

# ============================================================
# 3. SENSOR: Wassertemperatur
# ============================================================
class AquariumWassertemperaturSensor(CoordinatorEntity, SensorEntity):
    """Sensor für die Wassertemperatur."""

    def __init__(self, coordinator, name, description):
        super().__init__(coordinator)
        self._attr_name = f"{name} Wassertemperatur"
        self._attr_unique_id = f"{name.lower().replace(' ', '_')}_wassertemperatur"
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
        self._attr_extra_state_attributes = {
            "Beschreibung": description,
            "IP": coordinator.ip,
        }

    @property
    def state(self):
        """Liefert den aktuellen Temperaturwert als float."""
        try:
            val = self.coordinator.data.get("Data")
            return float(val) if val is not None else None
        except Exception as e:
            _LOGGER.warning("Fehler beim Konvertieren der Wassertemperatur: %s", e)
            return None

# ============================================================
# 4. SENSOR: Lufttemperatur
# ============================================================
class AquariumLufttemperaturSensor(CoordinatorEntity, SensorEntity):
    """Sensor für die Lufttemperatur."""

    def __init__(self, coordinator, name, description):
        super().__init__(coordinator)
        self._attr_name = f"{name} Lufttemperatur"
        self._attr_unique_id = f"{name.lower().replace(' ', '_')}_lufttemperatur"
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
        self._attr_extra_state_attributes = {
            "Beschreibung": description,
            "IP": coordinator.ip,
        }

    @property
    def state(self):
        """Liefert den aktuellen Temperaturwert als float."""
        try:
            val = self.coordinator.data.get("Data2")
            return float(val) if val is not None else None
        except Exception as e:
            _LOGGER.warning("Fehler beim Konvertieren der Lufttemperatur: %s", e)
            return None
