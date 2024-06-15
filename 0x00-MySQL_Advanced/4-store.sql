-- SQL script that creates a trigger that decrease the quantity of an item
-- after adding a new order

DELIMITER //

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = New.item_name;
END; //

DELIMITER ;
