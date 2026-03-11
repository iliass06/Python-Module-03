import sys


def max_in_dict(d: dict) -> tuple:
    max_val = -1
    max_key = ""
    for key in d.keys():
        val = d.get(key)
        if val > max_val:
            max_val = val
            max_key = key
    return max_val, max_key


def min_in_dict(d: dict) -> tuple:
    min_val = -1
    min_key = ""
    for key in d.keys():
        val = d.get(key)
        if min_val == -1 or val < min_val:
            min_val = val
            min_key = key
    return min_val, min_key


def ft_parse_into_dict() -> dict | None:
    d = dict()
    digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    err_msg = (
        "please enter valid arguments like this: "
        "(python3 ft_inventory_system.py sword:1 potion:5 shield:2 "
        "armor:3 helmet:1)"
    )

    try:
        if len(sys.argv) == 1:
            raise Exception(err_msg)
        for arg in sys.argv[1:]:
            name = ""
            value_str = ""
            found = False

            for char in arg:
                if char == ":" and not found:
                    found = True
                elif not found:
                    name += char
                else:
                    value_str += char
            if not found or name == "" or value_str == "":
                raise Exception(err_msg)

            value = 0
            for char in value_str:
                digit = digits.get(char)
                if digit is None:
                    raise Exception(
                        "invalid quantity! please enter only numbers "
                        "after ':'."
                    )
                value = (value * 10) + digit

            exist_val = d.get(name)
            if exist_val is not None:
                d.update({name: exist_val + value})
            else:
                d.update({name: value})
        return d
    except Exception as e:
        print(f"Error: {e}")
        return None


def ft_total_items(d: dict) -> int:
    total = 0
    for val in d.values():
        total += val
    return total


def ft_curr_inv(dict_inv: dict) -> None:
    dict_copy = dict()
    dict_copy.update(dict_inv)
    total = ft_total_items(dict_copy)
    for _ in dict_copy.keys():
        max_val, max_key = max_in_dict(dict_copy)
        if total == 0:
            pourcentage = 0.0
        else:
            pourcentage = (max_val * 100) / total
            w_unit = "units"
            if max_val == 1 or max_val == 0:
                w_unit = "unit"
            print(f"{max_key}: {max_val} {w_unit} ({pourcentage:.1f}%)")
            dict_copy.update({max_key: -1})


def ft_stats(d: dict) -> None:
    max_val, max_key = max_in_dict(d)
    min_val, min_key = min_in_dict(d)
    w_unit_max = "units"
    if max_val == 1 or max_val == 0:
        w_unit_max = "unit"
    w_unit_min = "units"
    if min_val == 1 or min_val == 0:
        w_unit_min = "unit"
    print(f"Most abundant: {max_key} ({max_val} {w_unit_max})")
    print(f"Least abundant: {min_key} ({min_val} {w_unit_min})")


def ft_categories(d: dict) -> None:
    categorie = dict()
    abundant = dict()
    moderate = dict()
    scarce = dict()

    for key, val in d.items():
        if val >= 10:
            abundant.update({key: val})
        elif val >= 5:
            moderate.update({key: val})
        else:
            scarce.update({key: val})
    categorie.update({"Abundant": abundant})
    categorie.update({"Moderate": moderate})
    categorie.update({"Scarce": scarce})
    if len(categorie.get("Abundant")) > 0:
        print(f"Abundant: {categorie.get('Abundant')}")

    if len(categorie.get("Moderate")) > 0:
        print(f"Moderate: {categorie.get('Moderate')}")

    if len(categorie.get("Scarce")) > 0:
        print(f"Scarce: {categorie.get('Scarce')}")


if __name__ == "__main__":
    d = ft_parse_into_dict()
    if d is not None:
        print("=== Inventory System Analysis ===")
        total = ft_total_items(d)
        print(f"Total items in inventory: {total}")
        print(f"Unique item types: {len(d)}")
        print("\n=== Current Inventory ===")
        ft_curr_inv(d)
        print("\n=== Inventory Statistics ===")
        ft_stats(d)
        print("\n=== Item Categories ===")
        ft_categories(d)
        print("\n=== Management Suggestions ===")
        min_val, min_key = min_in_dict(d)
        restock_str = ""
        is_first = True
        for key in d:
            val = d.get(key)
            if val == min_val:
                if not is_first:
                    restock_str += ", "
                restock_str += key
                is_first = False
        print(f"Restock needed: {restock_str}")
        print("\n=== Dictionary Properties Demo ===")
        keys_str = ""
        values_str = ""
        is_first = True
        for key in d:
            val = d.get(key)
            if not is_first:
                keys_str += ", "
                values_str += ", "
            keys_str += key
            values_str += f"{val}"
            is_first = False
        print(f"Dictionary keys: {keys_str}")
        print(f"Dictionary values: {values_str}")
        print(f"Sample lookup - 'sword' in inventory: {'sword' in d}")
