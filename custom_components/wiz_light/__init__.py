"""WiZ Light integration."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


from .const import DOMAIN


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the WiZ component."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "light")
    )

    return True
