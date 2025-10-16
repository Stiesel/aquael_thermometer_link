# Aquael Thermometer Link

**Version 1.0.0**

Aquael Thermometer Link is a Home Assistant integration for reading water and air temperature from Aquael devices via local HTTP API.

## Features

- Reads data from `/readADC` endpoint  
- Creates two sensors per device:
  - Water temperature (`sensor.<name>_wassertemperatur`)
  - Air temperature (`sensor.<name>_lufttemperatur`)
- Local communication, no cloud
- Adjustable update interval

## Installation via HACS

1. Add the repository in HACS → “Custom repositories”
2. Search for “Aquael Thermometer Link”
3. Install the integration
4. Restart Home Assistant
5. Go to *Settings → Devices & Services → Add Integration → Aquael Thermometer Link*

## Configuration

- Enter IP address of your Aquael Thermometer
- Define name and interval (default: 60 seconds)

## Author

**GitHub:** [https://github.com/Stiesel/aquael_thermometer_link](https://github.com/Stiesel/aquael_thermometer_link)
