# Event Flyer to Google Calendar Event
An exploratory script that uses Tesseract Optical Character Recognition (OCR) to parse words from an Event Flyer and then uses Google Calendar API to create a calendar event with that information.

# Pre-Requisites

## Google Calendar API Key
A Google Calendar OAuth 2.0 Client credential (API Key, ClientID, and Client Secret) is required for API calls that add calendar events to work. A Google Developer account, along with a Project and API Key, OAuth 2.0 Client can be created here: https://console.cloud.google.com.

## Tesseract Optical Character Recognition (OCR) 
Tesseract OCR needs to be installed on the machine that is hosting this service. Additionally a `TESSDATA_PREFIX` environment variable needs to be set that includes the location of the Tesseract install directory. Information on Tesseract can be found here https://github.com/UB-Mannheim/tesseract/wikiLinks.

# Required Python Packages

- **Pillow** – for image handling (from PIL import Image)
- **pytesseract** – wrapper for Tesseract OCR
- **google-auth** – for handling credentials
- **google-auth-oauthlib** – for OAuth 2.0 flow
- **google-api-python-client** – for accessing the Google Calendar API

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
