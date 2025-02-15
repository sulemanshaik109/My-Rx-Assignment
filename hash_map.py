def sort_dict_by_value(data):
    return dict(sorted(data.items(), key=lambda item: item[1]))

if __name__ == "__main__":
    input_data = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}
    output = sort_dict_by_value(input_data)
    print("Output:", output)