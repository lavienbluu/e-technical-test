CREATE TABLE `order_line` (
	`orderline_id` INT(11) NOT NULL,
	`order_id` INT(11) NULL DEFAULT NULL,
	`item_id` INT(11) NULL DEFAULT NULL,
	`ship_date` DATE NOT NULL,
	`promise_date` DATE NOT NULL,
	`ordered_quantity` INT(11) NOT NULL,
	PRIMARY KEY (`orderline_id`) USING BTREE,
	INDEX `order_id` (`order_id`) USING BTREE,
	INDEX `item_id` (`item_id`) USING BTREE,
	CONSTRAINT `order_line_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order_header` (`order_id`) ON UPDATE RESTRICT ON DELETE RESTRICT,
	CONSTRAINT `order_line_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item_referential` (`item_id`) ON UPDATE RESTRICT ON DELETE RESTRICT
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;