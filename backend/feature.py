import re
import tldextract
import whois
import datetime

class FeatureExtractor:
    def __init__(self, url):
        self.url = url
        self.features = {}
        self.ext = tldextract.extract(url)
        self.domain = self.ext.domain + '.' + self.ext.suffix

    def extract(self):
        self.isIp()
        self.isValid()
        self.activeDuration()
        self.urlLen()
        self.containsAtSymbol()
        self.isRedirect()
        self.haveDash()
        self.domainLen()
        self.numberOfSubdomains()
        return self.features

    def isIp(self):
        self.features['isIp'] = 1 if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', self.ext.domain) else 0

    def isValid(self):
        try:
            whois_info = whois.whois(self.domain)
            self.features['valid'] = 1 if whois_info.status else 0
        except:
            self.features['valid'] = 0

    def activeDuration(self):
        try:
            whois_info = whois.whois(self.domain)
            creation_date = whois_info.creation_date
            if isinstance(creation_date, list):
                creation_date = creation_date[0]
            self.features['activeDuration'] = (datetime.datetime.now() - creation_date).days
        except:
            self.features['activeDuration'] = -1

    def urlLen(self):
        self.features['urlLen'] = len(self.url)

    def containsAtSymbol(self):
        self.features['is@'] = 1 if '@' in self.url else 0

    def isRedirect(self):
        self.features['isredirect'] = 1 if '--' in self.url else 0

    def haveDash(self):
        self.features['haveDash'] = 1 if '-' in self.domain else 0

    def domainLen(self):
        self.features['domainLen'] = len(self.domain)

    def numberOfSubdomains(self):
        self.features['nosOfSubdomain'] = len(self.ext.subdomain.split('.')) if self.ext.subdomain else 0

