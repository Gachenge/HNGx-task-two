build a rest api that supports CRUD operations on a person resource

This api has been built using python flask. Using an ORM - sqlalchemy, makes database to python interaction smooth.
It relies on mysql database to store and retrieve data.

The api is hosted on pythonanywhere and can be accessed at:
    https://gachenge.pythonanywhere.com/
    The endpoint to get a list of all people in the databasde is at: https://gachenge.pythonanywhere.com/api/all
    
    Add a new person
    https://gachenge.pythonanywhere.com/api, with a post request. All we need is a name to add. Structure the data as
    a key, value pair eg, {'name': "Michael Essien"}.
    With this, Michael Essien is added to the database, and a unique id is automatically generated for him.

    Access a specific user
    https://gachenge.pythonanywhere.com/api/person/<user_id>, This endpoint will lead you to a specific user, where you
    can view the details of a specific user.

    Update a specific user
    https://gachenge.pythonanywhere.com/api/person/<user_id>. This endpoint, accessed with a put request, one is able
    to update a user's name. Simiolarly, this endpoint should also be accessed with a dictionary, the dictionary should
    contain the new name eg. {'name': 'Mike Essien'}

    Delete a user
    https://gachenge.pythonanywhere.com/api.person/<user_id>. Delete any user with their user_id.
