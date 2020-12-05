# graphql-django
GraphQL server with Graphene-Python  


### Getting Started

1. Clone the repo
   ```sh
   git clone https://github.com/mateusbatista4/graphql-django.git
   ```
   
2. Get into the repository
   ```sh
   cd graphql-django
   ``` 

3. Create a Virtual Enviroment 
   ```sh
   python3 -m venv venv
   ```
 
 4. Activate your Virtual Enviroment (differnt for Linux/Windows) 
   ```sh
   source venv/bin/activate
   ```
   
5. Install the requirements listed in requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
 
## Usage

Use this space to show useful examples of how to make some graphQL queryes

1. Run the project at the root repo
   ```sh
   python3 manage.py runserver
   ```
   
2.On your browser access the 'graphlq/' endpoint
   ```sh
   http://localhost:8000/graphql
   ```
   
 3.Make your queryes, as the folloewd example
  ```
   query {
      allMovies {
        id
        name
        category {
          name
        }
      }
    }
  ```
 

