-- list genres for show Dexter
SELECT DISTINCT tv_genres.name
  FROM tv_genres INNER JOIN tv_show_genres AS genres
    ON tv_genres.id = genres.genre_id
 WHERE genres.show_id = (
		 SELECT id
		   FROM tv_shows
		  WHERE title = 'Dexter')

 ORDER BY tv_genres.name;
