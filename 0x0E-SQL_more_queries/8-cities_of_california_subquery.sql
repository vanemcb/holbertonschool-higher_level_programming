-- Script that lists all the cities of
-- California that can be found in the database
SELECT id, name from cities where state_id = (SELECT id FROM states WHERE name = "California") ORDER BY cities.id;
