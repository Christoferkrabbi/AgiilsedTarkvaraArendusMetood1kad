import random

class ShelterManager:
    def __init__(self):
        self.food = 10
        self.water = 10
        self.morale = 50
        self.health = 100
        self.days_remaining = 30

    def status(self):
        print(f"\n📊 Staatus – Päevi alles: {self.days_remaining}")
        print(f"🥫 Toit: {self.food} | 💧 Vesi: {self.water} | 😊 Moraal: {self.morale} | ❤️ Tervis: {self.health}")

 def check_water_penalty(self):
        if self.water <= 0:
            print("🚨 Sul on veepuudus! Kaotad iga päev tervist ja moraali.")
            self.health -= 5
            self.morale -= 5
            
    def distribute_resources(self):
        if self.food > 0 and self.water > 0:
            self.food -= 1
            self.water -= 1
            self.morale += 5
            print("🍽️ Sa jagasid toitu ja vett. Moraal tõusis.")
        else:
            print("❌ Pole piisavalt toitu või vett.")

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.health += 10
            self.morale += 2
            print("😴 Sa puhkasid ja parandasid tervist.")
        else:
            print("⚠️ Puhkamine ebaõnnestus – nälg halvendab su seisundit.")
            self.health -= 5

    def move_out(self):
        print("🚶 Sa läksid uurima...")
        self.days_remaining -= 1
        self.food -= 2
        self.water -= 2
        chance = random.randint(1, 100)
        if chance <= 50:
            found = random.choice(["food", "water", "morale"])
            if found == "food":
                self.food += 3
                print("🎁 Leidsid toidupaki!")
            elif found == "water":
                self.water += 3
                print("💧 Leidsid veepudeli!")
            else:
                self.morale += 10
                print("📻 Leidsid vana raadiosaate, mis tõstis moraali.")
        else:
            self.health -= 10
            print("⚠️ Sa said vigastada, aga ei leidnud midagi.")

    def wait(self):
        print("🕰️ Otsustasid kohapeale jääda.")
        chance = random.randint(1, 100)
        if chance <= 40:
            self.health -= 10
            self.morale -= 5
            print("💥 Sind rünnati! Kaotasid tervist ja moraali.")
        else:
            print("🤫 Kõik oli vaikne – midagi ei juhtunud.")

    def random_event(self):
        roll = random.randint(1, 100)
        if roll <= 25:
            self.water -= 2
            print("🚱 Veevarustus sai kahjustada! Kaotasid 2 ühikut vett.")
        elif roll <= 50:
            self.food += 2
            print("🎁 Keegi jättis toidupaki varjendi ukse taha.")
        elif roll <= 75:
            self.morale += 10
            print("📻 Leidsid vana päeviku – see tõstis moraali.")
        else:
            self.health -= 10
            print("🤒 Keegi jäi haigeks – kaotasid 10 tervist.")

    def is_alive(self):
        return self.health > 0 and self.morale > 0 and self.days_remaining > 0

# --- Mängu tsükkel ---

def main():
    game = ShelterManager()
    print("☢️ Alustasid mängu: Doomsday shelter")

    while game.is_alive():
        game.status()
        game.random_event()
        print("\n🧭 Tegevused:")
        print("[1] Jaga toitu ja vett")
        print("[2] Puhka")
        print("[3] Uuri väljas")
        print("[4] Oota")

        choice = input("Tee oma valik: ")
        if choice == "1":
            game.distribute_resources()
        elif choice == "2":
            game.rest()
        elif choice == "3":
            game.move_out()
        elif choice == "4":
            game.wait()
        else:
            print("❗ Tundmatu valik.")

        game.days_remaining -= 1

    # --- Mängu lõpp ---
    print("\n🎮 Mäng lõppes.")
    if game.health <= 0:
        print("☠️ Sinu tervis sai otsa.")
    elif game.morale <= 0:
        print("😔 Moraal murdus. Rahvas kaotas usu sinusse.")
    elif game.days_remaining <= 0:
        print("✅ Sa elasid päevad üle ja varjend jäi püsima!")

if __name__ == "__main__":
    main()
