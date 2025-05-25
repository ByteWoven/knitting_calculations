"""Knitting Calculations sensor platform."""
import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import STATE_UNKNOWN
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.event import async_track_state_change_event
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType = None,
) -> None:
    """Set up the Knitting Calculations sensor platform."""
    _LOGGER.debug("Setting up Knitting Calculations sensor platform")
    add_entities([
        CalculatedStitchesSensor(hass),
        CalculatedWidthSensor(hass)
    ])

class CalculatedStitchesSensor(SensorEntity):
    """Representation of the calculated stitches sensor."""

    _attr_name = "Calculated Stitches"
    _attr_icon = "mdi:ruler"
    _attr_native_unit_of_measurement = "steken"
    _attr_unique_id = "knitting_calculations_calculated_stitches"

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the sensor."""
        self._hass = hass
        self._state = None
        self._desired_width_entity_id = "number.desired_width"
        self._gauge_stitches_entity_id = "number.gauge_stitches"
        self._gauge_cm_entity_id = "number.gauge_cm"

        _LOGGER.debug(f"Sensor '{self._attr_name}' kijkt naar: {self._desired_width_entity_id}, {self._gauge_stitches_entity_id}, {self._gauge_cm_entity_id}")

    async def async_added_to_hass(self) -> None:
        """Register callbacks when the entity is added to Home Assistant."""
        self.async_on_remove(
            async_track_state_change_event(
                self._hass,
                [self._desired_width_entity_id, self._gauge_stitches_entity_id, self._gauge_cm_entity_id],
                self._async_input_state_change,
            )
        )
        await self._async_update_stitches()

    @callback
    async def _async_input_state_change(self, event) -> None:
        """Handle state changes of any of the input numbers for this sensor."""
        await self._async_update_stitches()

    async def _async_update_stitches(self) -> None:
        """Update the calculated stitches based on current input values."""
        desired_width_state = self._hass.states.get(self._desired_width_entity_id)
        gauge_stitches_state = self._hass.states.get(self._gauge_stitches_entity_id)
        gauge_cm_state = self._hass.states.get(self._gauge_cm_entity_id)

        if (desired_width_state and desired_width_state.state != STATE_UNKNOWN and
            gauge_stitches_state and gauge_stitches_state.state != STATE_UNKNOWN and
            gauge_cm_state and gauge_cm_state.state != STATE_UNKNOWN):
            try:
                desired_width = float(desired_width_state.state)
                gauge_stitches = float(gauge_stitches_state.state)
                gauge_cm = float(gauge_cm_state.state)

                if gauge_cm > 0:
                    calculated_stitches = (gauge_stitches / gauge_cm) * desired_width
                    self._state = round(calculated_stitches)
                    _LOGGER.debug(f"Sensor '{self._attr_name}' berekend: {self._state} steken voor {desired_width} cm, met stekenproef {gauge_stitches} op {gauge_cm} cm.")
                else:
                    self._state = None
                    _LOGGER.warning(f"Sensor '{self._attr_name}': Stekenproef CM is nul, kan steken niet berekenen.")
            except ValueError as e:
                self._state = None
                _LOGGER.error(f"Sensor '{self._attr_name}': Ongeldige input voor berekening: {e}.")
        else:
            self._state = None
            _LOGGER.debug(f"Sensor '{self._attr_name}': Eén of meer input entiteiten zijn niet gereed voor berekening.")

        self.async_write_ha_state()

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self._state


class CalculatedWidthSensor(SensorEntity):
    """Representation of the calculated width sensor."""

    _attr_name = "Calculated Width"
    _attr_icon = "mdi:ruler"
    _attr_native_unit_of_measurement = "cm"
    _attr_unique_id = "knitting_calculations_calculated_width"

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the sensor."""
        self._hass = hass
        self._state = None
        self._desired_stitches_entity_id = "number.desired_stitches"
        self._gauge_stitches_entity_id = "number.gauge_stitches"
        self._gauge_cm_entity_id = "number.gauge_cm"

        _LOGGER.debug(f"Sensor '{self._attr_name}' kijkt naar: {self._desired_stitches_entity_id}, {self._gauge_stitches_entity_id}, {self._gauge_cm_entity_id}")

    async def async_added_to_hass(self) -> None:
        """Register callbacks when the entity is added to Home Assistant."""
        self.async_on_remove(
            async_track_state_change_event(
                self._hass,
                [self._desired_stitches_entity_id, self._gauge_stitches_entity_id, self._gauge_cm_entity_id],
                self._async_input_state_change,
            )
        )
        await self._async_update_width()

    @callback
    async def _async_input_state_change(self, event) -> None:
        """Handle state changes of any of the input numbers for this sensor."""
        await self._async_update_width()

    async def _async_update_width(self) -> None:
        """Update the calculated width based on current input values."""
        desired_stitches_state = self._hass.states.get(self._desired_stitches_entity_id)
        gauge_stitches_state = self._hass.states.get(self._gauge_stitches_entity_id)
        gauge_cm_state = self._hass.states.get(self._gauge_cm_entity_id)

        if (desired_stitches_state and desired_stitches_state.state != STATE_UNKNOWN and
            gauge_stitches_state and gauge_stitches_state.state != STATE_UNKNOWN and
            gauge_cm_state and gauge_cm_state.state != STATE_UNKNOWN):
            try:
                desired_stitches = float(desired_stitches_state.state)
                gauge_stitches = float(gauge_stitches_state.state)
                gauge_cm = float(gauge_cm_state.state)

                if gauge_stitches > 0:
                    calculated_width = (gauge_cm / gauge_stitches) * desired_stitches
                    self._state = round(calculated_width, 1)
                    _LOGGER.debug(f"Sensor '{self._attr_name}' berekend: {self._state} cm voor {desired_stitches} steken, met stekenproef {gauge_stitches} op {gauge_cm} cm.")
                else:
                    self._state = None
                    _LOGGER.warning(f"Sensor '{self._attr_name}': Stekenproef Steken is nul, kan breedte niet berekenen.")
            except ValueError as e:
                self._state = None
                _LOGGER.error(f"Sensor '{self._attr_name}': Ongeldige input voor berekening: {e}.")
        else:
            self._state = None
            _LOGGER.debug(f"Sensor '{self._attr_name}': Eén of meer input entiteiten zijn niet gereed voor berekening.")

        self.async_write_ha_state()

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self._state