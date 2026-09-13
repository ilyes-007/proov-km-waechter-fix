# What I checked, and what the agent got wrong

Write this yourself, in your own words. It is the part of the repo that proves the work is yours.

## What the agent got wrong
After carefully reading the results that the AI gave me, I noticed that it was using a different logic to tell if a car needs a service or not. It's not accurate since it does not flag out the new cars - which never had a service - when they reach more than 80% of the wear interval. It uses this false logic in needs_service and fleet_report.py file, and I could notice the error by verifying the test_km_watcher.py file where we can see that a fully worn car wasn't flagged.

## What I checked before I accepted its work
I verified the wear fix is correct by comparing it to my solution and checked that the used syntax is the correct one.

## What the data actually said
The data analysis showed the important parameters that actually predict breakdowns were km_since_service, avg_daily_km and load_factor. The parameters odometer_km and age_years don't really change between the healthy cars and the broken-down ones.