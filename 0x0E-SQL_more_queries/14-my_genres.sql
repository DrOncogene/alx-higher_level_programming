-- list genres for show Dexter
SELECT DISTINCT tv_genres.name
  FROM tv_genres INNER JOIN tv_show_genres AS genres LEFT JOIN tv_shows
    ON tv_genres.id = genres.genre_id
 WHERE tv_shows.title = 'Dexter'

 ORDER BY tv_genres.name;
