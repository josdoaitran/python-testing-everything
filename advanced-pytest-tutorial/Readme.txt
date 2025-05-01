# Lessons in Advanced Pytest Tutorial

 - Fixture Optimization
 - Parametrization Techniques
 - Custom Markers and Filtering
 - Advanced Assertions
 - Plugins and Extensions

 ## 1. Fixture Optimization

Use scope parameters (function, class, module, session) to control fixture lifecycle
Implement fixture factories that return functions for customizable setups
Use the autouse=True parameter for fixtures that should always run
```python
python@pytest.fixture(scope="session")
def database_connection():
    conn = create_connection()
    yield conn
    conn.close()
```

## 2. Parametrization Techniques

Parametrize tests to run against multiple inputs
Use ids for better test naming in reports
Combine parametrization with fixtures for complex scenarios
```python
python@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16)
], ids=["square of 1", "square of 2", "square of 3", "square of 4"])
def test_square(input, expected):
    assert input**2 == expected
```

## 3. Custom Markers and Filtering

Create custom markers to categorize tests
Use marker expressions to select test subsets
Apply markers at module level with pytestmark
```python
python@pytest.mark.slow
def test_complex_calculation():
    # Run with: pytest -m slow
    ...
```    
## 4. Advanced Assertions

Use pytest.raises for exception testing with context management
Implement custom assertion helpers for domain-specific validation
Leverage pytest.approx() for floating-point comparisons
```python
pythondef test_exception_details():
    with pytest.raises(ValueError) as excinfo:
        raise ValueError("Invalid input")
    assert "Invalid input" in str(excinfo.value)
```    
## 5. Plugins and Extensions

Utilize plugins like pytest-xdist for parallel testing
Implement conftest hooks for custom test behavior
Create your own fixtures and plugins for reusable test components