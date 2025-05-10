import random
from datetime import datetime, timedelta

# Sample news by category
news_data = {
    "tehnoloogia": [
        "Tehnoloogiaettevõte tutvustas uut tehisintellekti lahendust.",
        "Nutitelefonide müük kasvas märgatavalt viimases kvartalis.",
        "Teadlased arendavad kvantarvutit tavakasutajale."
    ],
    "spordiuudised": [
        "Eesti jalgpallikoondis võitis pingelise mängu.",
        "Maailmameister murdis jooksurekordi.",
        "Korvpallimeeskond võttis napi võidu lisaajal."
    ],
    "majandus": [
        "Inflatsioon aeglustus teises kvartalis.",
        "Börsil toimus järsk langus tehnoloogiaaktsiate seas.",
        "Uus start-up kaasas rekordilise investeeringu."
    ]
}

def random_date():
    days_ago = random.randint(0, 6)
    date = datetime.now() - timedelta(days=days_ago)
    return date.strftime("%d.%m.%Y")

def generate_news(category):
    selected = random.sample(news_data[category], k=2)
    return [f"{random_date()} - {headline}" for headline in selected]

def add_news(category):
    new_item = input("Sisesta uus uudis: ")
    if new_item.strip():
        news_data[category].append(new_item)
        print("Uudis lisatud!")

def choose_category():
    print("\nVali kategooria:")
    categories = list(news_data.keys())
    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat.capitalize()}")
    choice = input("Sisesta kategooria number: ")
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        return categories[int(choice) - 1]
    else:
        print("Vigane valik.")
        return choose_category()

def is_yes(answer):
    return answer.lower() in ["jah", "j"]

def is_no(answer):
    return answer.lower() in ["ei", "e"]

def ask_yes_no(question):
    while True:
        answer = input(question + " (jah/j või ei/e): ").strip().lower()
        if is_yes(answer):
            return True
        elif is_no(answer):
            return False
        else:
            print("Vigane vastus, palun sisesta 'jah', 'j', 'ei' või 'e'.")

# Main loop
while True:
    category = choose_category()
    print("\nGenereeritud uudised:")
    generated_news = generate_news(category)
    for item in generated_news:
        print(f"- {item}")

    if ask_yes_no("\nKas soovid lisada uue uudise?"):
        add_news(category)

    if not ask_yes_no("\nKas soovid uudised uuesti genereerida?"):
        print("Aitäh kasutamast!")
        break
