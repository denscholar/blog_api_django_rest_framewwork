# token Authentication
It's concept: Authentication provides for us a way in which we cann identify a request. every request created by Djannngo framework is identified by two things:
1. The user who created it
2. The token that signed it 
Authentication also enable us to protect our end up for us to be able to log in and get ouur access point. 

## steps in creating the Token Authentication
1. Add the rest_framework authentication app to the settings.py - ** rest_framework.authtoken **
2. Add the elow code snipet to the settings.py:
REST_FRAMEWORK = {
    "NON_FIELD_ERRORS_KEY": "errors",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication"
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated"
    )
}
The above code is the authentication settings from rest framwork.

3. We are going to need a way of creating a token and django_rest framework provides for uss a token model that basically creates a token and the token is to be associated with a single user of the appication. for us to e able to do it at siggnin up such that if a user signs up, a token is sent to them which will be used to authenticate their account and login in with their credentials. 

There are sevveral appraoches  to it. one is to within the serializer we created and set it up. another approoach is to create a signal that listens to a user creation and then go ahead and create a token for that specific user. 


## JWT AUTHENTICATION using django simple jwt
