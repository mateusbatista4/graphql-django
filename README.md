# graphql-django
GraphQL server with Graphene-Python  

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/mateusbatista4/graphql-django.git
   ```
2. Create a Virtual Enviroment 
   ```sh
   python3 -m venv venv
   ```
3. Install the requirements listed in requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
 
## Usage

Use this space to show useful examples of how to make some graphQL queryes

1. Run the project
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
 

