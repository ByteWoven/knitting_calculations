"""Knitting Calculations number platform."""
import logging
from homeassistant.components.number import NumberEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType = None,
) -> None:
    """Set up the Knitting Calculations number platform."""
    _LOGGER.debug("Setting up Knitting Calculations number platform")
    add_entities([
        DesiredWidthNumber(hass),
        DesiredStitchesNumber(hass),
        GaugeStitchesNumber(hass),
        GaugeCMNumber(hass)
    ])

class DesiredWidthNumber(NumberEntity):
    """Representation of the desired width number."""

    _attr_name = "Desired Width"
    _attr_native_min_value = 0.0
    _attr_native_max_value = 500.0
    _attr_native_step = 1.0
    _attr_native_unit_of_measurement = "cm"
    _attr_icon = "mdi:ruler"

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the desired width number."""
        self._hass = hass
        self._width = 120.0
        self._attr_unique_id = "knitting_calculations_desired_width"

    @property
    def native_value(self) -> float:
        """Return the current desired width."""
        return self._width

    async def async_set_native_value(self, value: float) -> None:
        """Update the current desired width."""
        self._width = value
        self.async_write_ha_state()
        _LOGGER.debug(f"Desired width set to: {value} cm")


class DesiredStitchesNumber(NumberEntity):
    """Representation of the desired stitches number."""

    _attr_name = "Desired Stitches"
    _attr_native_min_value = 0.0
    _attr_native_max_value = 500.0
    _attr_native_step = 1.0
    _attr_native_unit_of_measurement = "steken"
    _attr_icon = "mdi:ruler"

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the desired stitches number."""
        self._hass = hass
        self._stitches = 80.0
        self._attr_unique_id = "knitting_calculations_desired_stitches"

    @property
    def native_value(self) -> float:
        """Return the current desired stitches."""
        return self._stitches

    async def async_set_native_value(self, value: float) -> None:
        """Update the current desired stitches."""
        self._stitches = value
        self.async_write_ha_state()
        _LOGGER.debug(f"Desired stitches set to: {value} steken")


class GaugeStitchesNumber(NumberEntity):
    """Representation of the gauge stitches number."""

    _attr_name = "Gauge Stitches"
    _attr_native_min_value = 1.0
    _attr_native_max_value = 50.0
    _attr_native_step = 1.0
    _attr_native_unit_of_measurement = "steken"
    _attr_icon = "mdi:ruler-square"

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the gauge stitches number."""
        self._hass = hass
        self._stitches = 16.0
        self._attr_unique_id = "knitting_calculations_gauge_stitches"

    @property
    def native_value(self) -> float:
        """Return the current gauge stitches."""
        return self._stitches

    async def async_set_native_value(self, value: float) -> None:
        """Update the current gauge stitches."""
        self._stitches = value
        self.async_write_ha_state()
        _LOGGER.debug(f"Stekenproef steken ingesteld op: {value}")


class GaugeCMNumber(NumberEntity):
    """Representation of the gauge centimeters number."""

    _attr_name = "Gauge CM"
    _attr_native_min_value = 1.0
    _attr_native_max_value = 20.0
    _attr_native_step = 0.5
    _attr_native_unit_of_measurement = "cm"
    _attr_icon = "mdi:ruler-square"

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the gauge cm number."""
        self._hass = hass
        self._cm = 10.0
        self._attr_unique_id = "knitting_calculations_gauge_cm"

    @property
    def native_value(self) -> float:
        """Return the current gauge cm."""
        return self._cm

    async def async_set_native_value(self, value: float) -> None:
        """Update the current gauge cm."""
        self._cm = value
        self.async_write_ha_state()
        _LOGGER.debug(f"Stekenproef CM ingesteld op: {value} cm")