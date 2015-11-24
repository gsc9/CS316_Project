DELETE FROM beers_alt_frequents;
DELETE FROM beers_alt_serves;
DELETE FROM beers_alt_likes;
DELETE FROM beers_alt_bar;
DELETE FROM beers_alt_beer;
DELETE FROM beers_alt_drinker;
INSERT INTO beers_alt_bar SELECT name, address FROM Bar;
INSERT INTO beers_alt_beer SELECT name, brewer FROM Beer;
INSERT INTO beers_alt_drinker SELECT name, address FROM Drinker;
INSERT INTO beers_alt_frequents(drinker, bar, times_a_week) SELECT drinker, bar, times_a_week FROM Frequents;
INSERT INTO beers_alt_serves(bar, beer, price) SELECT bar, beer, price FROM Serves;
INSERT INTO beers_alt_likes(drinker, beer) SELECT drinker, beer FROM Likes;