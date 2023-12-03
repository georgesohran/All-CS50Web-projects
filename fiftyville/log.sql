-- Keep a log of any SQL queries you execute as you solve the mystery.
-- 07.28, Humphrey street
-- name, place tp leave

-- sus people:

SELECT description FROM crime_scene_reports WHERE month == 7 AND day == 28;
--time: 10:15, three withnesses

SELECT transcript,name FROM interviews WHERE month == 7 AND day == 28;
-- withdraw money, drove away from bakery parking lot, flew away tomorrow
