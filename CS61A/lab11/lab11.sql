CREATE table newest AS
  SELECT title, year from titles order by year desc limit 10;


CREATE table dog_movies AS 
  SELECT title, character from titles inner join principals on titles.tconst = principals.tconst where character like "%dog%";


CREATE table leads AS 
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE table long_movies AS 
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

