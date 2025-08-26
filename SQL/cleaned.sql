CREATE TABLE IF NOT EXISTS cleaned.faction_distribution AS
SELECT
    ROW_NUMBER() OVER () AS id,
    Faction AS faction,
    Regions AS regions,
    CAST(REPLACE(percent, '%', '') AS DOUBLE) AS percent
FROM main.faction_distribution
WHERE faction <> 'Total';


CREATE TABLE IF NOT EXISTS cleaned.households AS
SELECT
    ROW_NUMBER() OVER () AS id,
    household_id,
    region_id,
    household_type
FROM main.households;


CREATE TABLE IF NOT EXISTS cleaned.language_building_blocks AS
SELECT
    Language_ID AS id,
    Language_Name AS language,
    Branch_From AS branch_from,
    Phonology_Notes AS phonology_notes,
    Morphology_Patterns AS morphology,
    Example_Roots AS example_roots
FROM main.language_building_blocks;


CREATE TABLE IF NOT EXISTS cleaned.language_roots AS
SELECT
    ROW_NUMBER() OVER () AS id,
    Root AS root,
    Meaning AS meaning,
    Notes AS notes
FROM main.language_roots;


CREATE TABLE IF NOT EXISTS cleaned.moons AS
SELECT
    Moon_ID AS id,
    Moon_Name AS name,
    Settlement_Formal AS settlement_formal,
    Colloquial AS colloquial,
    Staff_Size AS staff_size,
    Specialty AS specialty,
    Language_Origin AS language_origin
FROM main.moons;


CREATE TABLE IF NOT EXISTS cleaned.people AS
SELECT
    person_id AS id,
    first_name,
    age,
    "language" AS language,
    current_region_id,
    household_id,
    family_name
FROM main.people;


CREATE TABLE IF NOT EXISTS cleaned.planets AS
SELECT
    World_ID AS id,
    World_Name AS world_name,
    Star_System AS star_system,
    Planet_Type AS planet_type,
    Gravity_g AS gravity,
    Day_Length_hours AS day_length,
    Year_Length_days AS year_length,
    Axial_Tilt_deg AS axial_tilt,
    Calendar_Name AS calendar_name
FROM main.planets;

CREATE TABLE IF NOT EXISTS cleaned.region_biome AS
SELECT
    ROW_NUMBER() OVER () AS id,
    Region_ID AS region_id,
    Full_Name AS full_name,
    Biome     AS biome
FROM main.region_biome;


CREATE TABLE IF NOT EXISTS cleaned.regions AS
SELECT
    Region_ID AS id,
    Ancient_Name        AS ancient_name,
    Current_Faction     AS current_faction,
    Era_Tag             AS era_tag,
    Full_Name           AS full_name,
    Colloquial_Name     AS colloquial_name,
    Founding_Era        AS founding_era,
    Density_Tier        AS density_tier,
    Capital             AS capital,
    Primary_Industry    AS primary_industry,
    Founding_Story      AS founding_story,
    SPLIT(Vote_History_Last3, '>')[1] AS vote_1,
    SPLIT(Vote_History_Last3, '>')[2] AS vote_2,
    SPLIT(Vote_History_Last3, '>')[3] AS vote_3,
    Key_Pressure_Points AS key_pressure_points,
    Unbound_Presence    AS unbound_presence
FROM main.regions;

