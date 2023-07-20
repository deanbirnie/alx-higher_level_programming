-- Displays the top 3 of cities temperatures during July and August ordered by temperature
-- Import into "hbtn_0c_0" "temperatures" from "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql"
SELECT city, AVG(value) AS avg_temp
FROM hbtn_0c_0.temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
