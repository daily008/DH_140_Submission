“Data sharing” generally refers to the act of releasing data in a form that can be used by other individuals. Promoting data sharing has been the consensus of our academic community today, as it allows people to benefit from current researches in a new approach. Data sharing has been credited with increasing efficiencies in research, more reproducible science, maximizing the use of a valuable resource, allowing for an expansion of innovation, escalating collaboration, and has been credited with the rapid development of COVID-19 vaccines, therapies and diagnostics.

In this study, I would like to take a small step towards the debates on data article by exploring the scholars in which field and which members of a research team are interested in sharing data with a data article. My specific questions are listed as below:
1) Which disciplines have researchers who published more data articles?
2) What type of research teams prefer to publish a data article, a large team with a lot of members or a small team with any a few members?
3) Who usually participate in the data publishing work in a research team, the majority of team members or only a few individual members? 
4) Can the lower-ranking authors of a research article gain more credits by getting a higher ranking in a data article?

There are three .ipynb files in the subfile "codes" in the repository:

-- The "final_project.ipynb" is the main Jupyter notebook for the final project.
-- The "GetRawData.ipynb" is used to get the author information data from Scopous API with the inputed dois of data and research articles.
-- The "DataProcessing.ipynb" is used to compare reformat the output of "GetRawData.ipynb", and calculate the similarity indexes between the author information of each pairs of data articles and research articles.

The dois of data and research articles is stored in "RawData.csv" in the subfile "data". This data is collected in a previous study.

The blog post of this project is at https://daily008.github.io/jblog/posts/final_project-submission.html.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/daily008/DH140_Final/HEAD)