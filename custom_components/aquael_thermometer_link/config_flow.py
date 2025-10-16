import re
import aiohttp
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

DOMAIN = "aquael_thermometer_link"

# IPv4 validation regex
IP_REGEX = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")


class AquaelThermometerLinkConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial setup step."""
        errors = {}

        if user_input is not None:
            ip_address = user_input["ip_address"].strip()

            # Validate IP format
            if not IP_REGEX.match(ip_address):
                errors["base"] = "invalid_ip"
            else:
                # Test connection
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f"http://{ip_address}/readADC", timeout=5) as resp:
                            if resp.status != 200:
                                errors["base"] = "cannot_connect"
                            else:
                                await resp.json(content_type=None)
                except Exception:
                    errors["base"] = "cannot_connect"

            if not errors:
                await self.async_set_unique_id(ip_address)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=user_input["name"],
                    data=user_input
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ip_address"): str,
                vol.Required("name", default="Aquarium"): str,
                vol.Optional("description", default=""): str,
                vol.Required("scan_interval", default=600): vol.All(int, vol.Range(min=10, max=3600))
            }),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return AquaelThermometerLinkOptionsFlowHandler(config_entry)


class AquaelThermometerLinkOptionsFlowHandler(config_entries.OptionsFlow):
    """Options flow for adjusting polling interval and description."""
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(
                    "scan_interval",
                    default=self.config_entry.data.get("scan_interval", 600)
                ): vol.All(int, vol.Range(min=10, max=3600)),
                vol.Optional(
                    "description",
                    default=self.config_entry.data.get("description", "")
                ): str
            })
        )
