CREATE TABLE `order_header` (
	`order_id` INT(11) NOT NULL,
	`order_number` VARCHAR(20) NOT NULL COLLATE 'utf8mb4_general_ci',
	`order_date` DATE NOT NULL,
	`customer_id` INT(11) NOT NULL,
	`order_status` VARCHAR(10) NOT NULL COLLATE 'utf8mb4_general_ci',
	`currency` VARCHAR(10) NOT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`order_id`) USING BTREE,
	INDEX `customer_id` (`customer_id`) USING BTREE,
	CONSTRAINT `order_header_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer_referential` (`customer_id`) ON UPDATE RESTRICT ON DELETE RESTRICT
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;