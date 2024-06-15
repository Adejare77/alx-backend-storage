-- SQL script that creates a stored procedure 'ComputeAverageWeightedScoreForUser'
-- that computes and store the average weighted score for a student
-- Requirements:
-- Procedure 'ComputeAverageScoreForUser' takes 1 input: user_id

DELIMITER $$

CREATE PROCEDURE `ComputeAverageScoreForUser` (IN user_id)
BEGIN
    UPDATE projects
    SET weight
