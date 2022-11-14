import pandas as pd

url = "https://drive.google.com/drive/u/0/folders/0AAfYcSFzOVo2Uk9PVA"
file = "https://docs.google.com/spreadsheets/d/1PA-StzhJWqxBB4P1RdT3aS7pXRgAu-Bvd6EZyhRA6_s/edit#gid=0"
file2 = "https://docs.google.com/spreadsheets/d/1PA-StzhJWqxBB4P1RdT3aS7pXRgAu-Bvd6EZyhRA6_s/edit#gid=0" + file.split('/')[-2]

gDocID = "1PA-StzhJWqxBB4P1RdT3aS7pXRgAu-Bvd6EZyhRA6_s"
sheetID = "Sheet1"

gDoc_Url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gDocID, sheetID)



df = pd.read_csv(gDoc_Url)
# df1 = pd.read_csv(file)
# df2 = pd.read_csv(file2)

print(df.head())