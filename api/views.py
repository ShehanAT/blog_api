from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer 
from django.http import JsonResponse
from .models import Post 
import requests
import json
# Create your views here.
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().order_by('id')
#     serializer_class = PostSerializer

def home(request):
    base_url = 'https://api.hatchways.io/assessment/blog/posts'
    tag = '?tag=tech'
    response = requests.get(base_url + tag)
    data = response.json()
    try:
        if len(data['posts']) > 0:
            return render(request, 'home.html', {
            'data': data['posts']
        })
    except KeyError as e: 
        print(e)
        return render(request, 'error.html', {
                'error': data['error']
        })

def ping_view(request):
    data = {
        "success": "True"
    }
    return JsonResponse(data)

def posts_view(request):
    tags = request.GET.get('tags')
    # sorted_by valid fields: id, reads, likes, popularity
    sorted_by = request.GET.get('sortedBy')
    # direction valid fields: asc, desc
    direction = request.GET.get('direction')
    base_url = 'https://api.hatchways.io/assessment/blog/posts'

    requests_arr = []
    post_arr = []
    tag_arr = []
    response_data = {'posts': []}
    if tags != None:
        tag_arr = tags.split(',')
        for tag in tag_arr:
            requests_arr.append(base_url + "?tag=" + tag + "&")
    if sorted_by != None:
        if sorted_by != 'id' and sorted_by != 'reads' and sorted_by != 'likes' and sorted_by != 'popularity':
            return JsonResponse({"error": "sortBy parameter is invalid"})
        else: 
            for i in range(0, len(requests_arr)):
                requests_arr[i] = requests_arr[i] + "sortedBy=" + sorted_by

    if direction != None:
        if direction != 'asc' and direction != 'desc':
            return JsonResponse({"error": "direction parameter is invalid"})
        else:
            for i in range(0, len(requests_arr)):
                requests_arr[i] = requests_arr[i] + "direction=" + direction

    else: 
        requests_arr.append(base_url)
    for request in requests_arr:
        response = requests.get(request)
        data = response.json()
        try: 
            for post in range(0, len(data["posts"])):
                response_data["posts"].append(data["posts"][post])
        except KeyError as e:
            print(e)
            return JsonResponse(data)
    if sorted_by != None: 
        if direction == "asc":
            response_data["posts"] = sorted(response_data["posts"], key=lambda k: k.get(sorted_by, 0))
        elif direction == "desc":
            response_data["posts"] = sorted(response_data["posts"], key=lambda k: k.get(sorted_by, 0), reverse=True)
        return JsonResponse(response_data, safe=False)
    return JsonResponse(response_data, safe=False)

        