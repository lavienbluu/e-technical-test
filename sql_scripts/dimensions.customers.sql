CREATE TABLE `customers` (
	`customer_id` INT(11) NOT NULL,
	`customer_no` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`customer_name` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`address` VARCHAR(100) NOT NULL COLLATE 'utf8mb4_general_ci',
	`city` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`country_code` VARCHAR(10) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`postal_code` VARCHAR(10) NOT NULL COLLATE 'utf8mb4_general_ci'
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;