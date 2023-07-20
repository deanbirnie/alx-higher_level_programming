-- Displays the average temperature by city orderd by temperature
-- database imported into "hbtn_0c_0" "temperatures" from "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql"
SELECT city, AVG(value) AS avg_temp
FROM hbtn_0c_0.temperatures
GROUP BY city
ORDER BY avg_temp DESC;
