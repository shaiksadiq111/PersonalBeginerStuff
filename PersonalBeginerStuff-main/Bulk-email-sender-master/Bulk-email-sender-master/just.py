import json

full_batch = [f"bt20cse00{item}@iiitn.ac.in" for item in range(1, 10)]
for i in range(10, 100):
    id = f"bt20cse0{i}@iiitn.ac.in"
    full_batch.append(id)
for i in range(100, 205):
    id_ = f"bt20cse{i}@iiitn.ac.in"
    full_batch.append(id_)
secA = [f"bt20cse00{item}@iiitn.ac.in" for item in range(1,10)]
for i in range(10, 69):
    id__ = f"bt20cse0{i}@iiitn.ac.in"
    secA.append(id__)
secB = [f"bt20cse{item}@iiitn.ac.in" for item in range(69,100)]
for i in range(100, 137):
    _id__ = f"bt20cse0{i}@iiitn.ac.in"
    secB.append(_id__)

secC = [f"bt20cse{item}@iiitn.ac.in" for item in range(137, 205)]
data = {
    "CSE": full_batch,
    "CSE-A": secA,
    "CSE-B": secB,
    "CSE-C": secC,
}
with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)
