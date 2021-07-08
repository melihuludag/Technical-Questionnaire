#v_table corresponds main data 


SELECT * FROM v_table

#Create a table that called 'Median_Table' and contains all groups' median

CREATE TABLE Median_Table
AS
	SELECT 
		median_group, AVG(daily_vaccinations) AS median
	FROM    
	   (SELECT 
		@row_number:=CASE
			WHEN @median_group = country THEN @row_number + 1
			ELSE 1
		END AS count_of_group,
		@median_group:=country AS median_group,
		country,
		daily_vaccinations,
		(SELECT 
				COUNT(*)
			FROM
				v_table
			WHERE
				a.country = country) AS total_of_group
		FROM
			(SELECT country, daily_vaccinations
		FROM
			v_table
		ORDER BY country , daily_vaccinations) AS a) b
	WHERE
		count_of_group BETWEEN total_of_group / 2.0 AND total_of_group / 2.0 + 1
	GROUP BY median_group;
  
 
#Alter the null cells with Median_Table
  
Update v_table
SET daily_vaccinations = (
	SELECT median 
	From Median_Table 
  Where v_table.country = Median_Table.median_group)
WHERE daily_vaccinations IS null;
