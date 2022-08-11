# IOTECH Coding Exercises

# Solution of IOTech Coding Exercise 1
- To view the final json file for this exercise navigate to `exercises-main/exercise-01/newDevices.json`
- All code responisble for the soltuion may be found in `exercises-main/exercise-01/main.py`



# IOTech Exercise 1:
Please provide the completed solution as a public Github repository. It should include:
- Your solution
- A readme instructing the user how to build and run your solution. It must build on linux, other platforms are optional
- (optional) Any addtional material e.g. tests, dockerfile

Please write a program in the language of your choice (C or GO prefered) to complete the following tasks:

- Parse the data in `exercise-01/data/devices.json`
- Extract the `uuid` from the `Info` field
- For each device, calculate sum of the sensor payloads
- Reformat the data so that it satisfies the schema in `exercise-01/output-schema/schema.json`
- Order the reformatted data by `Name` (ascending)
- Write the reformatted data to a new file in `JSON` format