# Surf_up
SQLLite, VS Code, Jupyter Notebook and Flask

# Project Overview/Challenge
- Query data from SQLite database
- Determine key statistical data about the month of June.
- Determine key statistical data about the month of December.
- Compare the finding between the month of June and December.
- Make recommendations for further analysis.

# Reseources
- Data Source: hawaii.sqlite
- Software: Jupyter Notebook, Visual Studio Code, 1.40.2. Flask

# Summary
- Practice
	- Queried 2 year data for precipitation, station information and temperature from hawaii.sqlite data
		- the data was then used to create Flask app to present to investors.
- Challenge
	- Queried the data for month of June from hawaii.sqlite for all years, precipitations and temperature.
	- The queried data showed that the there is little precipitation and the tempretatures range from 64 degrees to 85 degrees.
	- The average temperature  in month of June is 74.9 degrees.  

|       | precipitation | temperature |
|-------|---------------|-------------|
| count | 1574.000000   | 1700.000000 |
| mean  | 0.136360      | 74.944118   |
| std   | 0.335731      | 3.257417    |
| min   | 0.000000      | 64.000000   |
| 25%   | 0.000000      | 73.000000   |
| 50%   | 0.020000      | 75.000000   |
| 75%   | 0.120000      | 77.000000   |
| max   | 4.430000      | 85.000000   |	


	- Queried the data for month of December from hawaii.sqlite for all years, precipitations and temperature.
	- The queried data showed that the there is little precipitation and the tempretatures range from 56 degrees to 83 degrees. 
	- The average temperature in month of December is 71 degrees.


|       | precipitation | temperature |
|-------|---------------|-------------|
| count | 1405.000000   | 1517.000000 |
| mean  | 0.216819      | 71.041529   |
| std   | 0.541399      | 3.745920    |
| min   | 0.000000      | 56.000000   |
| 25%   | 0.000000      | 69.000000   |
| 50%   | 0.030000      | 71.000000   |
| 75%   | 0.150000      | 74.000000   |
| max   | 6.420000      | 83.000000   |


	- Key differences between the June and December. 
		- There is more precipitation in December that in the month of June. However, the difference is not significant only 2.00 difference between the months.
		- The tempretures also are different, however the difference is by only sevelar degrees. The average demperature in June is 74.9 degrees and in December is 71.0 degrees. 
		- The temperature in December can go as low as 56 degrees, and in June the temperatures can go as low as 64 degrees.
	- The findings ingicate that the business might be slower in December, but tempratures are still warm enough to have customers.
	- Further analysis needed.
		- Tourist activity data of the area to determine if there would be customers other than local population.
		- Compare other months to determine which months would be off season. How many month during the year could be off season months?
		- Find data to determine what type customers the surf and ice cream shop businees would attrack. 
	- The minimum, maximum and average tempretures for the months of June and December datas were also added to Flask app (app.py) for the investors' review. 


