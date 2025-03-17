import requests
from django.shortcuts import render


my_ApiKey = "vhc7IDKs3rcQuOGAEf77zWhVtZDFbGCg"

def get_events(request):
    city = request.GET.get("city", "Miami")  

    url = f"https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "city": city,
        "apikey": my_ApiKey,
        "size": 10,  
    }

    response = requests.get(url, params=params)
    data = response.json()

    events = []
    if "_embedded" in data:
        for event in data["_embedded"]["events"]:
            events.append({
                "name": event["name"],
                "date": event["dates"]["start"]["localDate"],
                "url": event["url"],
                "image": event["images"][0]["url"] if event.get("images") else "",
            })

    return render(request, "app/base.html", {"events": events, "city": city})