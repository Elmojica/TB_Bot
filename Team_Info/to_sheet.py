import openpyxl


players = {
  "Black Corsair": { "Rise Of the Ancients event": 1 },
  "pajaro": {
    "Rise Of the Ancients event": 8,
    "Level 10 Crypt": 6,
    "Level 5 Crypt": 1,
    "Level 10 Citadel": 1,
    "Level 15 Citadel": 1,
    "Level 15 rare Crypt": 1,
    "Level 10 rare Crypt": 1,
    "Level 15 epic Crypt": 1
  },
  "Linilus": { "Rise Of the Ancients event": 1 },
  "Calan": { "Rise Of the Ancients event": 4 },
  "OG Samugor": { "Rise Of the Ancients event": 5 },
  "Orodrafin": { "Rise Of the Ancients event": 9 },
  "Lucky Luna": { "Rise Of the Ancients event": 1 },
  "Blackconjuror": { "Rise Of the Ancients event": 8, "Level 5 Crypt": 1 },
  "Delduen": { "Rise Of the Ancients event": 5 },
  "Elladie": {
    "Rise Of the Ancients event": 8,
    "Level 5 Crypt": 1,
    "Level 15 epic Crypt": 1,
    "Level 10 Crypt": 3
  },
  "Sundsvall": { "Rise Of the Ancients event": 5 },
  "Delabor": {
    "Rise Of the Ancients event": 5,
    "Level 5 Crypt": 7,
    "Level 10 Crypt": 2
  },
  "Tuatara": { "Rise Of the Ancients event": 5 },
  "Robin z Locksley": { "Rise Of the Ancients event": 5 },
  "Knight": {
    "Rise Of the Ancients event": 1,
    "Level 15 Crypt": 1,
    "Level 20 Crypt": 1
  },
  "Bandirgas": {
    "Rise Of the Ancients event": 5,
    "Level 10 Crypt": 2,
    "Level 5 Crypt": 1
  },
  "pin Kan": { "Rise Of the Ancients event": 1 },
  "Lorbrinod": { "Rise Of the Ancients event": 4 },
  "Greenie": { "Rise Of the Ancients event": 5 },
  "Xanthippe Ragewind": { "Rise Of the Ancients event": 8 },
  ", onzie": { "Rise Of the Ancients event": 8 },
  "LolaSleepless": {
    "Rise Of the Ancients event": 1,
    "Level 15 Crypt": 1,
    "Level 5 Crypt": 1
  },
  "grumpy Guppy": { "Rise Of the Ancients event": 5 },
  "RunsWithScissors": { "Rise Of the Ancients event": 8 },
  "Dragonforce": { "Rise Of the Ancients event": 1 },
  "CiHaN": { "Rise Of the Ancients event": 4 },
  "goshmanskaya imperiya": { "Rise Of the Ancients event": 4 },
  "Ayel": {
    "Level 5 Crypt": 2,
    "Level 10 Crypt": 1,
    "Level 10 Citadel": 1,
    "Level 15 Crypt": 1
  },
  "Feli": {
    "Level 5 Crypt": 6,
    "Level 15 Crypt": 4,
    "Level 20 Crypt": 5,
    "Level 10 Crypt": 2,
    "Level 20 epic Crypt": 1
  },
  "ck69": { "Level 15 Citadel": 1, "Level 5 Crypt": 2 },
  "John": { "Level 10 Crypt": 1 },
  "OSMAN": { "Arena": 1, "Level 5 Crypt": 3 },
  "galbine": {
    "Level 5 Crypt": 13,
    "Arena": 3,
    "Level 10 Crypt": 2,
    "Level 20 Crypt": 1,
    "Level 10 rare Crypt": 1,
    "Level 15 Crypt": 1
  },
  "Aykayen": {
    "Level 10 rare Crypt": 1,
    "Level 10 Crypt": 8,
    "Level 15 Crypt": 1,
    "Level 15 epic Crypt": 2
  },
  "Zolotn": { "Level 15 Crypt": 1 },
  "caliNDN": { "Level 10 Crypt": 10 },
  "Gravel beard": { "Level 5 Crypt": 2, "Level 15 Crypt": 2 },
  "StrongArm": {
    "Level 20 epic Crypt": 3,
    "Arena": 3,
    "Level 20 Crypt": 1,
    "Level 25 Crypt": 2,
    "Level 15 rare Crypt": 5
  },
  "Slaine the Beserker": {
    "Level 15 Crypt": 1,
    "Level 10 Crypt": 1,
    "Level 10 rare Crypt": 1
  },
  "Tic Tac": { "Level 10 Crypt": 2 },
  ",Tsogda": { "Level 10 Crypt": 1, "Level 5 Crypt": 9 },
  ",€ein": { "Level 20 Crypt": 2 },
  "SteamrollTrav": { "Clan wealth": 23 },
  "Steamy": {
    "Level 15 epic Crypt": 9,
    "Level 20 epic Crypt": 5,
    "Level 20 Crypt": 1,
    "Level 5 Crypt": 1,
    "Level 20 rare Crypt": 4,
    "Level 20 rare Cryp": 1
  },
  "Ceretius": { "Level 20 Crypt": 2, "Level 20 rare Crypt": 2, "": 1 },
  "VAAL": { "Level 20 Crypt": 1, "Level 20 rare Crypt": 1, "Level 5 Crypt": 1 }
}

#
# Create a new workbook
workbook = openpyxl.Workbook()

# Select the active sheet
sheet = workbook.active

# Write the headers



headers = []

for player in players:
    for key in players[player]:
        # print("key: " + key)
        # print(players[player][key])
        if players[player] not in headers:
            headers.append(key)

headers = list(set(headers))
sheet.append(["Player"] + headers)

# for header in headers:
#     sheet.append([header] + [data.get(header, 0) for data in players.values()])
# workbook.save("test.xlsx")

# Write the data
for player, data in players.items():
    print(player)
    row = [player] + [data.get(header, 0) for header in headers]
    sheet.append(row)

# Save the workbook
workbook.save("test.xlsx")

