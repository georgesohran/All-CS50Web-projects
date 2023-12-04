-- Keep a log of any SQL queries you execute as you solve the mystery.
-- 07.28, Humphrey street
-- name, place tp leave

-- sus people:

SELECT description FROM crime_scene_reports WHERE month == 7 AND day == 28;
--time: 10:15, three withnesses

SELECT transcript,name FROM interviews WHERE month == 7 AND day == 28;
-- withdraw money, drove away from bakery parking lot, flew away tomorrow

SELECT activity,license_plate FROM bakery_security_logs WHERE month == 7 AND day == 28 AND hour == 10 ;

SELECT atm_location FROM atm_transactions GROUP BY atm_location;
-- Leggett Street


SELECT name FROM people WHERE
    id IN (SELECT person_id FROM bank_accounts WHERE
        account_number IN (SELECT account_number FROM atm_transactions WHERE
            month == 7 AND day == 28 AND atm_location == 'Leggett Street' AND transaction_type == 'withdraw'
            )
        );
-- suspects: Kenny, Iman, Benista, Taylor, Brooke, Luca, Diana, Bruce

SELECT * FROM people WHERE name == 'Bruce';

SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month == 7 AND day == 28) AND name == 'Bruce';


--Bruce, Keny, Benista, Taylor, Brooke made a call that day.
