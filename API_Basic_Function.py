import requests
def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    # it will only return if request.get succeeds
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url

#print(requestURL(some_base_url, some_params_dictionary))
paramama = {"q":"violins and guitars", "tbm":"isch"}
baseURL = "https://www.google.com/search"
fullURL=requestURL(baseURL,paramama)
print(fullURL)

newurl=requestURL("https://icanhazdadjoke.com/",params={"text":"plain"},headers={"Accept":"application/json"})
print(newurl)

dadjoke=requests.get(newurl)
raw_joke = dadjoke.json()
print(dadjoke.text)