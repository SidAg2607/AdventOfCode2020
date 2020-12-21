f = open("day16text.txt", "r+")

r = f.readlines()

rules = [[int(x) for x in r[0][r[0].index(":")+2:r[0].index(" or ")].split("-")]] + [[int(x) for x in r[0][r[0].index(" or ")+4:-1].split("-")]]


# Shorting the range of rules by combining ranges of all the Rules
def Checker(ruleToCheck):
    global rules
    if len(rules) > 1:
        for ind, rule1 in enumerate(rules):
            if (ruleToCheck[0] < rule1[0]) & (ruleToCheck[1] < rule1[1]):
                rules[ind][0] = ruleToCheck[0]
                return 0
            elif (ruleToCheck[0] < rule1[0]) & (ruleToCheck[1] > rule1[1]):
                if (ruleToCheck[1] > rules[ind+1][0]) & (ruleToCheck[1] < rules[ind+1][1]):
                    rules[ind][0] = ruleToCheck[0]
                    rules[ind][1] = rules[ind+1][1]
                    rules.pop(ind+1)
                    return 0
                elif ruleToCheck[1] < rules[ind+1][0]:
                    rules[ind][0] = ruleToCheck[0]
                    rules[ind][1] = ruleToCheck[1]
                    return 0
            elif (ruleToCheck[0] > rule1[0]) & (ruleToCheck[1] > rule1[1]):
                if (ruleToCheck[1] > rules[ind+1][0]) & (ruleToCheck[1] < rules[ind+1][1]):
                    rules[ind][1] = rules[ind+1][1]
                    rules.pop(ind+1)
                    return 0
                elif ruleToCheck[1] < rules[ind+1][0]:
                    rules[ind][1] = ruleToCheck[1]
                    return 0
            elif (ruleToCheck[0] > rule1[0]) & (ruleToCheck[1] < rule1[1]):
                return 0
    else:
        if ruleToCheck[0] < rules[0][0]:
            if ruleToCheck[1] < rules[0][1]:
                rules[0][0] = ruleToCheck[0]
                return 0
            else:
                rules[0][0] = ruleToCheck[0]
                rules[0][1] = ruleToCheck[1]
                return 0
        else:
            if ruleToCheck[0] < rules[0][1]:
                if ruleToCheck[1] < rules[0][1]:
                    return 0
                else:
                    rules[0][1] = ruleToCheck[1]
                    return 0
    rules.append(ruleToCheck)


for j in r[1:r.index("\n")]:
    rules_next = [[int(x) for x in j[j.index(":")+2:j.index(" or ")].split("-")]] + [[int(x) for x in j[j.index(" or ")+4:-1].split("-")]]
    for rule in rules_next:
        Checker(rule)

# Part 1
tickets = [int(y) for x in r[r.index("nearby tickets:\n")+1:] for y in x[:-1].split(",") if (int(y) < rules[0][0]) | (int(y) > rules[0][1])]
print("Part 1:", sum(tickets))


# Part 2
# making a list of valid nearby tickets
nearby_tickets = []
for x in r[r.index("nearby tickets:\n") + 1:]:
    count = 0
    for y in x[:-1].split(","):
        if (int(y) < rules[0][0]) | (int(y) > rules[0][1]):
            count += 1
    if count == 0:
        el1 = x[:-1].split(",")
        el2 = []
        for el in el1:
            el2.append(int(el))
        nearby_tickets.append(el2)

# making a list of columns in tickets
nearby_tickets_column = []

for integer in range(len(nearby_tickets[0])):
    nearby_tickets_column.append([])

for ticket in nearby_tickets:
    for place, id in enumerate(ticket):
        nearby_tickets_column[place].append(id)

# making a list of all rules
rules_all = []

for j in r[:r.index("\n")]:
    rules_all.append([[int(x) for x in j[j.index(":") + 2:j.index(" or ")].split("-")]] + [
        [int(x) for x in j[j.index(" or ") + 4:-1].split("-")]])

final = {}

Column_NumOfRules = {}


# A function which returns True if a column follows a particular Rule
def RuleChecker(Col, Rule_U):
    counter = 0
    for element in Col:
        if (Rule_U[0][0] <= element <= Rule_U[0][1]) | (Rule_U[1][0] <= element <= Rule_U[1][1]):
            counter += 1
    if counter == len(Col):
        return True
    else:
        return False


# To add Column: [List of Rules followed by Column] pairs to Column_NumOfRules
def NumOfRules(Column, index):
    global Column_NumOfRules
    for indRule, RuleForC in enumerate(rules_all):
        if RuleChecker(Column, RuleForC):
            Column_NumOfRules[index] += [indRule]


for IndexCol, ColumnToCheck in enumerate(nearby_tickets_column):
    Column_NumOfRules[IndexCol] = []
    NumOfRules(ColumnToCheck, IndexCol)


# Function to remove a particular Rule from the list of Rules for each column which contains that Rule
def RuleRemover(Rule):
    global Column_NumOfRules
    for var1, var2 in Column_NumOfRules.items():
        if Rule in var2:
            Column_NumOfRules[var1].pop(var2.index(Rule))


# Checks if the Column contains only one Rule and if it does then remove that rule from all columns to give the column containing only one rule a priority
def FinalChecker():
    global Column_NumOfRules
    global final
    for ColInd, RulesForColInd in Column_NumOfRules.items():
        if len(RulesForColInd) == 1:
            final[ColInd] = RulesForColInd[0]
            RuleRemover(RulesForColInd[0])
            Column_NumOfRules.pop(ColInd)
            if len(Column_NumOfRules.keys()) > 0:
                return FinalChecker()
            else:
                return 0


FinalChecker()

Ticket = [int(Column_my_ticket) for Column_my_ticket in r[r.index("your ticket:\n") + 1][:-1].split(",")]

FinalAnswer = 1

for colp, valp in final.items():
    if valp in range(6):
        FinalAnswer *= Ticket[colp]

print("Part 2:", FinalAnswer)

f.close()