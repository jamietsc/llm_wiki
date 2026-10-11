# Tuning of the output

## 🎯 Goal of this file
The goal of this file is to write down the decision for specific parameters (e.g. top_k or threshhoald) to understand these decisions in the future.

## Top-k-elements

### What it means
The top-k-elements select the top first k chunks out of the sorted array. Best Practice here is to select the variable due to the length of one chunk.

### The decision
For the first tests my decision for this variable was five. Each chunk is relatively large (about 500 words). To much chunks would fill the context of the LLM to fast and important facts could be missed.

## Threshold

### What it means
The threshold replaces elements in a tensor based on a specific limit, with the value the user selects. This value is normaly ``0.0``. The reason for using is to avoid that the LLM will use chunks with a low score, because there are no more chunks left. 

In normal the number in the tensor means: 
| Value | Description |
--- | --- |
0.9+ | Exact or near perfect match
0.7 - 0.8 | High relevance, ideal for strict production cutoffs
0.5 - 0.6 | Moderate relevance, use with caution as it may let in noise
< 0.5 | Weak or irrelevant connectio; filter out

### The decision
For the firsts tests my decision for this is 0.7. The reason is I have not get enough data to look only for a perfect match. 