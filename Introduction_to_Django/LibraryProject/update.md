Book.objects.get(title='1984').title="Nineteen Eighty-Four"
Book.objects.get(title='Nineteen Eighty-Four').save()