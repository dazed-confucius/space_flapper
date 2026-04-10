import urllib.request
import json
try:
    req = urllib.request.Request("https://en.wikipedia.org/w/api.php?action=query&titles=International_Space_University&prop=pageimages&format=json&pithumbsize=500", headers={"User-Agent": "Mozilla/5.0"})
    resp = urllib.request.urlopen(req, timeout=5).read()
    print(json.loads(resp)["query"]["pages"])
except Exception as e:
    print(e)
