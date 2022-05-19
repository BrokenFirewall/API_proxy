# API proxy assignment

For this assignment you are asked to create an API service accepting any person
given name (e.g. "Tom", "Pasquale", "Axel", etc.) as input and then gets back the most probable country of origin
by relying on an external API service.

You can use the `https://nationalize.io/` API service to guess the nationality
of any input sent to your API service. Unfortunately (is it?) `nationalize.io`
returns just the country code (ISO-3166-1), not the human readable country name.

Since you should return the country full name you need to use yet another API service
(`https://restcountries.com/`) that, among other things, lets you retrieve the
official name of any country.


On success your API service should return to the users the following
information:

- name received as input
- a human readable message

On failure:

- name received as input
- a meaningful HTTP code error
- a descriptive and human readable error message

On success, and according to the retrieved probability, the human readable
message should be formatted like this:

- if the probability is higher than 60%:
   [GIVEN_NAME] is mostly certain to be from [COUNTRY_NAME]

- if the probability is between 30% and 60%:
   [GIVEN_NAME] may be from [COUNTRY_NAME]

- if the probability is below 30%:
   It seems that [GIVEN_NAME] is from [COUNTRY_NAME]. But I'm just guessing!

The problem is quite simple and it has been chosen to be like that on purpose,
because in implementing it you should pay attention to a number of things:

- design you API service (even if so simple) for testability
- decide if you want to validate you user input or not
- write automated tests (the amount and type of tests you think is adequate)
- deal with possible errors from external services
- deal with possible unavailability of external services
- configure you API service for logging

You can write your service in your language of choice. Packaging the service as
a Docker image will be considered a plus.
