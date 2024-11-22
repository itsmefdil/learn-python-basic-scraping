import pandas as pd

states = ["Indonesia", "Malaysia", "Singapore", "Thailand", "Vietnam"]
population = [273523615, 32365999, 5850342, 69799978, 97338579]


dict_states = {"States": states, "Population": population}

df_states = pd.DataFrame.from_dict(dict_states)

print(df_states)
df_states.to_csv("states.csv", index=False)

# print(states[-4])

# for state in states:
#     # print(state)
#     if state == "Singapore":
#         print(state)

# with open("test.txt", "w") as file:
#     file.write("Data Succesfully Scraped!")
