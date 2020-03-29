# kaggle-covid19-line-list-backend

This backend serves several APIs that compare an individual's data and symptoms to individual [case-by-case coronavirus data](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset#COVID19_line_list_data.csv).

The current endpoint for these APIs is: https://covid-long-line-api.azurewebsites.net.

## Routes
### GET `/covid/getSymptomPercentagesCountry`
**Example Request Body**
```json
{
	"location": "USA",
	"attributes": {
		"age": 10,
		"gender": "male"
	}
}
```

**Example Response**
```json
{
    "country": "USA",
    "attributePercentages": {
        "age": 0.1,
        "gender": 0.1
    }
}
```

### GET `/covid/getSymptomPercentagesState`
**Example Request Body**
```json
{
	"location": "USA",
	"attributes": {
		"age": 10,
		"gender": "male"
	}
}
```

**Example Response**
```json
{
    "state": "USA",
    "attributePercentages": {
        "age": 0.2,
        "gender": 0.2
    }
}
```

### GET `/covid/getSymptomPercentagesCounty`
**Example Request Body**
```json
{
	"location": "USA",
	"attributes": {
		"age": 10,
		"gender": "male"
	}
}
```

**Example Response**
```json
{
    "state": "USA",
    "attributePercentages": {
        "age": 0.2,
        "gender": 0.2
    }
}
```

### GET `/covid/getSymptoms`
No request body needed.

**Example Response**
```json
{
    "symptoms": [
        "da flu",
        "da corona"
    ]
}
```

### GET `/covid/getCountries`
No request body needed.

**Example Response**
```json
{
    "countries": [
        "da usa",
        "ooo canada"
    ]
}
```

### GET `/covid/getStates`
No request body needed.

**Example Response**
```json
{
    "states": [
        "wurshingtun",
        "kanto"
    ]
}
```

### GET `/covid/getCounties`
No request body needed.

**Example Response**
```json
{
    "counties": [
        "king",
        "queen",
        "pallet town"
    ]
}
```