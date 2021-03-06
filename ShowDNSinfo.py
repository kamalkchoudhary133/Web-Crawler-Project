import dns.resolver

dns_info = dns.resolver.query('links', 'A')
for ip_value in dns_info:
    print('A Record : ', ip_value.to_text())

NS_info = dns.resolver.query('links', 'NS')
for values in NS_info:
    print('NS Record : ', values.to_text())

MX_info = dns.resolver.query('links', 'MX')
for MX_value in MX_info:
    print('MX Record : ', MX_value.to_text())

SOA_info = dns.resolver.query('links', 'SOA')
for SOA_value in SOA_info:
    print('SOA Record : ', SOA_value.to_text())