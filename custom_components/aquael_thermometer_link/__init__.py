import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Aquael Thermometer Link integration."""
    _LOGGER.debug("Setting up Aquael Thermometer Link for %s", entry.data.get("name"))
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Aquael Thermometer Link integration."""
    _LOGGER.debug("Unloading Aquael Thermometer Link for %s", entry.data.get("name"))
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"]) 
