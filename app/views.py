from django_tables2 import SingleTableView
from .models import Upfront
from .tables import UpfrontTable


class IndexView(SingleTableView):
    queryset = Upfront.objects.all()
    table_class = UpfrontTable
    template_name = 'index.html'
