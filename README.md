# Clash-Dashboard
This is a project I created for my own personal knowledge. Use it however you would like just note it does utilize your own personal JWT from the clash of clans API.

# Status
CURRENTLY A WORK IN PROGRESS!

# Goal
1) Make an easy to setup fully fleshed out clash of clans dashboard with real time texting alerts.

2) Gain more experience with Docker, Kubernetes, GitHub Actions, Git, Python, FastAPI, and React.

# TO DO
1) Figure out how to run the cron container as a cron, the clash API doesn't enable webhooks or websockets so we have to use polling
2) Have to add cron checking and python script for war monitoring and twilio texting in real time
3) Make the frontend signup more pretty, include checking for password length, error if the user exists or the otp is wrong, and add twilio phone verification to make sure that number exists.
