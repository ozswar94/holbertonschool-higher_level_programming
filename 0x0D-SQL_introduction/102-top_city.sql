-- Temperatures 1
SELECT city, AVG(value)'avg_temp' FROM `temperatures` WHERE month >= 7 AND month <= 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
