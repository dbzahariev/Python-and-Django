class Website:
    def __init__(self, Host, Domain, Inquiries):
        self.Host = Host
        self.Domain = Domain
        self.Inquiries = Inquiries


websites = []
while True:
    data = input().split(' | ')
    if data[0] == 'end':
        break
    host, domain = data[0], data[1]
    inquiries = ''
    if len(data) > 2:
        inquiries = data[2].split(',')
    new_website = Website(host, domain, inquiries)
    websites.append(new_website)

for website in websites:
    result = f'https://www.{website.Host}.{website.Domain}'
    if website.Inquiries[0] != '':
        result += f'/query?=[' + ']&['.join(website.Inquiries) + f']'
    print(result)
