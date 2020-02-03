# Retrieving units and quantities of each ingredient present in a given recipe.

import inflect
import re


def ingredient_quantities(recipe, ingredients_list, units_list_dict):

    # -------------------------------- Preprocessing Recipe Dataset

    id_ingredients = {}
    id_ingredients[recipe["id"]] = []

    for j in range(0, len(recipe["ingredients"])):

        id_ingredients[recipe["id"]].append({"id": j, "ingredient": (recipe["ingredients"][j]["text"]).lower()})

    # -------------------------------- Extracting Ingredients

    new_ingredients_list = [] # List of ingredients from the vocabulary with spaces instead of underscores.

    for i in range(0, len(ingredients_list)):

        if "_" in ingredients_list[i]:
            new_ingredients_list.append(ingredients_list[i].replace("_", " "))
            continue

        new_ingredients_list.append(ingredients_list[i]) # In case there is no _
    '''
    ingredients_count = {}

    if ingredient_counting:

        for j in range(0, len(new_ingredients_list)):

            ingredients_count[new_ingredients_list[j]] = 0
    '''
    # Dictionary with the ingredients (from the vocabulary of ingredients) and the number of occurrences in recipes.

    new_id_ingredients_tokenized_position = {}

    p = inflect.engine()

    new_id_ingredients_tokenized_position[recipe["id"]] = []

    for k in range(0, len(id_ingredients[recipe["id"]])):

        for j in range(0, len(new_ingredients_list)):

            if (re.search(r"\b" + re.escape(new_ingredients_list[j]) + r"\b", (id_ingredients[recipe["id"]][k])["ingredient"]) or re.search(r"\b" + p.plural(re.escape(new_ingredients_list[j])) + r"\b", (id_ingredients[recipe["id"]][k])["ingredient"])) is not None:

                new_id_ingredients_tokenized_position[recipe["id"]].append({"id": k, "ingredient": new_ingredients_list[j]})
    '''
                if ingredient_counting:
                    ingredients_count[new_ingredients_list[j]] = ingredients_count[new_ingredients_list[j]] + 1
                    print(ingredients_count)
    '''
    # -------------------------------- Extracting Units and Quantities

    ingrs_quants_units = {}

    value = new_id_ingredients_tokenized_position[recipe["id"]]

    ingrs_quants_units[recipe["id"]] = []

    for value2 in range(0, len(value)):

        for i in range(0, len(list(units_list_dict.keys()))):

            if (re.search(r"\b" + re.escape(list(units_list_dict.keys())[i]) + r"\b", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"])) is not None:

                if re.search(r"[1-9][0-9][0-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value[value2]["ingredient"], "quantity": float(re.search(r"[1-9][0-9][0-9]", ((id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"])).group()),"unit": list(units_list_dict.keys())[i], "quantity (g)": float(re.search(r"[1-9][0-9][0-9]",((id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"])).group()) * int(units_list_dict[list(units_list_dict.keys())[i]])})

                    break

                elif re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value[value2]["ingredient"], "quantity": int(((re.search(r"[1-9]/[1-9]",(id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]).group()).split("/"))[0]) / int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]).group()).split("/"))[1]), "unit": list(units_list_dict.keys())[i], "quantity (g)": (int(((re.search(r"[1-9]/[1-9]",(id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]).group()).split("/"))[0]) / int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]).group()).split("/"))[1])) * int(units_list_dict[list(units_list_dict.keys())[i]])})

                    break

                elif re.search(r"[1-9][0-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value[value2]["ingredient"], "quantity": float(re.search(r"[0-9][0-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]).group()), "unit": list(units_list_dict.keys())[i], "quantity (g)": float(re.search(r"[0-9][0-9]",(id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]).group()) * int(units_list_dict[list(units_list_dict.keys())[i]])})

                    break

                else:

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value[value2]["ingredient"], "quantity": float(units_list_dict[list(units_list_dict.keys())[i]]), "unit": list(units_list_dict.keys())[i], "quantity (g)": int(units_list_dict[list(units_list_dict.keys())[i]])})

                    break

            elif i == len(list(units_list_dict.keys())) - 1:

                if re.search(r"[1-9][0-9][0-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value[value2]["ingredient"], "quantity": 200, "unit": value[value2]["ingredient"], "quantity (g)": 200})

                elif re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value[value2]["ingredient"], "quantity": int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]).group()).split("/"))[0]) / int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]).group()).split("/"))[1]), "unit": value[value2]["ingredient"],"quantity (g)": int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]).group()).split("/"))[0]) / int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]).group()).split("/"))[1]) * 200})

                elif re.search(r"[1-9][0-9]", (id_ingredients[recipe["id"]][value[value2]["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value[value2]["ingredient"], "quantity": 200, "unit": value[value2]["ingredient"], "quantity (g)": 200})

                else:

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value[value2]["ingredient"], "quantity": 200, "unit": value[value2]["ingredient"], "quantity (g)": 200})

    return ingrs_quants_units[recipe["id"]]

