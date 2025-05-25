"""The Knitting Calculations integration."""
import logging

DOMAIN = "knitting_calculations"

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    """Set up the Knitting Calculations integration."""
    _LOGGER.debug("Setting up Knitting Calculations integration")
    return True