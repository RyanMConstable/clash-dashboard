CREATE TABLE IF NOT EXISTS userinfo (
  id SERIAL PRIMARY KEY, playertag VARCHAR(15) NOT NULL, phonenumber VARCHAR(10) NOT NULL, passwd VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS playerwarattacks (
  id VARCHAR(75) PRIMARY KEY, townhalllevel INTEGER, mapposition INTEGER, tag VARCHAR(15), defendertag VARCHAR(15), stars INTEGER, destructionpercentage FLOAT, ordernum INTEGER, duration INTEGER, clantag VARCHAR(15), time TIMESTAMP, enemytownhalllevel INTEGER, enemymapposition INTEGER, eloChange FLOAT
);

CREATE TABLE IF NOT EXISTS clanwars (
	id VARCHAR(50) PRIMARY KEY, teamSize INTEGER, attacksPerMember INTEGER, battleModifier VARCHAR(35), clanLevel INTEGER, attacks INTEGER, stars INTEGER, destructionPercentage FLOAT, enemyClanLevel INTEGER, enemyAttacks INTEGER, enemyStars INTEGER, enemyDestructionPercentage FLOAT, enemyTag VARCHAR(15), clantag VARCHAR(15), time TIMESTAMP, preperationstarttime VARCHAR(25), starttime VARCHAR(25), endtime VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS playerhistory (
  id SERIAL PRIMARY KEY, time TIMESTAMP NOT NULL, playertag VARCHAR(15) NOT NULL, townhalllevel INTEGER, townhallweaponlevel INTEGER, explevel INTEGER, trophies INTEGER, besttrophies INTEGER, warstars INTEGER, attackwins INTEGER, defensewins INTEGER, builderhalllevel INTEGER, builderbasetrophies INTEGER, bestbuilderbasetrophies INTEGER, role VARCHAR(15), warpreference VARCHAR(5), donations INTEGER, donationsreceived INTEGER, clancapitalcontributions INTEGER, league VARCHAR(30), builderleague VARCHAR(30), clantag VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS clanhistory (
  id SERIAL PRIMARY KEY, time TIMESTAMP NOT NULL, clantag VARCHAR(15) NOT NULL, description VARCHAR(255), clanlevel INTEGER, clanpoints INTEGER, clanbuilderbasepoints INTEGER, clancapitalpoints INTEGER, capitalleague VARCHAR(30), warwinstreak INTEGER, warwins INTEGER, warties INTEGER, warlosses INTEGER, warleague VARCHAR(30), members INTEGER, location VARCHAR(30), requiredtrophies INTEGER
);

CREATE TABLE IF NOT EXISTS clanlist (
  clantag VARCHAR(15) PRIMARY KEY, clanname VARCHAR(100), badgeurl VARCHAR(200), warstatus VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS playerlist (
  playertag VARCHAR(15) PRIMARY KEY, clantag VARCHAR(100), playername VARCHAR(50)
);
