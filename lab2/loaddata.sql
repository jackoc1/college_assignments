create table industrial_price_index (
	statistic varchar(50),
    mont varchar(20),
    sector varchar(20),
    unit varchar(30),
    value float
);

LOAD DATA INFILE '/home/jack-o-connor/Downloads/WPM25.20211124T001117.csv' 
INTO TABLE industrial_price_index 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;