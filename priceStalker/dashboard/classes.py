class Form:

    def __init__(self, form):
        self.form = form
        self.valid = False

    def saveRecord(self, request):
        if isValid(request):
            newRecord = form.save()

            return newRecord

    def isValid(self, request):
        if request.method == 'POST':
            if form.is_valid():
                self.valid = True
        return self.valid
