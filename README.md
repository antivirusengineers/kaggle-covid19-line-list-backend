# kaggle-covid19-line-list-backend

This backend serves several APIs that compare an individual's data and symptoms to individual [case-by-case coronavirus data](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset#COVID19_line_list_data.csv).

The current endpoint for these APIs is: https://covid-long-line-api.azurewebsites.net.

## Routes
### GET `/covid/prevalence`
**Example Request Body**
```json
{
	"attributes": {
		"age": 10,
		"gender": "male"
		"symptom_list": ["cough", "fever"],
		"country": USA 
	}
	"additional_args": {
		"age": 
		{
			"span": 5
		}
	}
	"localization": "country"
}
```

**Example Response**
```json
{
    "percentage": 0.075
}
```

### GET `/covid/symptom-list`
No request body needed.

**Example Response**
```json
    [
        "fever",
        "cough", 
	"headache",
	...
    ]
```

### GET `/covid/country-list`
No request body needed.

**Example Response**
```json
    [
        "Canada",
        "USA",
	...
    ]

```

### GET `/covid/gender-list`
No request body needed.

**Example Response**
```json
    [
        "female",
        "male"
    ]

```
