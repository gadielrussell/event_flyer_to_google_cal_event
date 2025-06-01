from PIL import Image
import pytesseract
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

windows_user_name = '' # Change this to your Windows Username or update path below as appropriate
google_api_oath_credentials_json_file_path = f'C:\\Users\\{windows_user_name}\\Downloads\\credentials.json'

# Example Flyer - https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F968394353%2F18644285781%2F1%2Foriginal.20250224-223403?crop=focalpoint&fit=crop&w=940&auto=format%2Ccompress&q=75&sharp=10&fp-x=0.154066606001&fp-y=0.546298411355&s=7331f8730fc77d8072ae76caa2c7dcea
# Retrieved from Event - https://www.eventbrite.com/e/jogs-las-vegas-gem-mineral-and-jewelry-show-2025-tickets-1252374508869?aff=ebdssbcitybrowse
event_flyer_image_path = f'C:\\Users\\{windows_user_name}\\Downloads\\lv_gem_mineral_show_20250604.png'

# Parse Text from Image
event_text = pytesseract.image_to_string(Image.open(event_flyer_image_path))
print(event_text)

# Scopes required for inserting events from Google Calendar Docs: Event QuickAdd
# https://developers.google.com/workspace/calendar/api/v3/reference/events/quickAdd
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

# Since this API request requires Authentication, we need to get an OAuth 2.0 Authentication Token
# You also need to download a credential file to successfully make API calls.
flow = InstalledAppFlow.from_client_secrets_file(google_api_oath_credentials_json_file_path, SCOPES)
creds = flow.run_local_server(port=0) # This will open an OAuth Authentication Window

# Build the Google Calendar Service
service = build('calendar', 'v3', credentials=creds)

# Use the Google Calendar QuickAdd event, to quickly add an event using text.
# Google uses a Large Language Model (LLM) to parse the text that you send to extract event info like name, date, time, etc.
# See Google Documentation on the various Events they expose through the API
# https://developers.google.com/workspace/calendar/api/v3/reference/events
calendar_id = 'primary'  # or your calendar's email address
event = service.events().quickAdd(calendarId=calendar_id, text=event_text).execute()
event_calendar_link = event.get('htmlLink')
print(f'Event created: {event_calendar_link}')

# References
# "Calendar API" GitHub, https://googleapis.github.io/google-api-python-client/docs/dyn/calendar_v3.htmlLinks. Accessed 1 June 2025.
# "JOGS Las Vegas Gem, Mineral and Jewelry Show 2025" Eventbrite, https://www.eventbrite.com/e/jogs-las-vegas-gem-mineral-and-jewelry-show-2025-tickets-1252374508869Links. Accessed 1 June 2025.
# "Tesseract at UB Mannheim" GitHub, https://github.com/UB-Mannheim/tesseract/wikiLinks. Accessed 1 June 2025.
# "Tesseract (Software)" Wikipedia, https://en.wikipedia.org/wiki/Tesseract_(software). Accessed 1 June 2025.
# "Python Tesseract" GitHub,  https://github.com/h/pytesseractLinks. Accessed 1 June 2025.
# "Python Quickstart" Google Calendar Developer Documentation, https://developers.google.com/workspace/calendar/api/quickstart/pythonLinks. Accessed 1 June 2025.