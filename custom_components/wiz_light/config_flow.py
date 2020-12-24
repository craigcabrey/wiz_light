import voluptuous as vol

from homeassistant.const import CONF_HOST, CONF_NAME
from homeassistant import config_entries
from .const import DOMAIN
from .light import WizBulb, wizlight


class LightConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            light = WizBulb(
                wizlight(user_input[CONF_HOST]),
                user_input[CONF_NAME],
            )

            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_NAME): str,
                vol.Required(CONF_HOST): str,
            }),
            errors=errors,
        )
