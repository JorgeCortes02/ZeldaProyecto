jugadores = "Select distinct  user_name, date_started from game;"

partidasxJugador = "Select user_name, count(*) from game group by user_name;"

ArmasUsuarios = "SELECT g.user_name AS Usuario, w.weapon_name AS Arma, COUNT(*) AS CantidadObtenida, MAX(g.date_started) AS FechaPartidaMasUsos FROM game g JOIN game_weapons w ON g.game_id = w.game_id GROUP BY g.user_name, w.weapon_name ORDER BY Usuario, CantidadObtenida DESC;"UPDATE game
mysql>  SELECT     g.user_name AS Usuario,     gf.food_name AS Alimento,     SUM(gf.quanntity_remaining) AS CantidadObtenida FROM     game g JOIN     game_food
gf ON g.game_id = gf.game_id GROUP BY     g.user_name, gf.food_name ORDER BY     Usuario, CantidadObtenida DESC;