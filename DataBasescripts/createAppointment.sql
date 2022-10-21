USE cs6440_sp22_team012;
CREATE TABLE Appointments (
	ID 			varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
    START 		date DEFAULT NULL,
	STOP 		date DEFAULT NULL,
	PATIENT 	varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
    APPOINTMENT varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    PRIMARY KEY (ID)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

