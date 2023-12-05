CREATE TABLE `orders` (
	`order_id` INT(11) NOT NULL,
	`order_number` VARCHAR(20) NOT NULL COLLATE 'utf8mb4_general_ci',
	`order_date` DATE NOT NULL,
	`currency` VARCHAR(10) NOT NULL COLLATE 'utf8mb4_general_ci'
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;