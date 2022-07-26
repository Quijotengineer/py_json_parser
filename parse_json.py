import json

config_file = open("config/config.json")
config_contents = json.load(config_file)
json_filepath = config_contents['json_to_parse']

# json_file = open("data/example.json")
json_file = open(json_filepath)

# returns JSON object as a dictionary
json_contents = json.load(json_file)
  
# Iterating through the json list
print('\n === S3 Inputs: === \n')
try:
    for input in json_contents['s3']['input']:
        print(input, ': ', json_contents['s3']['input'][input])
except:
    print("No S3 inputs")

print('\n === S3 Outputs: === \n')
try:
    for output in json_contents['s3']['output']:
        print(output, ': ', json_contents['s3']['output'][output])
except:
    print("No S3 outputs")

print('\n === Hive Inputs: === \n')
try:
    for input in json_contents['hive']['input']:
        print(input, ': ', json_contents['hive']['input'][input])
except:
    print("No hive inputs")

print('\n === Hive Outputs: === \n')
try:
    for output in json_contents['hive']['output']:
        print(output, ': ', json_contents['hive']['output'][output])
except:
    print("No hive outputs")
  
# Closing file
json_file.close()