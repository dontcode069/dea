import pulp
from data import df

for dmu in df.index:
    row = df.loc[dmu]

    prob = pulp.LpProblem(f"CCR_{dmu}", pulp.LpMaximize)
    u = pulp.LpVariable("u", lowBound=0)
    v1 = pulp.LpVariable("v1", lowBound=0)
    v2 = pulp.LpVariable("v2", lowBound=0)

    prob += float(row["passes"]) * u

    prob += float(row["teachers"]) * v1 + float(row["rooms"]) * v2 == 1

    for other in df.index:
        o = df.loc[other]
        prob += float(o["passes"]) * u - float(o["teachers"]) * v1 - float(o["rooms"]) * v2 <= 0

    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    print(dmu, round(pulp.value(prob.objective), 3))