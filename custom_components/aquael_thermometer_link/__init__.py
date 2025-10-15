async def async_setup_entry(hass, entry):
    hass.async_create_task(
        hass.helpers.forward.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass, entry):
    return await hass.helpers.forward.async_forward_entry_unload(entry, "sensor")
