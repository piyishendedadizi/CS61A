CREATE table newest AS
  SELECT title, year
  FROM titles
  ORDER BY year DESC
  LIMIT 10;


CREATE table dog_movies AS 
  SELECT titles.title, principals.character
  FROM titles JOIN principals ON titles.tconst = principals.tconst
  WHERE principals.character LIKE "%dog%";


CREATE table leads AS 
  SELECT names.name, count(*) AS lead_roles
  FROM principals JOIN names ON principals.nconst = names.nconst
  WHERE principals.ordering = 1
  GROUP BY names.nconst
  HAVING count(*) > 10;


CREATE table long_movies AS 
  SELECT ((year / 10) * 10) || "s" AS decade, count(*) AS count
  FROM titles
  WHERE runtime > 180
  GROUP BY year / 10;


