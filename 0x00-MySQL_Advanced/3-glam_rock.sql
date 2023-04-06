-- Script that lists all bands with Glam rock
-- Column names must be: band_name and lifespan (in years)

SELECT band_name AS band_name, IFNULL(split, 2020)-IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
