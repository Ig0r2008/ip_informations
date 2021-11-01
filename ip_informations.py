import ipinfo

access_token = "cdcf53103a55ae"
handler = ipinfo.getHandler(access_token)

ip_address = 'put the ip here'
details = handler.getDetails(ip_address)

print(details.all)