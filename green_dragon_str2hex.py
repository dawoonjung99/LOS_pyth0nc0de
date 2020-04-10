data = " union select 0x61646d696e#"
for i in data:
    print(hex(ord(i)).split("0x")[1])
