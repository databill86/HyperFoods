from matplotlib import pyplot


def matplotlib_function(x_ingredients_embedded1_arg, x_ingredients_embedded2_arg, words_arg, colors, sizes, title):
    # Retrieve all of the vectors from a trained model as follows

    fig_matplotlib, (ax1, ax2) = pyplot.subplots(nrows=1, ncols=2, figsize=(24, 12), dpi=500)
    ax1.set_title('PCA')
    ax2.set_title('T-SNE')
    fig_matplotlib.suptitle(title, fontsize=20)

    ax1.scatter(x_ingredients_embedded1_arg[:, 0], x_ingredients_embedded1_arg[:, 1], c=colors, alpha=0.5, s=sizes)
    ax2.scatter(x_ingredients_embedded2_arg[:, 0], x_ingredients_embedded2_arg[:, 1], c=colors, alpha=0.5, s=sizes)

    words = words_arg

    # ----- PCA

    #for i, word in enumerate(words):
        #ax1.annotate(word, xy=(x_ingredients_embedded1_arg[i, 0], x_ingredients_embedded1_arg[i, 1]))

    # ----- T-SNE

    #for i, word in enumerate(words):
        #ax2.annotate(word, xy=(x_ingredients_embedded2_arg[i, 0], x_ingredients_embedded2_arg[i, 1]))
