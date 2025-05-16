CREATE TABLE IF NOT EXISTS userinfo (
  id SERIAL PRIMARY KEY, playertag VARCHAR(15) NOT NULL, phonenumber VARCHAR(10) NOT NULL, passwd VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS playerwarattacks (
  id SERIAL PRIMARY KEY, playertag VARCHAR(15) NOT NULL, clantag VARCHAR(15) NOT NULL, time TIMESTAMP NOT NULL, defendertag VARCHAR(15) NOT NULL, stars VARCHAR(1), destructionpercentage VARCHAR(5), theorder VARCHAR(5), duration VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS clanwars (
  id PRIMARY KEY, INTEGER teamSize, INTEGER attacksPerMember, VARCHAR(35) battleModifier, INTEGER clanLevel, INTEGER attacks, INTEGER stars, FLOAT destructionPercentage, INTEGER enemyClanLevel, INTEGER enemyAttacks, INTEGER enemyStars, FLOAT enemyDestructionPercentage, VARCHAR(15) enemyTag
);

CREATE TABLE IF NOT EXISTS playerhistory (
  id SERIAL PRIMARY KEY, time TIMESTAMP NOT NULL, playertag VARCHAR(15) NOT NULL, townhalllevel INTEGER, townhallweaponlevel INTEGER, explevel INTEGER, trophies INTEGER, besttrophies INTEGER, warstars INTEGER, attackwins INTEGER, defensewins INTEGER, builderhalllevel INTEGER, builderbasetrophies INTEGER, bestbuilderbasetrophies INTEGER, role VARCHAR(15), warpreference VARCHAR(5), donations INTEGER, donationsreceived INTEGER, clancapitalcontributions INTEGER, league VARCHAR(30), builderleague VARCHAR(30), clantag VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS clanhistory (
  id SERIAL PRIMARY KEY, time TIMESTAMP NOT NULL, clantag VARCHAR(15) NOT NULL, description VARCHAR(255), clanlevel INTEGER, clanpoints INTEGER, clanbuilderbasepoints INTEGER, clancapitalpoints INTEGER, capitalleague VARCHAR(30), warwinstreak INTEGER, warwins INTEGER, warties INTEGER, warlosses INTEGER, warleague VARCHAR(30), members INTEGER, location VARCHAR(30), requiredtrophies INTEGER
);

CREATE TABLE IF NOT EXISTS clanlist (
  id SERIAL PRIMARY KEY, clantag VARCHAR(15) NOT NULL
);
