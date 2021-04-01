-- QUESTION 1
CREATE TABLE Pub(
	PLN VARCHAR(10) NOT NULL,
	PubName VARCHAR(30) NOT NULL,
	PCounty VARCHAR(20) NOT NULL,
	
	PRIMARY KEY (PLN)
);

CREATE TABLE NeighbourCounty(
	County1 VARCHAR(20) NOT NULL,
	County2 VARCHAR(20) NOT NULL,
	
	PRIMARY KEY (County1, County2)
);

CREATE TABLE Person(
	PPSN VARCHAR(10) NOT NULL,
	PName VARCHAR(30) NOT NULL,
	PCounty VARCHAR(20) NOT NULL,
	Age SMALLINT NOT NULL,
	DailyPubLimit SMALLINT NOT NULL,
	
	PRIMARY KEY (PPSN)
);

CREATE TABLE Visit(
	PLN VARCHAR(10) NOT NULL,
	PPSN VARCHAR(10) NOT NULL,
	StartDateOfVisit DATETIME NOT NULL,
	EndDateOfVisit DATETIME NOT NULL,
	
	CHECK (StartDateOfVisit < EndDateOfVisit),  -- Doesn't do anything in MySQL but assignment does have CHECK listed as an option since works in other SQL variants.
	
	PRIMARY KEY (PLN, PPSN, StartDateOfVisit, EndDateOfVisit),
	FOREIGN KEY (PLN) REFERENCES Pub (PLN) ON DELETE CASCADE,
	FOREIGN KEY (PPSN) REFERENCES Person (PPSN) ON DELETE CASCADE
);

CREATE TABLE Covid_Diagnosis(
	PPSN VARCHAR(10) NOT NULL,
	DiagnosisDate DATE NOT NULL,
	IsolationEndDate DATE NOT NULL,
	
	CHECK (DiagnosisDate < IsolationEndDate), -- Doesn't do anything in MySQL but assignment does have CHECK listed as an option since works in other SQL variants.
	
	PRIMARY KEY (PPSN, DiagnosisDate),
	FOREIGN KEY (PPSN) REFERENCES Person (PPSN) ON DELETE CASCADE
);

-- QUESTION 2
-- Tom should not be able to visit a pub in Limerick. My delimiter in a later question catches this, but since Q2 asks to populate with these values I've him in Visit anyway.
INSERT INTO Pub VALUES
	("L1234", "Murphy's", "Cork"),
	("L2345", "Joe's", "Limerick"),
	("L3456", "BatBar", "Kerry");

INSERT INTO NeighbourCounty VALUES
	("Cork", "Limerick"),
	("Limerick", "Cork"),
	("Cork", "Kerry"),
	("Kerry", "Cork");
 
INSERT INTO Person VALUES
	("1", "Liza", "Cork", 22, 5),
	("2", "Alex", "Limerick", 19, 7),
	("3", "Tom", "Kerry", 23, 10),
	("4", "Peter", "Cork", 39, 8);

INSERT INTO Visit VALUES
	("L1234", "1", '2020-02-10 10:00:00', '2020-02-10 11:00:00'),
	("L1234", "1", '2020-12-08 11:00:00', '2020-12-08 11:35:00'),
	("L2345", "3", '2020-12-03 11:00:00', '2020-02-10 11:50:00');

INSERT INTO Covid_Diagnosis VALUES
	("2", '2020-02-11', '2020-02-21');


-- QUESTION 3
DELIMITER //
DROP TRIGGER IF EXISTS restrict_visit_infection //
CREATE TRIGGER restrict_visit_infection
	BEFORE INSERT ON Visit
	FOR EACH ROW
BEGIN
	DECLARE finish INT;
	DECLARE diagnosis_date DATETIME;
	DECLARE isolation_end_date DATETIME;
	DECLARE latest_diagnosis_date DATETIME;
	DECLARE latest_isolation_end_date DATETIME;
	-- Get latest isolation period for new.PPSN.
	-- If you have got it twice your first case was in the past and you can't book a visit for a past date.
	DECLARE cur CURSOR FOR SELECT cd.DiagnosisDate, cd.IsolationEndDate FROM Covid_Diagnosis cd WHERE cd.PPSN = NEW.PPSN;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET finish = 1;
	
	SET latest_diagnosis_date = '1760-10-03 11:00:00';  -- set to impossible date to prevent null values errors.
	SET latest_isolation_end_date = '1760-10-04 11:00:00';
	SET finish = 0;

	OPEN cur;
	getDates: LOOP
		FETCH cur INTO diagnosis_date, isolation_end_date;
		IF (finish = 1) THEN
			LEAVE getDates;
		END IF;
		IF (diagnosis_date > latest_diagnosis_date) THEN
			SET latest_diagnosis_date = diagnosis_date;
			SET latest_isolation_end_date = isolation_end_date;
		END IF;
	END LOOP getDates;
	CLOSE cur;

	IF ((NEW.StartDateOfVisit BETWEEN latest_diagnosis_date AND latest_isolation_end_date)
		OR (NEW.EndDateOfVisit BETWEEN latest_diagnosis_date AND latest_isolation_end_date))
	THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Person has the Covid-19 at that time.';
	END IF;
END; //
DELIMITER ;

-- QUESTION 4
CREATE VIEW PERSON_ALLOWED_PUBS(ppsn, pln) AS
	SELECT p.PPSN, pb.PLN
	FROM Person p JOIN Pub pb
		ON p.Pcounty = pb.PCounty
	UNION -- Pubs in same county as person union pubs in neighbouring counties to person.
	SELECT p2.PPSN, pb2.PLN
	FROM Person p2 JOIN NeighbourCounty nc JOIN Pub pb2
		ON p2.PCounty = nc.County1 AND nc.County2 = pb2.PCounty;

DELIMITER //
DROP TRIGGER IF EXISTS restrict_visit_county //
CREATE TRIGGER restrict_visit_county
	BEFORE INSERT ON Visit
	FOR EACH ROW
BEGIN
	IF ((SELECT COUNT(*) FROM PERSON_ALLOWED_PUBS pab WHERE pab.PLN = NEW.PLN AND pab.PPSN = NEW.PPSN) = 0)
	THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Person trying to travel outside their allowed counties.';
	END IF;
END; //
DELIMITER ;

-- QUESTION 5
-- One pub at a time
DELIMITER //
DROP TRIGGER IF EXISTS restrict_visit_one_pub_at_a_time //
CREATE TRIGGER restrict_visit_one_pub_at_a_time
	BEFORE INSERT ON Visit
	FOR EACH ROW
BEGIN
	DECLARE finish INT;
	DECLARE start_date DATETIME;
	DECLARE end_date DATETIME;
	
	DECLARE cur CURSOR FOR SELECT v.StartDateOfVisit, v.EndDateOfVisit FROM Visit v WHERE v.PPSN = NEW.PPSN;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET finish = 1;

	SET finish = 0;

	OPEN cur;
	getDateInterval: LOOP
		FETCH cur INTO start_date, end_date;
		IF (finish = 1) THEN
			LEAVE getDateInterval;
		END IF;
		
		-- Check their start date doesn't coincide with any other visits.
		IF ((NEW.StartDateOfVisit > start_date) AND (NEW.StartDateOfVisit < end_date))
		THEN
			SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Person can not be in 2 pubs at once.';
		
		-- Check their end date doesn't coincide with any other visits
		ELSEIF (NEW.EndDateOfVisit > start_date AND NEW.EndDateOfVisit < end_date)
		THEN
			SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Person can not be in 2 pubs at once.';
		END IF;
	END LOOP getDateInterval;
	CLOSE cur;
END; //
DELIMITER ;

-- Daily pub limit
DELIMITER //
DROP TRIGGER IF EXISTS restrict_visit_daily_limit //
CREATE TRIGGER restrict_visit_daily_limit
	BEFORE INSERT ON Visit
	FOR EACH ROW
BEGIN
	DECLARE daily_limit INT;
	DECLARE new_start_date DATE;
	DECLARE new_end_date DATE;
	
	SET new_start_date = DATE(NEW.StartDateOfVisit);  -- Reduce calls to DATE function
	SET new_end_date = DATE(NEW.EndDateOfVisit);
	SELECT p.DailyPubLimit INTO daily_limit FROM Person p WHERE p.PPSN = NEW.PPSN;
	
	-- Only have to worry about start and end since people can only be in one pub at a time.
	IF ((SELECT COUNT(*)
		FROM Visit v 
		WHERE ((v.PPSN = NEW.PPSN) AND (
			((new_start_date = DATE(v.StartDateOfVisit)) OR (new_start_date = DATE(v.EndDateOfVisit)))))) > daily_limit)
	THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Person in excess of thier daily limit';
	
	-- Check don't exceed daily limit for the day they finish as well.
	ELSEIF ((SELECT COUNT(*)
		FROM Visit v 
		WHERE ((v.PPSN = NEW.PPSN) AND (
			(new_end_date = DATE(v.StartDateOfVisit) OR new_end_date = DATE(v.EndDateOfVisit))))) > daily_limit)
	THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Person in excess of their daily limit';
	END IF;
END; //
DELIMITER ;

-- QUESTION 6
-- Counties with zero previous cases do not show up.
CREATE VIEW COVID_NUMBERS(county, cases) AS
	SELECT p.PCounty, COUNT(cd.PPSN)
	FROM Person p JOIN Covid_Diagnosis cd
		ON p.PPSN = cd.PPSN
	GROUP BY p.PCounty;
