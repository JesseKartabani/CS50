-- Keep a log of any SQL queries you execute as you solve the mystery.

-- All I know is that the theft took place on July 28,
-- 2020 and that it took place on Chamberlin Street.

.tables -- Lists all of the tables in the database.
.schema -- Lists the schema of the database used for knowing which columns to query.

-- Im going to start with the crime scene reports table as advised.
.schema crime_scene_reports
-- CREATE TABLE crime_scene_reports (
--  id INTEGER,
--  year INTEGER,
--  month INTEGER,
--  day INTEGER,
--  street TEXT,
--  description TEXT,
--  PRIMARY KEY(id)
--  );

-- Using this query I was able to get a description on the theft.
SELECT description FROM crime_scene_reports
WHERE day = "28" AND month = "7" AND year = "2020" AND street = "Chamberlin Street";
-- Theft of the CS50 duck took place at 10:15am at the Chamberlin Street courthouse.
-- Interviews were conducted today with three witnesses who were present at the time -
-- each of their interview transcripts mentions the courthouse.

-- Using this query i was able to get the transcript of the interview.
SELECT transcript FROM interviews
WHERE day = "28" AND month = "7" AND year = "2020" AND transcript LIKE "%courthouse%";
-- I found three pieces of key infomation
-- 1.The thief got into a car in the courthouse parking lot sometime within ten minutes of the theft.
-- 2.The thief withdrew money from the ATM on Fifer Street.
-- 3.As the thief was leaving the courthouse they called someone (length of call  <1m) and it was overheard that they were
--   planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person
--   on the other end of the phone to purchase the flight ticket.

SELECT activity FROM courthouse_security_logs; -- Used to see how activities work.

-- Gets the names of people that left the courthouse within the 10 minute timeframe.
SELECT name FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE day = "28" -- Names: Patrick, Ernest, Amber, Danielle, Roger,
AND month = "7"  --        Elizabeth, Russell, Evelyn
AND year = "2020"
AND hour = "10"
AND minute >= "15"
AND minute < "25"
AND activity = "exit";

-- Gets the names of people who took money out the ATM the day of the crime on Fifer Street.
SELECT DISTINCT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE day = "28"  -- Names: Danielle, Bobby, Madison, Ernest, Roy,
AND month = "7"   --        Elizabeth, Victoria, Russell
AND year = "2020"
AND transaction_type = "withdraw"
AND atm_location = "Fifer Street";

-- Gets the names of the people who took the first flight on the day after the 28th.
SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = (SELECT id FROM flights WHERE day = "29" -- Names: Doris, Roger, Ernest, Edward,
AND month = "7"                                            --        Evelyn, Madison, Bobby,
AND year = "2020" ORDER BY hour, minute LIMIT 1);          --        Danielle

-- Gets the names of the people who made a call less than one minute long the day of the crime.
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE day = "28" -- Names: Roger, Evelyn, Ernest, Evelyn, Madison,
AND month = "7"  --        Russell, Kimberly, Bobby, Victoria
AND year = "2020"
AND duration < "60";

-- Now I intersect all of the infomation to find the name of the thief.
SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = (SELECT id FROM flights
WHERE day = "29"
AND month = "7"
AND year = "2020"
ORDER BY hour, minute LIMIT 1)
INTERSECT
SELECT DISTINCT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE day = "28"
AND month = "7"
AND year = "2020"
AND transaction_type = "withdraw"
AND atm_location = "Fifer Street"
INTERSECT
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE day = "28"
AND month = "7"
AND year = "2020"
AND duration < "60"
INTERSECT
SELECT name FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE day = "28"
AND month = "7"
AND year = "2020"
AND hour = "10"
AND minute >= "15"
AND minute < "25"
AND activity = "exit";
-- Revealing Ernest is the thief.

-- Finding where Ernest escaped to.
SELECT city FROM airports
WHERE id = (SELECT destination_airport_id FROM flights
WHERE day = "29"
AND month = "7"
AND year = "2020"
ORDER BY hour, minute LIMIT 1);
-- Revealing it was the city London.

-- Finding the accomplice
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE day = "28"
AND month = "7"
AND year = "2020"
AND duration < "60"
AND caller = (SELECT phone_number FROM people WHERE name = "Ernest");
-- Revealing it was Berthold.