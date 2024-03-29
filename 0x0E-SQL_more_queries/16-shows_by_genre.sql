-- query lists all shows and genres linked to that shows from
-- database
SELECT
    tv_shows.title AS title, tv_genres.name AS name FROM tv_show_genres
    RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    ORDER BY title, name;
