import requests
import time
from datetime import datetime
from dhooks import Webhook, Embed

url = "https://www.digikey.com/products/api/v4/pricing/15194699"
headers = {'x-currency': 'USD', 'accept-language': 'en-us'}

hook = Webhook('https://discord.com/api/webhooks/658061206548119562/0k4VOMro53L3mCjFOTfgJgIYqeFvuBA6BAyC-Ol2exL9ijspMGf0hcJspKtP0at4h1he')

embed = Embed(
  description='DigiKey restock SenseCap for immediate delivery!',
  color=0x5CDBF0,
  timestamp='now'
  )

embed.add_field(name='Click this link', value=url)

print ("Start Monitoring "+url+ " @ "+ str(datetime.now()))
while True:
    resp = requests.get(url, headers=headers)
    resp = resp.json()
    messages = resp['data']['messages']
    messages = str(messages)
    if messages == "[{'message': '0 In Stock', 'type': 'title', 'code': '3'}, {'message': 'Import Tariff may apply to this part if shipping to the United States', 'type': 'tariff', 'code': '41'}, {'message': 'Due to temporary constrained supply, Digi-Key is unable to accept backorders at this time.', 'type': 'qtyAvailableNotes', 'code': '20'}]":
        print("No Change " + str(datetime.now()))
    else:
        hook.send(embed=embed)
        print("Detected change @ " + str(datetime.now()))