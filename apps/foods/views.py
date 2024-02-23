from django.shortcuts import render

# Create your views here.
def foods_create(request):
    if request.method == 'GET':
        if food = Food.object.get(user.id == request.user.id): 
            cnt = {
                'food' : food 
            }
            render( cnt)
        else:
            get_food(request.user)


def foods_detail():

def foods_update():

def foods_delete():
