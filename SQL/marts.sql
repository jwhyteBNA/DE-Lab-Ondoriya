CREATE TABLE IF NOT EXISTS marts.total_population AS
SELECT COUNT(*) AS total_population
FROM cleaned.people;


CREATE TABLE IF NOT EXISTS marts.dominant_faction AS
SELECT Faction AS dominant_faction
FROM cleaned.faction_distribution
ORDER BY percent DESC
LIMIT 1;


CREATE TABLE IF NOT EXISTS marts.population_density_by_region AS
SELECT
    r.id AS region_id,
    r.full_name,
    COUNT(p.id) AS population
FROM cleaned.regions r
LEFT JOIN cleaned.people p ON r.id = p.current_region_id
GROUP BY r.id, r.full_name
ORDER BY population DESC;


CREATE TABLE IF NOT EXISTS marts.faction_distribution AS
SELECT
    Faction,
    percent
FROM cleaned.faction_distribution
ORDER BY percent DESC;


CREATE TABLE IF NOT EXISTS marts.top5_most_populous_regions AS
SELECT
    r.id AS region_id,
    r.full_name,
    COUNT(p.id) AS population
FROM cleaned.regions r
LEFT JOIN cleaned.people p ON r.id = p.current_region_id
GROUP BY r.id, r.full_name
ORDER BY population DESC
LIMIT 5;