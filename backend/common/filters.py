# # filters.py
# import django_filters
# from .models import BusinessProblem


# class BusinessProblemFilter(django_filters.FilterSet):
#     created_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
#     created_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

#     class Meta:
#         model = BusinessProblem
#         fields = ['status']  # exact-match filter: ?status=pending_ai