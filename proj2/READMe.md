# Django

   pip install django
    
    pip install django_restframework
  
 # start the project
 
    django-admin startproject project
 
 # create app into project
 
    python manage.py startapp app
    
# Model Creating
   
 1. Here we have to create models (models.py)

 2. And Create tables 

 3. Its creating tables 

         DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'newproject',
                'USER': 'root',
                'PASSWORD': 'sam8778',
                'HOST': 'localhost',
                'PORT': '3306'
            }
         }
         
         
   # Serializer
        
       1. Create a file name serializer.py
       2. And Implement all Models in Serializers ,each and every models have seperate classes.
       
   # CRUD application
             
             views.py 
             
          Here we create our view functions 
          1.POST , 2.GET ,3.PUT  ,4.DELETE
          
  # Rest Frame Work
  
          rest_framework
          
       here is keyword to implement on INSTALLED_APPS in settings.py
       
       and to mentioned decorators to the framework creates the UI of your function.
   
   # swagger
           
  dsrf_yasg
           
      To include this command on INSTALLED_APPS
      
      and to insert the configuratioins of swagger on app/urls.py
      
            schema_view = get_schema_view(
                   openapi.Info(
                                    title="MATC project",
                                    default_version='v1',
                                    description="Django CRUD",

                                 ),
                                     public=True,
                                     permission_classes=[permissions.AllowAny],
                                     )

             path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
             path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

Above mentioned paths helps to view the swagger UI.


# Logging
         
  logging config to inplement in settings.py
         
        
          LOGGING = {
                      'version': 1,
                      'disable_existing_loggers': False,
                      'formatters': 
                      'verbose': {
                      'format': '{levelname} {asctime} {module}{message}',
                              'style': '{',
              },

            'handlers': {
                              'file': {
                                            'level': 'DEBUG',
                                            ‘class': 'logging.FileHandler',
                                             'filename': '/path/to/django/debug.log',
                                             },'loggers': {
          'django': {
                'handlers': ['file'],'level': 'DEBUG','propagate': True, },    },


message's about your Flask application are logged on res.log
      
  # JWT    
    To add this comment on settings.py

                             REST_FRAMEWORK = {
              'DEFAULT_AUTHENTICATION_CLASSES': [
                  'rest_framework_simplejwt.authentication.JWTAuthentication',
              ],
          }
  
     And to insert some urls in project/urls.py
     
               urlpatterns = [
              path('api/token/',
                   jwt_views.TokenObtainPairView.as_view(),
                   name='token_obtain_pair'),
              path('api/token/refresh/',
                   jwt_views.TokenRefreshView.as_view(),
                   name='token_refresh'),
                   
      # To implement the token on function 
                 
                Set permission class for IsAuthenticated  helps to protect our data. This helps to protect our functions,
         And access the data only the authorised persons only.
         
         
# Celery 
     
     1.    Celery, it's creating queue behind the functions and to insert the timings of the functions.
           Here, my application  i have create some functions and that functions will executing by some duration of times.
    
     2.   And the RabbitMQ it's working a message brokers, If you send a message it will go through the RabbitMq and its creates celery workers,
     
     3.   So the celery workers to implement the functions depends upon seleted queue.
     
 # Pagination
    
     1 . Paginatin helps to split the results,
         
         And the config is,
       
            REST_FRAMEWORK = {
                'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberSetPagination',
                'PAGE_SIZE': 100
            }
            
            
# Unittest

      1.  Django’s unit tests use a Python standard library module: unittest. This module defines tests using a class-based approach.
                         
      2. Subclasses from django.test.TestCase, which is a subclass of unittest.Testcase  That runs the each test inside the class.

         
