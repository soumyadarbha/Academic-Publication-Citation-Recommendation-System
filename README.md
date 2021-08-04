# Academic-Publication-Citation-Recommendation-System

Academic publishing is one of the main method for the re-
searchers in academia to reveal their works to the public and peers.
However, for the newcomers to the academia, finding a most fittable or
interesting topic to them is a huge challenge due to the high volume of
scientic publications in the field. Thus, we propose our Academic Pub-
lication Citation Recommendation System (APCRS). The APCRS can
recommend scientiic readings to the users for the most relevant papers
based on the paper they have read and the topic they want to explore.
The APCRS uses a new proposed metric to assign the score of relevance
to papers to a given paper. The project consists of 3 parts: web-based
application, database management, and algorithm development.

Contribution:

- Proposed a relevance based recommendation scheme based on the count
of mutual citations.
- Built Academic Publication Citation Recommendation System (APCRS),
a fully functional web-service that provide recommendation services for aca-
demic publications.
- Propose a future work direction and make a prototype of recommendation
model based on Word Similarity algorithms.


Dataset:

The dataset for the recommendation system is one of the key role in the entire
project. In our case, we choose to use the citation network dataset provided
by aminer.org[3]. The citation data is extracted from DBLP, ACM, MAG (Mi-
crosoft Academic Graph), and other sources. Each paper is associated with ab-
stract, authors, year, venue, and title. We use the rst version of the dataset
for developing and testing use. The Citation-network V1 of Citation Network
Dataset: DBLP+Citation,ACM Citation network contains 629,814 papers and
over 632,752 citation relationships.
The data format is shown as following:
#* | paperTitle
#@ | Authors
#t | Year
#c | publication venue
#index | index id of this paper
#% | the id of references of this paper (there are multiple lines, with each
indicating a reference)
