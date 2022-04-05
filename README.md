# Webex API Report Downloader

## Purpose

This CLI application was created to demonstrate how someone can use the Webex APIs to create and download a report.  The reason this demo was created is because some users find it confusing that the reports that are scheduled in Control Hub do not show up in the list of available reports from the API query.  **The only reports that can be downloaded via the API are reports that were created via API.**

## How to use this code

> There is an assumption that you understand Python and virtual environments. 

> I also assume you've created a Webex Integration and have the `App ID` and `Secret`.

> Webex Integration needed the `analytics:read_all` scope. 

1. git clone this repo. 
1. Setup your virtual environment using the tools you're accustomed too. 
1. `pip install -r requirements.txt`
1. Modify the code in `downloader.py` under the `_report_creation` function to have your start date, end date and Webex instance.  
1. Modify the code in `.env` to have your application ID and secret. 
1. `python app.py`
1. Copy the URL provided by the CLI.
1. Authenticate to Webex and grant your application the permissions asked. 
1. Copy the `localhost` URL in your browser and paste it back into the CLI. 
1. Select #2 for "Details" Template.
1. The application will now create the report and wait for the status of the report to be `done`.
1. Once the status is done, the application will now download the report and place it in the `files` directory. 


## What you should see as an output
```c
(py_webex_report_downloader) ➜  py_webex_report_downloader python3 app.py
Please go here and authorize: https://webexapis.com/v1/authorize?response_type=code&client_id=**Omitted**redirect_uri=https%3A%2F%2Flocalhost%3A8080%2Fwebex-teams-auth.html&scope=spark%3Akms+meeting%3Aadmin_schedule_read+analytics%3Aread_all&state=**Omitted**
Paste the full redirect URL here:https://localhost:8080/webex-teams-auth.html?code=**Omitted**
Template Title: Active Hosts, Template ID: 1
Template Title: Details, Template ID: 2
Template Title: Attendees, Template ID: 3
Template Title: Inactive Users, Template ID: 4
Template Title: Usage Summary, Template ID: 202
Template Title: Attendee Quality, Template ID: 10
Template Title: Audio Usage, Template ID: 20
Template Title: Future Schedules, Template ID: 300
Template Title: High CPU, Template ID: 301
Template Title: Enterprise Agreement, Template ID: 2020
Template Title: Active User Rolling Average, Template ID: 2019
Template Title: License Consumption, Template ID: 320
Template Title: User Activity, Template ID: 114
Template Title: Bots Activity, Template ID: 5
Template Title: User Activity Summary, Template ID: 115
Template Title: Bots Activity Summary, Template ID: 303
Template Title: Engagement Report, Template ID: 116
Template Title: Quality Report, Template ID: 117
Template Title: Calling Detailed Call History, Template ID: 500
Template Title: User Activation and License Details, Template ID: 400
Template Title: APP Version, Template ID: 120
Template Title: Rooms and Desks Detail, Template ID: 410
Template Title: Webex Assistant Usage, Template ID: 310
Which Template ID would you like to run? 2
Report status: waiting, checking in 30 seconds...
Report status: manual_processing, checking in 30 seconds...
Report status: manual_processing, checking in 30 seconds...
Report status: manual_processing, checking in 30 seconds...
Report status: manual_processing, checking in 30 seconds...
Report status: manual_processing, checking in 30 seconds...
Report status: manual_processing, checking in 30 seconds...
Report status: manual_processing, checking in 30 seconds...
Report status: done, checking in 30 seconds...
Done: 204
(py_webex_report_downloader) ➜  py_webex_report_downloader
```

## Notes

This is for demonstration purposes only.  As of now this is only written to show how to download the `Meeting Details` report (Report Template #2).  
