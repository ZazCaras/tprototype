This project is a prototype application for sentiment analysis in news articles. It classifies content gathered from multiple sources through web scraping, using neural networks to determine sentiment and categorize them on "negative", "neutral" or "positive".

## Setup

Follow the steps below to get the project up and running locally.

### Backend Setup

```
cd back
sudo docker compose build
sudo docker compose up -d
```

### Frontend Setup
```
cd front
npm install
npm run dev
```
