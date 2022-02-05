-- list all shows and associated genres
SELECT DISTINCT shows.title, genres.name
  FROM tv_genres AS genres
  	INNER JOIN tv_show_genres AS show_genres
  	RIGHT JOIN tv_shows AS shows
    ON genres.id = show_genres.genre_id AND shows.id = show_genres.show_id
ORDER BY shows.title, genres.name;
