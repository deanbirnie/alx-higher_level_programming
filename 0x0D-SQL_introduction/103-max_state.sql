-- Displays the max temperature of each state ordered by state name
-- Import into "hbtn_0c_0" "temperatures" from "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql"
SELECT state, MAX(value) AS max_temp
FROM hbtn_0c_0.temperatures
GROUP BY state
ORDER BY state;
