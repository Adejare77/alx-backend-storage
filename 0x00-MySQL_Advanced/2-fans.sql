-- SQL script that ranks country origins of bands, ordered by the number of
-- of (non-unique) fans. Requirements:
-- Column names must be: origin and nb_fans


SELECT origin,
        SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC
