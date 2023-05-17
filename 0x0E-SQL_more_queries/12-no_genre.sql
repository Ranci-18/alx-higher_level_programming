-- query lists shows in hbtn_0d_tvshows without genre linked
-- by title and genre_id in asc
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;