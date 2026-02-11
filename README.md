# DATA221Assignment2This repository contains the solutions for **DATA221 Assignment 2** (Questions 1–10).  
Questions Overview

- **Question 1** – Read `sample-file.txt`, clean the text (lowercase, remove punctuation, keep tokens with ≥2 letters), and print the 10 most frequent words.  

- **Question 2** – From `sample-file.txt`, clean the text, generate bigrams (pairs of consecutive words), and print the 5 most frequent bigrams.  

- **Question 3** – Identify near-duplicate lines in `sample-file.txt` after normalizing text (lowercase, remove spaces and punctuation). Print the number of near-duplicate sets and the first two sets with line numbers.  

- **Question 4** – Filter `student.csv` for students with `studytime ≥ 3`, `internet = 1`, and `absences ≤ 5`. Save the filtered dataset to `high_engagement.csv` and print the number of students and their average grade.  

- **Question 5** – Create a new column `grade_band` in `student.csv` (Low: ≤9, Medium: 10–14, High: ≥15). Generate a grouped summary table with number of students, average absences, and percent with internet access. Save as `student_bands.csv`.  

- **Question 6** – In `crime.csv`, create a `risk` column (`HighCrime` if `ViolentCrimesPerPop ≥ 0.50`, else `LowCrime`). Group by `risk` and print the average unemployment rate for each group.  

- **Question 7** – Scrape the Wikipedia page on Data Science. Extract and print the page `<title>` and the first meaningful paragraph (≥50 characters) from the main content.  

- **Question 8** – From the same Wikipedia page, extract all `<h2>` section headings (skip References, External links, See also, Notes). Remove `[edit]` and save to `headings.txt`.  

- **Question 9** – Scrape the Machine Learning Wikipedia page. Extract the first table with ≥3 data rows. Normalize rows with missing columns and save as `wiki_table.csv`.  

- **Question 10** – Write a reusable function `find_lines_containing(filename, keyword)` that returns lines containing the keyword (case-insensitive) with line numbers. Test using `sample-file.txt` and print the number of matches and the first 3 lines.  
tail -n 20 README.md

