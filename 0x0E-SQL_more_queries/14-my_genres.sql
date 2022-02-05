-- list genres for show Dexter
SELECT DISTINCT tv_genres.name
  FROM tv_genres
  	INNER JOIN tv_show_genres AS genres 
	INNER JOIN tv_shows AS shows
    ON tv_genres.id = genres.genre_id AND shows.id = genres.show_id
  WHERE shows.title = "Dexter"

 ORDER BY tv_genres.name;
