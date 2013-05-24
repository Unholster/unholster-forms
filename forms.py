class form(dict):
    def referer_allowed(self, referer):
        return referer in self.get('referers', [])