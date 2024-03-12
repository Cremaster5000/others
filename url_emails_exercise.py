"""Given a list of emails and URLs, return a dictionary,where each key is a URL 
and the value is how many emails have the same domain. Note
that the domains begin with www. whereas the emails do not, and that emails
with domains not in the list of urls should be ignored"""

count_email_domains = {
					'emails' :['foo@a.com', 'bar@a.com', 'baz@b.com', 'qux@d.com'],
					'urls' : ['www.a.com','www.b.com', 'www.c.com']}
final_dict = {}

def createDict():
	for url in count_email_domains['urls']:
		final_dict[url] = countEmails(url)


def countEmails(url: str)->int:
	total = 0
	for email in count_email_domains['emails']:
		domi = email.split('@')[1]
		if url.find(domi)>=0: total +=1
	return total



createDict()
print(final_dict)
