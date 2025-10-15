import voluptuous as vol
from homeassistant import config_entries

class AquaelThermometerLinkConfigFlow(config_entries.ConfigFlow, domain="aquael_thermometer_link"):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(
                title=user_input["name"],
                data=user_input
            )
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ip_address", default="192.168.2.110"): str,
                vol.Required("name", default="Aquarium"): str,
                vol.Optional("description", default=""): str,
                vol.Required("scan_interval", default=600): int
            }),
            errors=errors,
        )