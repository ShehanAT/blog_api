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
    sorted_by = request.GET.get('sorted_by')
    # direction valid fields: asc, desc
    direction = request.GET.get('direction')
    base_url = 'https://api.hatchways.io/assessment/blog/posts'
    requests_arr = []
    post_arr = []
    response_data = {'posts': []}
    if sorted_by != None:
        base_url += "?sorted_by=" + sorted_by 
    if direction != None:
        base_url += "?direction=" + direction 
    if tags != None:
        tag_arr = tags.split(',')
        for tag in tag_arr:
            requests_arr.append(base_url + "?tag=" + tag)
    for request in requests_arr:
        response = requests.get(request)
        data = response.json()
        for post in range(0, len(data["posts"])):
            response_data["posts"].append(data["posts"][post])
    # response_data = json.dumps(post_arr)
    return JsonResponse(response_data, safe=False)
                # response_data["posts"] = data["posts"]
        # except KeyError as e: 
        #     print(e)
        #     return render(request, 'error.html', {
        #             'error': data['error']
        #     })
        