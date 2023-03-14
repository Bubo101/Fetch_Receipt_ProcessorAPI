# Instructions
1. Clone project off of GitHub
2. CD to root project directory
3. RUN `docker-compose up --build` in the terminal
4. Make API Calls

- `localhost:8000/receipts/process` POST

Example JSON:
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}

Returns:
{
	"id": "receipt id number"
}

- `localhost:8000/receipts/{id}/points` GET

Example Return for Receipt Created Above:

{
	"points": 109
}

## Why Django?
- Django is what I know best. I know it's a bit large and overly powerful for this application, but I think that this showcases my ability to use and learn frameworks. I am confident that I would be able to pickup languages such as Go very quickly if needed for the role!