-- list all comedy shows
SELECT shows.title
  FROM tv_shows AS shows
  	INNER JOIN tv_show_genres AS genres
	INNER JOIN tv_genres
    ON shows.id = genres.show_id AND genres.genre_id = tv_genres.id
 WHERE tv_genres.name = 'Comedy'
ORDER BY shows.title;
