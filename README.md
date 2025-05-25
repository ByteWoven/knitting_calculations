# 🧶 Home Assistant Knitting Calculations

This custom integration for Home Assistant provides simple, automated knitting calculations, built to make knitting projects easier.

This project started as a hobby because my girlfriend frequently asked me to do these  calculations for her.

## ✨ Features

* **Gauge Input**: Set your gauge swatch measurements (stitches and CM).
* **Stitches to Width Calculation**: Determine the width of your knitted fabric based on a desired stitch count.
* **Width to Stitches Calculation**: Calculate the number of stitches needed for a desired fabric width.
* **Instant Updates**: All calculations update in real-time as you adjust your input values.

## 🚀 Installation via HACS (Recommended)

This integration is available via HACS (Home Assistant Community Store), making installation and updates straightforward.

1.  **Ensure you have HACS installed**: Follow the official [HACS installation guide](https://hacs.xyz/docs/setup/install/).
2.  **Add this repository to HACS**:
    * In Home Assistant, go to **HACS** in the sidebar.
    * Navigate to **Integrations**.
    * Click the **three dots** in the top right corner and select **"Custom repositories"**.
    * Enter the URL of this GitHub repository: `https://github.com/ByteWoven/knitting_calculations`.
    * Select **"Integration"** as the category.
    * Click **"Add"**.
3.  **Install the integration**:
    * After adding the repository, search for "Knitting Calculations" in HACS under **Integrations**.
    * Click on the "Knitting Calculations" integration.
    * Click **"Download"** and follow the prompts.
4.  **Restart Home Assistant**: Go to **Settings > System > Restart** to fully load the new integration.

## ⚙️ Entities

Once installed and Home Assistant restarted, the following entities will be available:

### Input Entities

* `number.knitting_calculations_desired_width` (`Desired Width`)
* `number.knitting_calculations_desired_stitches` (`Desired Stitches`)
* `number.knitting_calculations_gauge_cm` (`Gauge CM`)
* `number.knitting_calculations_gauge_stitches` (`Gauge Stitches`)

### Output Entities

* `sensor.knitting_calculations_calculated_stitches` (`Calculated Stitches`)
* `sensor.knitting_calculations_calculated_width` (`Calculated Width`)

## 📊 Lovelace Dashboard Usage (Example)

```yaml
title: Breiberekeningen
icon: mdi:sheep
path: breiberekeningen
cards:
  - type: markdown
    content: |
      # Breiberekeningen

      Welkom bij je persoonlijke breiberekenaar!

      Pas de invoerwaarden aan en zie direct de berekende resultaten voor je
      breiwerk.
  - type: entities
    title: Jouw Stekenproef
    show_header_toggle: false
    entities:
      - entity: number.knitting_calculations_gauge_cm
        name: Stekenproef CM
      - entity: number.knitting_calculations_gauge_stitches
        name: Stekenproef Steken
  - type: horizontal-stack
    cards:
      - type: vertical-stack
        cards:
          - type: markdown
            content: >
              ## Breedte naar Steken

              Voer de gewenste breedte in (in cm) en zie hoeveel steken je nodig
              hebt.
          - type: entities
            title: Invoer
            show_header_toggle: false
            entities:
              - entity: number.knitting_calculations_desired_width
                name: Gewenste Breedte
          - type: entities
            title: Resultaat
            show_header_toggle: false
            entities:
              - entity: sensor.knitting_calculations_calculated_stitches
                name: Berekende Steken
      - type: vertical-stack
        cards:
          - type: markdown
            content: >
              ## Steken naar Breedte

              Voer het gewenste aantal steken in en zie hoe breed je breiwerk
              dan wordt.
          - type: entities
            title: Invoer
            show_header_toggle: false
            entities:
              - entity: number.knitting_calculations_desired_stitches
                name: Gewenste Steken
          - type: entities
            title: Resultaat
            show_header_toggle: false
            entities:
              - entity: sensor.knitting_calculations_calculated_width
                name: Berekende Breedte