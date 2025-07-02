import pandas as pd

# Define paths
METADATA_FILE = 'food-101/dish_metadata.csv'

# Simple keyword-based rules for dietary tags
VEG_KEYWORDS = ['pizza', 'salad', 'ice_cream', 'apple_pie', 'cheesecake', 'french_fries']
NON_VEG_KEYWORDS = ['chicken', 'beef', 'pork', 'fish', 'shrimp', 'sushi', 'hamburger']
SPICY_KEYWORDS = ['curry', 'spicy', 'chili', 'tacos', 'hot']

def infer_dietary_tags(dish_name):
    dish_name = dish_name.lower()
    is_veg = None
    is_spicy = None
    
    # Vegetarian check
    if any(keyword in dish_name for keyword in VEG_KEYWORDS):
        is_veg = True
    elif any(keyword in dish_name for keyword in NON_VEG_KEYWORDS):
        is_veg = False
    
    # Spicy check
    if any(keyword in dish_name for keyword in SPICY_KEYWORDS):
        is_spicy = True
    else:
        is_spicy = False
    
    return is_veg, is_spicy

# Update metadata with dietary tags
def add_dietary_tags(metadata_file):
    # Load metadata
    df = pd.read_csv(metadata_file)
    
    # Apply tags
    df[['is_veg', 'is_spicy']] = df['cleaned_dish_name'].apply(
        lambda x: pd.Series(infer_dietary_tags(x))
    )
    
    # Save updated metadata
    df.to_csv(metadata_file, index=False)
    print(f"Dietary tags added. Metadata updated at {metadata_file}")

if __name__ == "__main__":
    add_dietary_tags(METADATA_FILE)