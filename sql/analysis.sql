USE shopeasy;

-- 1) Total customers
SELECT COUNT(*) AS total_customers FROM customers;

-- 2) Total products
SELECT COUNT(*) AS total_products FROM products;

-- 3) Total reviews + avg rating (if column exists)
SELECT COUNT(*) AS total_reviews, ROUND(AVG(Rating),2) AS avg_rating
FROM customer_reviews;

-- 4) Top 5 products by avg rating
SELECT ProductID, ROUND(AVG(Rating),2) AS avg_rating, COUNT(*) AS review_count
FROM customer_reviews
GROUP BY ProductID
ORDER BY avg_rating DESC
LIMIT 5;

-- 5) Bottom 5 products by avg rating
SELECT ProductID, ROUND(AVG(Rating),2) AS avg_rating, COUNT(*) AS review_count
FROM customer_reviews
GROUP BY ProductID
ORDER BY avg_rating ASC
LIMIT 5;

-- 6) Overall engagement (proxy metric)
SELECT
  COUNT(*) AS total_engagement_rows,
  SUM(COALESCE(Likes,0)) AS total_likes,
  ROUND(AVG(COALESCE(Likes,0)), 2) AS avg_likes_per_record
FROM engagement_data;

-- 7) Engagement by Content Type
SELECT
  ContentType,
  COUNT(*) AS records,
  SUM(COALESCE(Likes,0)) AS total_likes
FROM engagement_data
GROUP BY ContentType
ORDER BY total_likes DESC;

-- 8) Top 10 Products by Engagement
SELECT
  ProductID,
  SUM(COALESCE(Likes,0)) AS total_likes,
  COUNT(*) AS engagements
FROM engagement_data
GROUP BY ProductID
ORDER BY total_likes DESC
LIMIT 10;

-- 9) Top 10 Campaigns by Engagement
SELECT
  CampaignID,
  SUM(COALESCE(Likes,0)) AS total_likes,
  COUNT(*) AS engagements
FROM engagement_data
GROUP BY CampaignID
ORDER BY total_likes DESC
LIMIT 10;

-- 11) Customers by geography (if customers has GeographyID)
SELECT c.GeographyID, COUNT(*) AS customers
FROM customers c
GROUP BY c.GeographyID
ORDER BY customers DESC;