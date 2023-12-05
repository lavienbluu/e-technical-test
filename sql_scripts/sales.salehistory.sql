CREATE TABLE `saleshistory` (
	`orderline_id` INT(11) NOT NULL,
	`order_id` INT(11) NOT NULL,
	`item_id` INT(11) NOT NULL,
	`customer_id` INT(11) NOT NULL,
	`ship_date` DATE NOT NULL,
	`promise_date` DATE NOT NULL,
	`ordered_quantity` INT(11) NOT NULL
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;