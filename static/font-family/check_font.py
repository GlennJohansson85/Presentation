from fontTools.ttLib import TTFont

p = "Jost-900-Black.woff2"
f = TTFont(p)
n = f["name"].names

def get(nid):
    for r in n:
        if r.nameID == nid and r.platformID in (3, 1):
            try:
                return r.toUnicode()
            except:
                pass
    return None

print("File:", p)
print("Family (nameID 1):", get(1))
print("Subfamily (nameID 2):", get(2))
print("Full name (nameID 4):", get(4))
print("usWeightClass:", f["OS/2"].usWeightClass)
print("Italic flag:", bool(f["OS/2"].fsSelection & 0x01))