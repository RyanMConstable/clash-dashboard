# Clash-Dashboard
This is a completely self hosted clash of clans admin panel. Clash-Dashboard allows you to self host your own clash of clans dashboard panel. This panel shows the users statistics that were previously unknown. 

CURRENTLY A WORK IN PROGRESS --- USE WITH BUGS OR INCOMPLETION
# Setup
Install Docker and Docker Compose! 

1) Put your official clash of clans api token into the .env file
2) Make sure port 80 is available on your local computer
3) Run docker-compose build
4) Run docker-compose up -d
5) You can now visit the frontend in the browser

# Status
After setup there are currently graphs for the current wars (not including cwl) and a table of all users and their elo rankings calculated from previous clan war attacks (not including cwl)

# Goal
- Make an easy to setup fully fleshed out clash of clans dashboard with real time texting alerts.

- Gain more experience with Docker, Kubernetes, GitHub Actions, Git, Python, FastAPI, and React.

# TO DO
- Add logging, most likely another container with everything flowing into it
- Add TLS internal use
- Add proper authorization
- Add databases for cwl
- Countdown for war prep/war end (in progress)
- AI to predict who will win the war or odds for each clan winning
