-- Temperatures 2
SELECT state, MAX(value)'max_temp' FROM `temperatures` GROUP BY state ORDER BY state;
