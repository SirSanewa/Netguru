# Netguru
## Run
To run open terminal in `netguru_app` directory and run `python manage.py runserver`
## Requirements
asgiref==3.3.1

certifi==2020.12.5

chardet==4.0.0

Django==3.1.7

djangorestframework==3.12.2

idna==2.10

pytz==2021.1

requests==2.25.1

sqlparse==0.4.1

urllib3==1.26.3

## Endpoints
1. POST /cars
Request body should contain car make and model name
Based on this data, its existence should be checked here https://vpic.nhtsa.dot.gov/api/
If the car doesn't exist - returned error
If the car exists - saved in the database

example post:
Content-Type: application/json;charset=UTF-8
`{
  "make" : "Volkswagen",
  "model" : "Golf",
}`

2. DELETE /cars/{ id }
Deletes car with the given id from database
If the car doesn't exist in database - returns an error

example delete:
`DELETE /cars/{  id }/`

3. POST /rate
* Add a rate for a car from 1 to 5

example post:
`POST /rate/`
Content-Type: application/json;charset=UTF-8
`{
  "car_id" : 1,
  "rating" : 5,
}`

4. GET /cars
Returns a list of all cars already present in application database with their current average rate

example get:
`GET /cars/`
Content-Type: application/json;charset=UTF-8

Response:
`[
{
  "id" : 1,
  "make" : "Volkswagen",
  "model" : "Golf",
  "avg_rating" : 5.0,
},
{
  "id" : 2,
  "make" : "Volkswagen",
  "model" : "Passat",
  "avg_rating" : 4.7,
}
]`

5. GET /popular
Returns top cars already present in the database ranking based on a number of rates.

example get:
`GET /popular/`
Content-Type: application/json;charset=UTF-8

Response:
`[
{
  "id" : 1,
  "make" : "Volkswagen",
  "model" : "Golf",
  "rates_number" : 100,
},
{
  "id" : 2,
  "make" : "Volkswagen",
  "model" : "Passat",
  "rates_number" : 31,
}
]`