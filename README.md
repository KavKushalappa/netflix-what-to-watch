# netflix-what-to-watch
Netflix recommendation tool built on Python

# Netflix: What Should You Watch? 
An interactive Python-based recommendation tool that suggests Netflix shows based on your mood, genre, time available, intensity, and bingeabilty. This includes interactive inputs in Jupyter and visual breakdowns of recommendation drivers with appropriate libraries.
This project has been created to demonstrates how a simple, explainable scoring model can be used to build a lightweight recommender system prototype with a starter dataset form knowledge.

# Features
- Interactive user inputs (mood, genre, time, pacing, intensity, bingeability)
- Top 3 personalized recommendations
- Transparent scoring logic
- Explainability charts showing why a show matched

# How it works
Each show is tagged with attributes like:
- genres
- mood
- intensity
- pacing
- episode runtime
- bingeability
User preferences are converted into a weighted score across these factors, and recommendations are returned.

# Tech stack
- Python (core logic for reccomendations)
- Jupyter Notebook (easy to run)
- ipywidgets (interactivity UI)
- pandas + matplotlib (libraries for analysis + visuals)

# Run the notebook
1. Download or clone the repository
2. Open the notebook: `notebooks/netflix_what_to_watch.ipynb`
3. Run all cells
4. Use the dropdowns/sliders and click **Recommend**


# Note
The show list is a small curated dataset for demonstration purposes.  
