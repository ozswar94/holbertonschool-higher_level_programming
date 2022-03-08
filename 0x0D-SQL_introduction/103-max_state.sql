-- Temperatures 2
SELECT state, MAX(value)'max_tmp' FROM `temperatures` GROUP BY state ORDER BY state;
