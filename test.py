event = {
  "S3Bucket": "talent-academy-439272626435-tfstate-ashley",
  "S3Prefix": "sprint2/lambda-practice-1/sample_data.json",
  "PetName": "Meowsalot"
}

body = {
    "pets": [
      {
        "name" : "Purrsloud",
        "species" : "Cat",
        "favFoods" : ["wet food", "dry food", "<strong>any</strong> food"],
        "birthYear" : 2016,
        "photo" : "https://learnwebcode.github.io/json-example/images/cat-2.jpg"
      },
      {
        "name" : "Barksalot",
        "species" : "Dog",
        "birthYear" : 2008,
        "favFoods" : ["wet food", "dry food", "<strong>any</strong> food"],
        "photo" : "https://learnwebcode.github.io/json-example/images/dog-1.jpg"
      },
      {
        "name" : "Meowsalot",
        "species" : "Cat",
        "favFoods" : ["tuna", "catnip", "celery"],
        "birthYear" : 2012,
        "photo" : "https://learnwebcode.github.io/json-example/images/cat-1.jpg"
      }
    ]
  }

for pets in body['pets']:
    if pets['name'] == event['PetName']:
        print(pets['favFoods'])