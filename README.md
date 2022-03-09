# Sentiment-Analysis-Bahasa-Indonesia

###
This project is created to predict the sentiment of a sentence or list of sentences in Bahasa Indonesia.

### JSON Structure:
```
{
	"text": (query),
	"text_sentiment": (sentiment of the text/query)
}
```

### Output:
Output is in the form of ```payload``` in JSON form.

# How to Use:
## API Endpoints:
### Predicting the sentiment of a string of text:
``` {url}/predict/sentimentone ```
### Predicting the sentiment of a list of texts:
``` {url}/predict/sentimentlist ```

## Example of Usages:
### /sentimentone
**Input:**
```
{
	"query": "Saya suka sekali dengan coklat ini. Mungkin bakal coba beli minggu depan"
}
```
**Output:**
```
{
	"status": 200,
	"message": "OK",
	"payload": {
		"query": "Saya suka sekali dengan coklat ini. Mungkin bakal coba beli minggu depan",
		"text_sentiment": "positive"
	}
}
```
### /sentimentlist
**Input:**
```
{
	"query": [
		"Saya suka sekali dengan coklat ini. Mungkin bakal coba beli minggu depan",
		"Apel ini pahit banget. Kok bisa?",
		"Aku ternyata dapat juara satu loh!",
		"Sudah dibilang apa, jangan pergi ke sana. Bahaya!"
	]
}
```
**Output:**
```
{
	"status": 200,
	"message": "OK",
	"payload": {
		"results": [
			{
				"text": "Saya suka sekali dengan coklat ini. Mungkin bakal coba beli minggu depan",
				"text_sentiment": "positive"
			},
			{
				"text": "Apel ini pahit banget. Kok bisa?",
				"text_sentiment": "negative"
			},
			{
				"text": "Aku ternyata dapat juara satu loh!",
				"text_sentiment": "positive"
			},
			{
				"text": "Sudah dibilang apa, jangan pergi ke sana. Bahaya!",
				"text_sentiment": "negative"
			}
		]
	}
}
```




