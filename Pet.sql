

 --Database: `pet'


-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `ap_id` int(11) NOT NULL,
  `pet_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `purpose` varchar(100) NOT NULL,
  `notes` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;




INSERT INTO `appointment` (`ap_id`, `pet_id`, `date`, `purpose`, `notes`) VALUES
(31, 16, '2024-03-16', 'erty', 'dbn'),
(32, 12, '2023-12-11', 'vaccination', 'appointment for vaccination'),
(33, 14, '2021-04-12', 'health checkup', 'monthy health checkup'),
(34, 5, '2003-03-21', 'injectoj', 'cg');

-- --------------------------------------------------------


-- Table structure for table `emergency_contact`

CREATE TABLE `emergency_contact` (
  `contact_id` int(11) NOT NULL,
  `pet_relation` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `pet_id` int(11) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `emergency_contact`
--

INSERT INTO `emergency_contact` (`contact_id`, `pet_relation`, `name`, `pet_id`, `phone`) VALUES
(16, 'parent', 'rah', 5, '1234567890'),
(19, 'parent', 'rah', 5, '1265789035'),
(22, 'parent', 'rah', 5, '1265789035'),
(25, 'owner', 'rahul', 12, '1224456788');

-- --------------------------------------------------------

--
-- Table structure for table `health_record`
--

CREATE TABLE `health_record` (
  `record_id` int(11) NOT NULL,
  `pet_id` int(11) NOT NULL,
  `vaccination` varchar(100) NOT NULL,
  `medication` varchar(100) NOT NULL,
  `medical_history` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `health_record`
--

INSERT INTO `health_record` (`record_id`, `pet_id`, `vaccination`, `medication`, `medical_history`) VALUES
(21, 16, 'Canine Distemper Virus (CDV)', 'Anti-inflammatories', 'asdfgh'),
(22, 5, 'CDV', 'qwertyul', 'nothing'),
(23, 5, 'fone', 'ghuhj', 'g'),
(24, 5, 'xcvbn', 'okmb', 'none');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `empid` varchar(50) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `empid`, `password`) VALUES
(1, 'E001', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `nutrition_and_diet`
--

CREATE TABLE `nutrition_and_diet` (
  `nutrition_diet_id` int(11) NOT NULL,
  `pet_id` int(11) NOT NULL,
  `diet_plan` varchar(100) NOT NULL,
  `requirements` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nutrition_and_diet`
--

INSERT INTO `nutrition_and_diet` (`nutrition_diet_id`, `pet_id`, `diet_plan`, `requirements`) VALUES
(8, 5, 'Monitor Weight and Overall Health', 'Current Diet'),
(12, 16, 'dfghj', 'dfgh'),
(14, 12, 'wdf', 'xcv');

-- --------------------------------------------------------

--
-- Table structure for table `pet`
--

CREATE TABLE `pet` (
  `pet_id` int(11) NOT NULL,
  `breed` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `species` varchar(50) NOT NULL,
  `u_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pet`
--

INSERT INTO `pet` (`pet_id`, `breed`, `age`, `species`, `u_id`) VALUES
(5, 'ranj', 2, 'lmn', 'abc'),
(12, 'raks', 4, 'bn', 'azx'),
(14, 'Labrador Retriever', 3, 'Canis latrans', 'NONE'),
(16, 'Bulldog', 3, 'asd', 'keft eye small'),
(17, 'pertian', 3, 'kml', 'keft eye small'),
(18, 'bulldog', 4, 'kml', 'keft eye small');


--

-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`ap_id`),
  ADD KEY `appointment_ibfk_1` (`pet_id`);

--
-- Indexes for table `emergency_contact`
--
ALTER TABLE `emergency_contact`
  ADD PRIMARY KEY (`contact_id`),
  ADD KEY `emergency_contact_ibfk_1` (`pet_id`);

--
-- Indexes for table `health_record`
--
ALTER TABLE `health_record`
  ADD PRIMARY KEY (`record_id`),
  ADD KEY `foreign key` (`pet_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nutrition_and_diet`
--
ALTER TABLE `nutrition_and_diet`
  ADD PRIMARY KEY (`nutrition_diet_id`),
  ADD KEY `fk_nutrition_pet` (`pet_id`);

--
-- Indexes for table `pet`
--
ALTER TABLE `pet`
  ADD PRIMARY KEY (`pet_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `ap_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `emergency_contact`
--
ALTER TABLE `emergency_contact`
  MODIFY `contact_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `health_record`
--
ALTER TABLE `health_record`
  MODIFY `record_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `nutrition_and_diet`
--
ALTER TABLE `nutrition_and_diet`
  MODIFY `nutrition_diet_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `pet`
--
ALTER TABLE `pet`
  MODIFY `pet_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

-
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`pet_id`) REFERENCES `pet` (`pet_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `emergency_contact`
--
ALTER TABLE `emergency_contact`
  ADD CONSTRAINT `emergency_contact_ibfk_1` FOREIGN KEY (`pet_id`) REFERENCES `pet` (`pet_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `health_record`
--
ALTER TABLE `health_record`
  ADD CONSTRAINT `foreign key` FOREIGN KEY (`pet_id`) REFERENCES `pet` (`pet_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `nutrition_and_diet`
--
ALTER TABLE `nutrition_and_diet`
  ADD CONSTRAINT `fk_nutrition_pet` FOREIGN KEY (`pet_id`) REFERENCES `pet` (`pet_id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- Assertions
Ensure the pet's age is a non-negative value:

-ALTER TABLE pet
ADD CONSTRAINT chk_pet_age CHECK (age >= 0);

Ensure that the phone number consists of exactly 10 digits (valid for your use case):

ALTER TABLE emergency_contact
ADD CONSTRAINT chk_phone_format CHECK (LENGTH(phone) = 10 AND phone REGEXP '^[0-9]+$');

--Trigger

Trigger to Enforce Unique Emergency Contact Per Pet:

DELIMITER //
CREATE TRIGGER enforce_unique_contact_per_pet
BEFORE INSERT ON emergency_contact
FOR EACH ROW
BEGIN
   DECLARE contact_exists INT;
   SELECT COUNT(*) INTO contact_exists
   FROM emergency_contact
   WHERE pet_id = NEW.pet_id AND pet_relation = NEW.pet_relation;
   
   IF contact_exists > 0 THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'This pet already has an emergency contact for this relation type';
   END IF;
END;
//
DELIMITER ;

 Trigger for Deleting Related Data Automatically 
 
DELIMITER //
CREATE TRIGGER cascade_delete_pet
AFTER DELETE ON pet
FOR EACH ROW
BEGIN
   DELETE FROM health_record WHERE pet_id = OLD.pet_id;
   DELETE FROM nutrition_and_diet WHERE pet_id = OLD.pet_id;
   DELETE FROM emergency_contact WHERE pet_id = OLD.pet_id;
END;
//
DELIMITER ;

DELIMITER //

CREATE TRIGGER trg_check_future_date
BEFORE INSERT ON appointment
FOR EACH ROW
BEGIN
    IF NEW.date < CURDATE() THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Appointment date must be today or later.';
    END IF;
END;
//

DELIMITER ;


COMMIT;

