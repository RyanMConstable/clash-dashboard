# Clash-Dashboard
This is a project I created for my own personal knowledge. Use it however you would like just note it does utilize your own personal JWT from the clash of clans API.

# Setup
Install Docker and Docker Compose! 

1) Put your official clash of clans api token into the .env file
2) Make sure port 80 is available on your local computer
3) Run docker-compose build
4) Run docker-compose up -d
5) You can now visit the frontend in the browser

# Status
The database is in a workable state, player and clan history are recorded every 15 minutes and recorded. The UI boots up and is able to create a user row in the signup table.

# Goal
- Make an easy to setup fully fleshed out clash of clans dashboard with real time texting alerts.

- Gain more experience with Docker, Kubernetes, GitHub Actions, Git, Python, FastAPI, and React.

# TO DO
- Have to add cron checking and python script for war monitoring and twilio texting in real time
- Make the frontend signup more pretty, include checking for password length, error if the user exists or the otp is wrong, and add twilio phone verification to make sure that number exists.
- Create kubernetes cluster
- Add argocd to kubernetes cluster
