from rest_framework import generics, status
from rest_framework.response import Response
from .models import Device, StatusActivity
from django.db.models import Subquery, OuterRef
from django.db.models import Count, Max, Min
from .serializers import *

class DeviceListView(generics.ListAPIView):
    queryset = Device.objects.annotate(
    status=Subquery(
        StatusActivity.objects.filter(
            device_id=OuterRef('pk')
        ).order_by('-modified_at').values('status')[:1]
    ),
    modified_at=Subquery(
        StatusActivity.objects.filter(
            device_id=OuterRef('pk')
        ).order_by('-modified_at').values('modified_at')[:1]
    ),
).values('id', 'device_name', 'status', 'modified_at')

    serializer_class = DeviceStatusListSerializer

#alternative:
#queryset = StatusActivity.objects.values('device_id__device_name').annotate(Max('modified_at'))
        
    for item in queryset:
        print(item)
        print("\n")
#     serializer_class = DeviceStatusListSerializer


class StatusUpdateView(generics.CreateAPIView):
    queryset = StatusActivity.objects.all()
    serializer_class = DeviceStatusUpdateSerializer
    def create(self, request, *args, **kwargs):
        super(StatusUpdateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)


