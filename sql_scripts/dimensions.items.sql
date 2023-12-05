CREATE TABLE `items` (
	`item_id` INT(11) NOT NULL,
	`item_description` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`item_status` VARCHAR(1) NOT NULL COLLATE 'utf8mb4_general_ci'
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;