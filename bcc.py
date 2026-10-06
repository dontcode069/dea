


import pulp
from data import df

for dmu in df.index:
    row = df.loc[dmu]

    prob = pulp.LpProblem(f"BCC_{dmu}", pulp.LpMaximize)
    u = pulp.LpVariable("u", lowBound=0)
    v1 = pulp.LpVariable("v1", lowBound=0)
    v2 = pulp.LpVariable("v2", lowBound=0)
    u0 = pulp.LpVariable("u0")

    prob += float(row["passes"]) * u + u0

    prob += float(row["teachers"]) * v1 + float(row["rooms"]) * v2 == 1

    for other in df.index:
        o = df.loc[other]
        prob += (float(o["passes"]) * u - float(o["teachers"]) * v1 - float(o["rooms"]) * v2 + u0 <= 0), f"cap_{other}"

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    score = pulp.value(prob.objective)

    peers = []
    for other in df.index:
        slack = prob.constraints[f'cap_{other}'].slack
        if abs(slack) < 1e-6:
            peers.append(other)

    print(dmu, round(score, 3), "u0 =", round(pulp.value(u0), 3), "reference set:", peers)
