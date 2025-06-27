import os

def rename_pdfs(base_path):
    items = os.listdir(base_path)

    for item in items:
        item_path = os.path.join(base_path, item)

        if os.path.isfile(item_path) and item.endswith('.pdf') and "9002360087-" in item:
            new_name = item.replace("9002360087-", "")
            new_path = os.path.join(base_path, new_name)
            
            os.rename(item_path, new_path)
            print(f'Renamed: {item} -> {new_name}')

if __name__ == "__main__":
    base_path = os.path.join(os.getcwd(), "INFORMACION")
    
    if os.path.exists(base_path) and os.path.isdir(base_path):
        rename_pdfs(base_path)
    else:
        print(f'EL DIRECTORIO INFORMACION NO EXISTE {base_path}')