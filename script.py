import json
import operator
import csv

with open('./raw_findings.json') as json_file:
    data = json.load(json_file)

print("Number of cases: ", len(data["Findings"]))

finalList = []
for i in data["Findings"]:

    resourceName = i["Resources"][0]["Id"].split(":")[5]
    accountId = i["AwsAccountId"]
    region = i["Resources"][0]["Region"]
    title = i["Title"]
    severity = i["Severity"]["Label"]
    resourceType = i["Resources"][0]["Type"]
    standardType = i["Types"][0].split("/")[2]

    if "Details" in i["Resources"][0]:
        if "CreatedAt" in i["Resources"][0]["Details"][resourceType]:
            createdAt = i["Resources"][0]["Details"][resourceType]["CreatedAt"]
            formattedTime = createdAt.split("T",1)[0] + " " +  createdAt.split("T",1)[1].split(".",1)[0]
        elif "LaunchedAt" in i["Resources"][0]["Details"][resourceType]:
            createdAt = i["Resources"][0]["Details"][resourceType]["LaunchedAt"]
            formattedTime = createdAt.split("T",1)[0] + " " +  createdAt.split("T",1)[1].split(".",1)[0]
        else:
            formattedTime = "\t-\t"
        findingList.append([accountId,region,severity,resourceName,formattedTime])
    else:
        formattedSpace = "\t\t\t"
        findingList.append([accountId,region,severity,resourceName,formattedSpace])

sortedList = sorted(findingList, key=lambda x:x[0])

titleHeader = ["Title", title]
standardHeader = ["Standard Type", standardType]
header = ["Account ID","Region","Severity",resourceType,"CreatedAt","Action Taken"]
with open('FormattedFindings.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(titleHeader)
    writer.writerow(standardHeader)
    writer.writerow(" ")
    writer.writerow(header)
    writer.writerows(sortedList)