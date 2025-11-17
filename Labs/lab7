Query 1:
{
  "year": { "$gt": 1990 },
  "cast": "Tom Hanks",
  "genres": "Comedy",
  "imdb.rating": { "$gt": 7.5 },
  "metacritic": { "$gt": 80 }
}
Answer 1:
Toy Story, Toy Story 2, Toy Story 3

Query 2:
{
  "rated": "R",
  "genres": "Sci-Fi",
  "cast": "Arnold Schwarzenegger",
  "fullplot": { "$regex": "hunt", "$options": "i" },
  "imdb.rating": { "$gt": 6 },
  "metacritic": { "$lt": 40 }
}
Answer 2:
No matching documents found in the sample_mflix dataset.

Query 3:
{
  "rated": "G",
  "runtime": 100,
  "$or": [
  "fullplot": { "$regex": "dog", "$options": "i" }
}
Answer 3:
No matching documents found in the sample_mflix dataset.

Part 2

Part 3

1. How many patients are diagnosed with:
   Flu: 18
   Common Cold: 12
   Pneumonia: 9
   Migraine: 7
   Asthma: 6
   Undiagnosed: 8

2. Top 2 average symptom features for Flu patients:
   fever, cough

3. Patient closest to Pneumonia centroid:
   P029 (Pneumonia)

4a. Fraction of patients within distance 3.0 of their diagnosis centroid:
   0.90

4b. Number of 'Undiagnosed' patients closer to 'Migraine' centroid than their own:
   0

5. Three nearest neighbors for patient P010:
   P009 (Migraine)
   P031 (Migraine)
   P003 (Migraine)
