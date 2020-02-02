# MRes Biomedical Research
[github.com/warcraft12321/HyperFoods/blob/master/HyperFoods.ipynb](https://github.com/warcraft12321/HyperFoods/blob/master/HyperFoods.ipynb)

## HyperFoods: Machine intelligent mapping of cancer-beating molecules in foods

## Recipe Retrieval w/ Higher Number Anti-Cancer Molecules

Each recipe had all the ingredients concatenated in single string. It was used the ingredients vocabulary of the dataset
to filter what were and what weren't ingredient names in each string. Finally, it was calculated the sum of the number
of anti-cancer molecules present in each recipe using the table food_compound.csv. A DataFrame object was created so that
it not ony shows us the ID of each recipe, but also the number of anti-cancer molecules, along with an URL to the recipe's
location online.

## Benchmark Facebook Recipe Retrieval Algorithm

It was created a dictionary object (id_url.json) that matches recipes IDs (layer1.json) with the URLs of images available in layer2.json. While
some recipes do not contain images, others contain more than 1. This matching between different files was possible once layer2.json
also contain the recipe ID present in layer1.json.

Then, by manipulating Facebook's algorithm and its repository, the recipe retrieval algorithm is able to convert the JSON file id_url.json into
an array of strings of URLs. Along with this, it creates a parallel array of strings of the IDs of the recipes, so that in each position there is
correspondence between ID in this object with an image URL in the previous.

Finally, Facebook's algorithm was run and the ingredients list for each image URL was obtained. The number of correct elements over the total
number of elements in the ground-truth recipe gives us the accuracy of the algorithm. The ingredients present in each ground-truth recipe
were retrieved using the method above - "Recipe Retrieval w/ Higher Number Anti-Cancer Molecules".

### Supervisors
Kirill Veselkov ([Imperial College London](https://www.imperial.ac.uk/people/kirill.veselkov04)) | Michael Bronstein ([Imperial College London](https://www.imperial.ac.uk/people/m.bronstein))

Roadmap -> [Wiki]()