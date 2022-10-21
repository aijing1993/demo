use patientconnection;
CREATE TABLE `patient` (
      `id` VARCHAR(40) NOT NULL,
      `firstname` VARCHAR(36),
      `lastname`  VARCHAR(36),
      PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;