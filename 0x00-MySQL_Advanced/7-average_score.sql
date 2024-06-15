-- SQL script that creates a stored procedure 'ComputeAverageScoreForUser'
-- that computes and store the average score for a student. Note: Average
-- score can be a decimal
-- Requirements:
-- Procedure 'ComputeAverageScoreForUser' is taking 1 inpute
-- user_id: a users.id value(you can assume user_id is linked to an
-- existing users)

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE average_score_by_user_id DECIMAL(10, 2);
    SELECT AVG(score) INTO average_score_by_user_id
    FROM corrections
    WHERE corrections.user_id = user_id
    GROUP BY user_id;

    UPDATE users
    SET average_score = average_score_by_user_id
    WHERE id = user_id;
END; //

DELIMITER ;
