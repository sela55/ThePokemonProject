# Pokemon API Test Suite

## Setup

* .Install Python if not already installed.
* .Install required dependencies using the following command:

    ```bash
    pip install pytest requests
    ```
* .Run the tests:

    ```bash
    pytest -v test_pokemon_api.py
    ```

## Tests:

### Question 1
Test the number of unique Pokemon types returned by the API using a Set data structure.

### Question2 
Test if specific Pokemon names are present in the list of fire-type Pokemon using Data-Driven Testing (DDT).

### Question 3
Test the weight of specific fire-type Pokemon and ensure they are in the top 5 heaviest using Data-Driven Testing (DDT).
The conditional statement is used to connect to the API only in the first iteration to reduce time.


## Additional Information
The test suite includes three main test cases.
The code uses a class (TestPokemonApi) with a class-level setup method to reduce the number of API connections and store information for mutual use between tests.
