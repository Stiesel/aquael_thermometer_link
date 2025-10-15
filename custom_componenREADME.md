# Aquael Thermometer Link

## Produktbeschreibung

**Aquael Thermometer Link** ist eine Home Assistant Integration, die es ermöglicht, Wassertemperatur und Lufttemperatur von mehreren Aquael Thermometer Geräten direkt und komfortabel in Home Assistant einzubinden. Über eine intuitive Benutzeroberfläche können beliebig viele Geräte (IP-Adressen) hinzugefügt werden. Für jedes Gerät lassen sich Name, Beschreibung und das Abfrageintervall individuell einstellen. Die Integration ist einfach über HACS installierbar und bietet echte Sensor-Entitäten für die einfache Nutzung in Automationen, Dashboards und Benachrichtigungen.

---

## English Description

**Aquael Thermometer Link** is a Home Assistant integration that allows you to conveniently connect water and air temperature sensors from multiple Aquael Thermometer devices directly to Home Assistant. Using an intuitive user interface, you can add any number of devices (IP addresses). For each device, you can set the sensor name, description, and polling interval individually. The integration is easy to install via HACS and provides true sensor entities for seamless use in automations, dashboards, and notifications.

---

## 🇩🇪 Deutsch – Installation & Einrichtung

1. **Installiere das Addon über HACS**  
   - Füge dein GitHub-Repository als „Custom Repository“ zu HACS hinzu.
   - Installiere „Aquael Thermometer Link“.

2. **Integration hinzufügen**  
   - Gehe in Home Assistant zu „Integrationen“ > „Integration hinzufügen“.
   - Wähle „Aquael Thermometer Link“ aus.

3. **Gerät konfigurieren**  
   - Gib die IP-Adresse des Geräts ein.
   - Wähle einen Namen für das Aquarium/Sensor und optional eine Beschreibung.
   - Stelle das gewünschte Abfrageintervall ein.

4. **Mehrere Geräte möglich**  
   - Wiederhole die Schritte, um weitere Geräte hinzuzufügen.

5. **Sensoren nutzen**  
   - Die Wassertemperatur- und Lufttemperatur-Sensoren erscheinen als Entitäten (`sensor.<name>_wassertemperatur`, `sensor.<name>_lufttemperatur`).

---

## 🇬🇧 English – Installation & Setup

1. **Install the addon via HACS**  
   - Add your GitHub repository as a "Custom Repository" in HACS.
   - Install "Aquael Thermometer Link".

2. **Add integration**  
   - In Home Assistant, go to "Integrations" > "Add Integration".
   - Choose "Aquael Thermometer Link".

3. **Configure device**  
   - Enter the device's IP address.
   - Choose a name for the aquarium/sensor and optionally add a description.
   - Set the desired polling interval.

4. **Multiple devices supported**  
   - Repeat the steps to add more devices.

5. **Using the sensors**  
   - Water temperature and air temperature sensors will appear as entities (`sensor.<name>_wassertemperatur`, `sensor.<name>_lufttemperatur`).

---

## Hinweise / Notes

- **Nur Wassertemperatur und Lufttemperatur werden unterstützt.**
- Keine weiteren Sensortypen oder Steuerfunktionen enthalten.
- Die Integration ist für Aquael-Thermometer mit REST-API ausgelegt (z.B. `/readADC`).

---

**GitHub:** [Dein Repository-Link](https://github.com/Stiesel/aquael_thermometer_link)  
**Autor / Author:** [Stiesel](https://github.com/Stiesel)
