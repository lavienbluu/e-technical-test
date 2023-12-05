CREATE TABLE `audit_table` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`start_time` DATETIME NOT NULL,
	`end_time` DATETIME NOT NULL,
	`numberrow_treatment` INT(11) NOT NULL,
	`status` VARCHAR(20) NOT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`id`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;