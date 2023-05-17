-- query list all genres from hbtn_0d_tvshows and displays
-- number of shows linked to each
SELECT tv_show_genres.name AS genre, COUNT(tv_shows_genres.genre_id) AS number_of_shows FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
