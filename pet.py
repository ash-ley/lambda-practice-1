import json

# def lambda_handler(event, context):
#     return {
#         'statusCode' : 200,
#         for name, species, birthYear, favFoods, photo in x['pets']:
# 	        if name == "Meowsalot":
# 		print(favFoods)
#         'body' : json.dumps(event['favFoods'])
#     }
sample_data = {
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

event = {
    "S3Bucket" : "talent-academy-example-storage",
    "S3Prefix" : "sample_data.json",
    "PetName"  : "Meowsalot"
}
print(event["PetName"])
myPet = event['PetName']

for name, species, birthYear, favFoods, photo in sample_data['pets']:
    print(name)
	if name == myPet:
		print(favFoods)
    else:
        print(name)
