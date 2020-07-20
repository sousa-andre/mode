from django.db.models import Q


class MultipleObjectFilterMixin:
    filter_columns = []
    filter_slug = 'filtro'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_string = self.request.GET.get(self.filter_slug)
        if filter_string is None:
            return queryset

        conditions = [Q(**{column+'__contains': filter_string}) for column in self.filter_columns]
        condition = conditions.pop()
        for item in conditions:
            condition |= item

        queryset = super().get_queryset().filter(condition)
        print(queryset.query)
        return queryset
