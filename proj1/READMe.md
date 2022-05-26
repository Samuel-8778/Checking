# flask

# create the virtual enviroment  

    python3 -m venv project
    
    source project/bin/activate
   
# Implement ORM models 

Create models based on flask – mysql    (models.py)
 
   ORM models creates three tables 
          
          
          1.Employee
          2.Person    
          3.Address
          
 Create Relationship between tables
                 
                 1.Employee  - Person(one-one)
                 2. Employee – AddressI(one to many)

                 
                 And also implemented the fetchings on relationship instances
                 
 Now we fetching the employee_id (dynamic)to connect the Person table and to allows to use seperate query.
 And joined is to connect the two tables and helps to retrive any value between the tables.
 
 # CRUD Application
 
 CRUD   (views.py)
 
          Here , to create a CRUD application and create some types of methods here
          
    • POST
    • GET
    • PUT
    • DELETE
 # Documentaion through Swagger
  To configure our swagger in config.py file
 
         http://localhost/swagger
   
  We will create an json/yml file for swagger ui , its replicate our functions on UI.
  (swagger.json) is help to create the swagger UI.
    
 
 # JWT for user authentication
   jwt is implemented on user_auth.py 
   
                   Here I am oppointed Admin to access all the data, So to create a token based on Admin employee_id , and to generate a token by encoding format.
     If the Admin to Access the data the token will help him.But some other’s  are not allowed on this session.
     Then to decoding the token based on Admin employee_id and will take the employee_id, And to put @token_required decorator to helps to protect the function.
     
     
# Tracing with Jaeger
   
     
                      1. We config our jaeger on config.py
                      2. And to set app and views and auth_views on initialize_tracer
                          and also to create span on each and every function for trace what you do
     1.So to create admin log() function to encode the token.
           (     Headers - mention the algorithem, and Payload – Authorised person details and security_key)
     2.And token_required()   function to decode out token .
     3.So where ever you want to  set the protection, so use @token_required decorator
     
# logging
     
                   1. we config our logging on config.py
                      here we set message-format and level and mention the logfile 
                   2. So where ever you want to show the log message to mention that comments.
                   3.message about your Flask application are logged on res.log
                   
                                      
# Pagination 
             Here,our output has been show by pages and to co-ordinate the views, and split the views on multiple pages.
             Page number will given the url .
             
# Exception Handling
              
              IN my app, I used Exception Handling for to avoid some errors displaying with the help of EH.
              
              1. Try 2.Except 
# Code coverage

              Its helps to cover our application to generate the report.
              The report depends upon a Execution of our functions.
              
             
                   

 
 
