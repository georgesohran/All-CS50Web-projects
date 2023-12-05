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
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month == 7 AND day == 28) AND name == 'Kenny';
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month == 7 AND day == 28) AND name == 'Benista';
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month == 7 AND day == 28) AND name == 'Brooke';
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month == 7 AND day == 28) AND name == 'Luca';
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month == 7 AND day == 28) AND name == 'Taylor';
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month == 7 AND day == 28) AND name == 'Diana';
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month == 7 AND day == 28) AND name == 'Iman';


--Bruce, Keny, Benista, Taylor, Diana Brooke made a call that day.

SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE day == 28 AND month == 7 AND year == 2021 AND hour == 10);

--Bruce, Diana drove away from bakery at 10.

SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE year ==2021 AND day==29 AND month==7 ));

--still Bruce and Diana

SELECT id FROM flights WHERE year ==2021 AND day==29 AND month==7 ORDER BY hour;

-- earliest flight id is 36

SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id == 36);

--the only name overlaping is Bruce, so that's probobly him

SELECT city FROM airports WHERE id == (SELECT destination_airport_id FROM flights WHERE id == 36);

--THe city thief escaped to was New York City

SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE caller == (SELECT phone_number FROM people WHERE name =='Bruce') AND day == 28 AND month == 7 AND year == 2021);

-- Possible accomplice == Gregory, Carl, Robin, Deborah


