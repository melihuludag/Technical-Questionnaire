import re
import pandas as pd

d = {'Device_Type': ["AXO145", "TRU151" ,"ZOD231" ,"YRT326","LWR245"], 'Stats_Access_Link':["<url>https://xcd32112.smart_meter.com</url>", "<url>https://tXh67.dia_meter.com</url>","<url>https://yT5495.smart_meter.com</url>","<url>https://ret323_TRu.crown.com</url>","<url>https://kuwr3243.celcius.com</url>"]}
df = pd.DataFrame(data=d)

pattern = re.compile(r'<url>https://(\S+)</url>')

for item in df["Stats_Access_Link"]:
    result=re.search(pattern,item)
    link = result.group(1)
    print(link.lower())
