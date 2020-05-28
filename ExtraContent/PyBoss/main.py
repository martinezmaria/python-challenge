# import modules
import os
import csv

# create path to file
csv_file_path = os.path.join("Resources", "employee_data.csv")

# define variables
line_count = 0
employee_id = []
name = []
firstname = []
lastname = []
dob = []
new_dob = []
ss_number = []
new_ss = []
state = []
new_state = []

state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# open and read file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    csv_header = next(csvreader)

    print(csv_header)

# loop through rows
    for row in csvreader:
        print(row)

          
        line_count += 1
        employee_id.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ss_number.append(row[3])
        

        name =row[1].split(" ")
        firstname.append(name[0])
        lastname.append(name[1])

        dob = row[2].split("-")
        new_dob.append(dob[1] + str("/") + dob[2] + str("/") + dob[0])

        ss_number = row[3].split("-")
        new_ss.append(str('xxx-xx-') + ss_number[2])

        state = state_abbrev.values()
    

cleaned_employee_csv = zip(employee_id, firstname, lastname, new_dob, new_ss, state)

output_file = os.path.join("Analysis" , "new_employee_data.txt")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    writer.writerows(cleaned_employee_csv)