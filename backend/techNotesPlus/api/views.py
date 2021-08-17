from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import *
from decouple import config

'''
get all API endpoints
method: GET

'''
@api_view(['GET'])
def api_main(request):
    api_urls = {
        'All users': 'users/all',
        'All notes': 'notes/all',
        'User register': 'user/register',
        'User login': 'user/login',
        'User delete': 'user/delete',
        'Note create': 'create/note',
        'Note delete': 'delete/note',
        'Get all notes by a specific user': 'user/<str:fk>/notes'
    }

    return Response(api_urls)

'''
get all the users
method: GET

'''
@api_view(['GET'])
def get_all_users(request):
    users = User.objects.filter(is_staff=False, is_superuser=False)
    user_serializer = UserSerializer(users, many=True)
    return Response(user_serializer.data)


'''
get all the notes from all the users
method: GET

'''
@api_view(['GET'])
def get_all_notes(request):
    notes = NOTE.objects.all()
    note_serializer = NoteSerializer(notes, many=True)

    return Response(note_serializer.data)


'''
Register a user
method: POST
@:param-> 
{
    'username': String,
    'email': String
    'password': String,
    
}
'''
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register_user(request):
    user = User.objects.create_user(username=request.data['username'], email=request.data['email'], password=request.data['password'])
    user.save()
    return Response(200)



'''

Get the notes of a specific users
method: GET

'''
@api_view(['GET'])
def get_notes_for_user(request):
    notes = NOTE.objects.filter(CREATED_BY=request.user.id)

    note_serializer = NoteSerializer(notes, many=True)

    return Response(note_serializer.data)


'''
Get the current logged in user details
method: GET
'''
@api_view(['GET'])
def get_current_user(request):
    user = User.objects.get(id=request.user.id)
    user_serializer = UserSerializer(user, many=False)
    return Response(user_serializer.data)


'''
Delete a user
method: DELETE

'''
@api_view(['DELETE'])
def delete_user(request):
    try:
        user = User.objects.get(id=request.user.id)
    except:
        return Response(400)

    user.delete()

    return Response(200)


'''
Create a note
method: POST
@:param-> 
{
    'content': String,
  
}
'''
@api_view(['POST'])
def create_note(request):
    note = NOTE(CREATED_BY=request.user, CONTENT=request.data['content'])

    note.save()
    serialized = NoteSerializer(note, many=False)

    return Response(serialized.data)


'''
Get a specific note
method: POST
@:param-> 
{
    'content': String,

}
'''
@api_view(['GET'])
def get_note(request, note_id):
    note = NOTE.objects.get(id=note_id)
    note_serializer = NoteSerializer(note, many=False)
    return Response(note_serializer.data)

'''
Delete a specific note
method: DELETE
'''
@api_view(['DELETE'])
def delete_note(request, note_id):
    try:
        note = NOTE.objects.get(id=note_id)
    except:
        return Response(400)

    note.delete()

    return Response(200)



'''
Update a specific note
method: PUT
@:param-> 
{
    'content': String,

}
'''
@api_view(['PUT'])
def update_note(request, note_id):
    try:
        note = NOTE.objects.get(id=note_id)
    except:
        return Response(400)

    note.CONTENT = request.data['content']

    note.save()

    return Response(200)



'''
Log out from the system
method: GET
'''
@api_view(["POST"])
def sign_out(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response


'''
This function is not applied on the frontend yet. I couldn't use Sendgrid due to their new account
creating policy, it takes a lot of time to verification. Instead I use mailjet to get the job done.
'''
def email(request):
    from mailjet_rest import Client
    import os
    api_key = config('api_key')
    api_secret = config('api_secret')
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "shourav6688@gmail.com",
                    "Name": "Mahabub"
                },
                "To": [
                    {
                        "Email": "shourav6699@gmail.com",
                        "Name": "Mahabub"
                    }
                ],
                "Subject": "Hey, Check this note",
                "TextPart": "",
                "HTMLPart": "<h3>Check this note out at <a href='https://techcare.co/'> TechNotesPlus</a>!</h3><br />",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())





